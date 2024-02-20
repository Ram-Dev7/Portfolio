from input_module import collect_data
from calculation_module import calculate_statistics

def main():
    """Orchestrate the data collection and calculation processes, and print the results."""
    data = collect_data()
    stats = calculate_statistics(data)
    for location, (avg, std_dev) in stats.items():
        print(f"Location: {location}, Average: {avg}, Standard Deviation: {std_dev}")

if __name__ == "__main__":
    main()
