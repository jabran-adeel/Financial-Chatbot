from data_loader import get_company_df
import math

def format_m(n):
    """Format million-dollar numbers nicely (rounded, with commas)."""
    try:
        n = float(n)
    except:
        return str(n)
    if abs(n) >= 1_000:
        # show billions if > 1000 million
        return f"${n/1000:,.2f}B"
    return f"${n:,.0f}M"

def answer_query(user_text, df=None):
    """
    Basic rule-based parser. Recognizes company name and keywords.
    Returns a text answer string.
    """
    text = user_text.lower()
    # detect company: microsoft, apple, tesla
    company = None
    for c in ['microsoft', 'apple', 'tesla']:
        if c in text:
            company = c
            break
    if company is None:
        return "Please mention one company (Microsoft, Apple, or Tesla) in your question."

    cdf = get_company_df(company, df)

    # handle latest year request
    if any(x in text for x in ['latest', 'most recent', '2024', '2023', '2022']):
        # try to extract year
        year = None
        for y in [2024,2023,2022]:
            if str(y) in text:
                year = y
                break
        if year is None:
            year = cdf['Year'].max()

    # revenue
    if 'revenue' in text or 'total revenue' in text or 'sales' in text:
        row = cdf[cdf['Year']==year].iloc[0]
        rev = format_m(row['Total Revenue (USD millions)'])
        return f"{company.title()} total revenue for {year} was {rev}."

    # net income
    if 'net income' in text or 'profit' in text:
        row = cdf[cdf['Year']==year].iloc[0]
        ni = format_m(row['Net Income (USD millions)'])
        return f"{company.title()} net income for {year} was {ni}."

    # assets / liabilities
    if 'assets' in text and 'liabilities' in text:
        row = cdf[cdf['Year']==year].iloc[0]
        a = format_m(row['Total Assets (USD millions)'])
        l = format_m(row['Total Liabilities (USD millions)'])
        return f"In {year}, {company.title()} had total assets of {a} and total liabilities of {l}."

    if 'assets' in text:
        row = cdf[cdf['Year']==year].iloc[0]
        a = format_m(row['Total Assets (USD millions)'])
        return f"{company.title()} total assets in {year}: {a}."

    if 'liabilities' in text:
        row = cdf[cdf['Year']==year].iloc[0]
        l = format_m(row['Total Liabilities (USD millions)'])
        return f"{company.title()} total liabilities in {year}: {l}."

    # operating cash flow
    if 'cash' in text or 'operating cash' in text or 'cash flow' in text:
        row = cdf[cdf['Year']==year].iloc[0]
        cf = format_m(row['Operating Cash Flow (USD millions)'])
        return f"{company.title()} operating cash flow in {year}: {cf}."

    # growth (YoY) requests
    if 'growth' in text or 'change' in text or 'increase' in text or 'decrease' in text:
        years = sorted(cdf['Year'].unique())
        if len(years) < 2:
            return "Not enough years of data to calculate growth."
        # compare latest two years
        y1, y2 = years[-2], years[-1]  # e.g., 2023, 2024
        r1 = float(cdf[cdf['Year']==y1]['Total Revenue (USD millions)'].values[0])
        r2 = float(cdf[cdf['Year']==y2]['Total Revenue (USD millions)'].values[0])
        if r1 == 0:
            return f"Revenue changed from {r1} to {r2} between {y1} and {y2}."
        pct = (r2-r1)/r1*100
        sign = "increased" if pct>0 else "decreased"
        return (f"{company.title()} revenue {sign} by {pct:.1f}% from {y1} to {y2} "
                f"({format_m(r1)} → {format_m(r2)}).")

    # fallback - show available queries
    return ("I can answer questions like:\n"
            "- 'What is Microsoft total revenue 2024?'\n"
            "- 'How has Tesla net income changed?'\n"
            "- 'Apple assets and liabilities 2023'\n"
            "Please mention company and year (optional).")