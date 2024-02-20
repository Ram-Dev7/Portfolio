def collect_data():
    """Collect radiation data until the user decides to stop."""
    data = {}
    while True:
        location = input("Enter location (or 'quit' to stop): ")
        if location.lower() == 'quit':
            break
        measurements = []
        while True:
            measurement = input(f"Enter radiation measurement for {location} (or 'done' to finish): ")
            if measurement.lower() == 'done':
                break
            measurements.append(float(measurement))
        data[location] = measurements
    return data
