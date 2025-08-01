import pandas as pd

VALID_AIRPORTS = ["SFO", "LAX", "JFK", "ATL", "ORD", "LAS", "MIA", "SEA", "DFW", "DEN"]

def load_reservations(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print("Could not load file")  # TODO-FIX: Doesn't log error details
        return pd.DataFrame()
    return df

def process_reservations(df):
    # TODO-FIX: Drops all rows without checking if Passenger column exists
    df = df[df["Passenger"] != ""]

    # TODO-FIX: Missing handling for missing Fare values (NaN)
    df = df[df["Fare"] > 0]

    # TODO-FIX: Doesn't check if Origin and Destination columns contain valid values
    df = df[df["Origin"].isin(VALID_AIRPORTS)]
    df = df[df["Destination"].isin(VALID_AIRPORTS)]

    # TODO-FIX: Duplicates based only on Passenger name instead of PNR
    df = df.drop_duplicates(subset="Passenger")

    return df

if __name__ == "__main__":
    df = load_reservations("data/reservations.csv")
    clean_df = process_reservations(df)
    print(clean_df.head())
