# Finance Package

A Python package for analyzing stock data. This package provides functionalities to load, clean, analyze, and visualize Apple stock data, with a focus on ease of use and reproducibility.

```
finance_package/
│
├── finance_package/
│   ├── __init__.py
│   └── apple_stock_analysis.py
│
├── data/
│   └── finance-charts-apple.csv
│
├── output/
│   ├── __init__.py
│   └── filtered_data.csv
│
├── tests/
│   ├── __init__.py
│   └── run_analysis.py
│
├── setup.py
└── README.md
```




## Installation

To install the package, clone the repository and run:

```bash
pip install .
```

## Functionality : Modules and Functions
apple_stock_analysis.py: Contains all the core functions for data loading, cleaning, analysis, and visualization.
apple_load_data(file_path): Load the CSV data into a pandas DataFrame.
apple_compute_summary_stats(df): Compute max, min, and average values from 'AAPL.Close'.
apple_clean_data(df): Ensure the time series data is clean, removing duplicates and sorting by date.
apple_add_day_of_week(df): Add a new column 'DayOfWeek' indicating the day of the week for each date.
apple_filter_and_save_above_average_volume(df, output_file): Filter out rows with volume below the dataset's average and save the result to a CSV file.
apple_aggregate_to_weekly(df): Aggregate the dataset to a weekly level.
apple_graph_candlestick_chart(df): Graph the weekly aggregated data as a candlestick chart.

## Development Approach
### Approach to Solving the Problem
Data Loading: The data is loaded using pandas' read_csv function for easy manipulation and analysis.
Data Cleaning: Ensured that the data is free from duplicates and sorted by date.
Analysis: Computed summary statistics such as max, min, and average closing prices.
Filtering: Filtered the dataset to include only rows with volume above the average.
Aggregation: Aggregated the data to a weekly level to make trends more apparent.
Visualization: Created a candlestick chart to visually represent the weekly trends.

### Rationale for Choices
Pandas: Chosen for its powerful data manipulation capabilities.
Plotly: Selected for its ability to create interactive and visually appealing charts.
Python Standard Libraries: Used datetime for date manipulations and numpy for numerical operations.
Code Quality and Best Practices
Modular Functions: Each function performs a single, well-defined task.
Documentation: Docstrings provided for each function to explain its purpose and usage.
Error Handling: Basic error handling to ensure robustness.
Readability: Code is written to be easy to read and understand, following PEP 8 guidelines.

### Challenges and Future Improvements
Data Quality: Although the dataset was assumed clean, real-world data often requires more rigorous cleaning and validation.
Performance: For very large datasets, performance optimizations might be necessary.
Enhanced Visualizations: Adding more interactive features or different types of visualizations could provide deeper insights.
Unit Tests: Implementing comprehensive unit tests to ensure code reliability.
Next Steps
Unit Testing: Implement detailed unit tests for each function.
Performance Optimization: Explore ways to optimize the code for better performance with larger datasets.
Additional Features: Consider adding more analytical functions or visualizations based on user feedback.

### Running Tests
To run the tests, navigate to the tests directory and execute the run_analysis.py script:

```bash
cd finance_package/tests
python run_analysis.py
```


