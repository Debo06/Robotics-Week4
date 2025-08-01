import csv
import random
from faker import Faker

fake = Faker()

AIRPORTS = ["SFO", "LAX", "JFK", "ATL", "ORD", "LAS", "MIA", "SEA", "DFW", "DEN"]

def generate_reservations(n=200):
    reservations = []
    for i in range(n):
        pnr = fake.unique.bothify(text='???###')
        passenger = fake.name() if random.random() > 0.025 else ""  # 2.5% blank
        origin = random.choice(AIRPORTS + [""])  # 5% invalid
        dest = random.choice(AIRPORTS + ["XXX"])  # 5% invalid
        fare = round(random.uniform(-50, 1000), 2) if random.random() < 0.05 else round(random.uniform(100, 500), 2)
        status = random.choice(["Confirmed", "Pending", "Cancelled"])
        reservations.append([pnr, passenger, origin, dest, fare, status])
    return reservations

def save_to_csv(filename, reservations):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["PNR", "Passenger", "Origin", "Destination", "Fare", "Status"])
        writer.writerows(reservations)

if __name__ == "__main__":
    import sys
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    data = generate_reservations(count)
    save_to_csv("data/Debo_reservations.csv", data)
    print(f"Generated {count} synthetic reservations.")
