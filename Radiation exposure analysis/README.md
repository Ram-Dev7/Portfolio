# Physics Experiment: Radiation Exposure Analysis

## Case Study Overview

Dr. Eleanor, a distinguished physicist, is conducting a physics experiment to measure average radiation levels in diverse environments characterized by high amounts of radioactive waste. This comprehensive study spans several weeks, during which Dr. Eleanor collects extensive data from various locations, ranging from urban areas to dense forests. To ensure accuracy, she takes measurements at varying distances from known radiation sources, accounting for background or ambient, naturally occurring radiation. Multiple measurements at different times of the day are recorded for each location to capture variations.

## Experiment Requirements

To process the vast amount of data collected, Dr. Eleanor requires a program capable of efficiently handling numerous measurements. The program's functionality should enable her to input radiation measurements for each location and then calculate essential statistical insights. These insights include:

- **Average Radiation Level:** Determining the central tendency of the measurements.
- **Standard Deviation:** Understanding the variability within the dataset.
- **Other Relevant Metrics:** Identifying patterns or anomalies in the data for comprehensive analysis.

Given the repetitive nature of data input and the calculations required for each set of measurements, the program is designed to utilize loops effectively. For instance, a for loop iterates over each location's dataset, while nested loops process individual measurements within those sets. Additionally, the program provides an option for Dr. Eleanor to continue inputting data until she decides to stop, making use of a while loop.

## Program Structure

The code for this experiment has been organized into modular components:

- **input_module.py:** Handles the collection of radiation data, allowing input until the user decides to stop.
- **calculation_module.py:** Calculates statistical insights, including average radiation levels and standard deviations, for each location.
- **main.py:** Orchestrates the data collection and calculation processes and prints the results.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/radiation-experiment.git
   ```

2. Run the program:

   ```bash
   python main.py
   ```

3. Follow the prompts to input radiation measurements for each location and analyze the calculated statistical insights.

## Future Enhancements

- Include visualization for a more intuitive representation of data.
- Implement a database for storing and retrieving experiment data.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute by submitting pull requests or reporting issues.
