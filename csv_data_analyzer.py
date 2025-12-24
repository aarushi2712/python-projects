import csv

def analyze_csv(file_name):
    values = []

    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                values.append(float(row[0]))
    except FileNotFoundError:
        print("File not found.")
        return

    if not values:
        print("No data available.")
        return

    print(f"Total: {sum(values)}")
    print(f"Average: {sum(values) / len(values)}")
    print(f"Maximum: {max(values)}")
    print(f"Minimum: {min(values)}")

analyze_csv("data.csv")
