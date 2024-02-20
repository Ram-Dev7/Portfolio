import statistics

def calculate_statistics(data):
    """Calculate the average and standard deviation of the measurements for each location."""
    stats = {}
    for location, measurements in data.items():
        avg = sum(measurements) / len(measurements)
        std_dev = statistics.stdev(measurements)
        stats[location] = (avg, std_dev)
    return stats
