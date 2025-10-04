import pandas as pd

# Path to your CSV file
CSV_PATH = "financial_data_2022_2024.csv"

def load_data(path: str = CSV_PATH) -> pd.DataFrame:
    """
    Load and preprocess financial data from CSV.
    Ensures correct datatypes and sorting.
    """
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the CSV file at: {path}")

    # Clean and standardize
    df.columns = df.columns.str.strip()
    df['Year'] = df['Year'].astype(int)
    df['Company'] = df['Company'].astype(str).str.strip()
    df = df.sort_values(['Company', 'Year']).reset_index(drop=True)
    return df


def get_company_data(company: str, df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the dataframe by company name (case-insensitive).
    """
    company = company.strip().lower()
    return df[df['Company'].str.lower() == company]