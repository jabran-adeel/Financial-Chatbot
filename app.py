from flask import Flask, render_template, request, jsonify
from data_loader import load_data, get_company_data


df = load_data()

app = Flask(__name__)


def generate_response(user_query: str) -> str:
    """
    Simple rule-based chatbot logic for financial Q&A.
    """
    query = user_query.lower()

    # Identify company
    company = None
    for name in ["microsoft", "apple", "tesla"]:
        if name in query:
            company = name
            break

    if not company:
        return "Please mention one of these companies: Microsoft, Apple, or Tesla."

    # Filter data
    company_df = get_company_data(company, df)
    latest_year = company_df['Year'].max()
    row = company_df[company_df['Year'] == latest_year].iloc[0]

    # Respond to specific keywords
    if "revenue" in query:
        value = row["Total Revenue (USD millions)"]
        return f"{company.title()}'s total revenue in {latest_year} was ${value:,.0f} million."

    elif "net income" in query or "profit" in query:
        value = row["Net Income (USD millions)"]
        return f"{company.title()}'s net income in {latest_year} was ${value:,.0f} million."

    elif "assets" in query and "liabilities" in query:
        assets = row["Total Assets (USD millions)"]
        liabilities = row["Total Liabilities (USD millions)"]
        return (f"In {latest_year}, {company.title()} had total assets of "
                f"${assets:,.0f} million and liabilities of ${liabilities:,.0f} million.")

    elif "assets" in query:
        value = row["Total Assets (USD millions)"]
        return f"{company.title()}'s total assets in {latest_year}: ${value:,.0f} million."

    elif "liabilities" in query:
        value = row["Total Liabilities (USD millions)"]
        return f"{company.title()}'s total liabilities in {latest_year}: ${value:,.0f} million."

    elif "cash" in query or "cash flow" in query:
        value = row["Operating Cash Flow (USD millions)"]
        return f"{company.title()}'s operating cash flow in {latest_year}: ${value:,.0f} million."

    elif "growth" in query or "change" in query:
        # Compare last two years
        years = sorted(company_df["Year"].unique())
        if len(years) < 2:
            return f"Not enough data to calculate {company.title()}'s growth."
        y1, y2 = years[-2], years[-1]
        v1 = company_df.loc[company_df["Year"] == y1, "Total Revenue (USD millions)"].values[0]
        v2 = company_df.loc[company_df["Year"] == y2, "Total Revenue (USD millions)"].values[0]
        change = ((v2 - v1) / v1) * 100
        direction = "increased" if change > 0 else "decreased"
        return (f"{company.title()}'s revenue {direction} by {abs(change):.2f}% "
                f"from {y1} (${v1:,.0f}M) to {y2} (${v2:,.0f}M).")

    else:
        return ("I can answer queries like:\n"
                "- 'What is Microsoft revenue 2024?'\n"
                "- 'Apple assets and liabilities'\n"
                "- 'Tesla cash flow 2023?'\n"
                "Please include the company name in your question.")



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    bot_reply = generate_response(user_input)
    return jsonify({"reply": bot_reply})



if __name__ == "__main__":
    app.run(debug=True)