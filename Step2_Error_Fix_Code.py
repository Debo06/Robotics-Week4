import pandas as pd

file_path = "data/Debo_reservations.csv"

VALID_AIRPORTS = ["SFO", "LAX", "JFK", "ATL", "ORD", "LAS", "MIA", "SEA", "DFW", "DEN"]

def load_reservations(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Could not load file: {e}")  # Fix 1
        return pd.DataFrame()
    return df

def process_reservations(df):
    # Fix 2: Handle blank passenger names
    if "Passenger" in df.columns:
        df = df[df["Passenger"].notna() & (df["Passenger"].str.strip() != "")]

    # Fix 3: Filter invalid or missing fares
    if "Fare" in df.columns:
        df = df[df["Fare"].notna() & (df["Fare"] > 0)]

    # Fix 4: Validate Origin and Destination codes
    if "Origin" in df.columns and "Destination" in df.columns:
        df = df[df["Origin"].isin(VALID_AIRPORTS) & df["Destination"].isin(VALID_AIRPORTS)]

    # Fix 5: Proper deduplication using PNR
    if "PNR" in df.columns:
        df = df.drop_duplicates(subset="PNR")

    return df

if __name__ == "__main__":
    df = load_reservations(file_path)
    clean_df = process_reservations(df)
    print(clean_df.head())
