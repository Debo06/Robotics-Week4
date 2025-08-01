import pandas as pd

file_path = "data/Debo_reservations.csv"

VALID_AIRPORTS = {"SFO", "LAX", "JFK", "ATL", "ORD", "LAS", "MIA", "SEA", "DFW", "DEN"}

def load_reservations(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Could not load file: {e}")
        return pd.DataFrame()
    return df

def process_reservations(df):
    # Drop rows with missing or blank Passenger names
    df = df[df.get("Passenger").fillna("").str.strip() != ""]

    # Keep rows with positive Fare values
    df = df[df.get("Fare", pd.Series(dtype='float')).fillna(-1) > 0]

    # Filter valid Origin and Destination airports
    df = df[
        df.get("Origin", "").isin(VALID_AIRPORTS) &
        df.get("Destination", "").isin(VALID_AIRPORTS)
    ]

    # Drop duplicates by PNR
    df = df.drop_duplicates(subset="PNR", keep="first")

    return df

if __name__ == "__main__":
    df = load_reservations(file_path)
    clean_df = process_reservations(df)
    print(clean_df.head())
