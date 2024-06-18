import pandas as pd
import numpy as np
from datetime import datetime
import calendar
import plotly.graph_objects as go

def load_data(file_path):
    """
    Load the CSV data into a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def compute_summary_stats(df):
    """
    Compute max, min, and average values from 'AAPL.Close'.
    """
    max_value = df['AAPL.Close'].max()
    min_value = df['AAPL.Close'].min()
    avg_value = df['AAPL.Close'].mean()
    return max_value, min_value, avg_value

def clean_data(df):
    """
    Ensure the time series data is clean, removing duplicates if any (though
    current dataset is assumed clean).
    """
    df = df.drop_duplicates()
    df = df.sort_values('Date')
    return df

def add_day_of_week(df):
    """
    Add a new column 'DayOfWeek' to the DataFrame indicating the day of the week.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    df['DayOfWeek'] = df['Date'].dt.day_name()
    return df

def filter_and_save_above_average_volume(df, output_file):
    """
    Find the average volume for the entire dataset and filter out rows
    with volume below average, saving the result to a new CSV file.
    """
    average_volume = df['AAPL.Volume'].mean()
    filtered_df = df[df['AAPL.Volume'] >= average_volume]
    filtered_df.to_csv(output_file, index=False)

def aggregate_to_weekly(df):
    """
    Aggregate the dataset to weekly level and save as a new DataFrame.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    weekly_df = df.resample('W-Mon', on='Date').agg({
        'AAPL.Open': 'first',
        'AAPL.High': 'max',
        'AAPL.Low': 'min',
        'AAPL.Close': 'last',
        'AAPL.Volume': 'sum',
        'AAPL.Adjusted': 'last',
        'dn': 'last',
        'mavg': 'last',
        'up': 'last',
        'direction': 'last'
    })
    weekly_df.reset_index(inplace=True)
    return weekly_df

def graph_candlestick_chart(df):
    """
    Graph the results from weekly aggregation as a candlestick chart.
    (You'll need to install plotly or another library for this visualization)
    """

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                         open=df['AAPL.Open'],
                                         high=df['AAPL.High'],
                                         low=df['AAPL.Low'],
                                         close=df['AAPL.Close'])])

    fig.update_layout(title='Weekly Candlestick Chart for AAPL',
                      xaxis_title='Date',
                      yaxis_title='Price')

    fig.show()

if __name__ == "__main__":
    # Load data
    file_path = 'data/finance_charts_apple.csv'
    df = load_data(file_path)
    # Task 1: Compute summary statistics
    max_val, min_val, avg_val = compute_summary_stats(df)
    print(f"Max value: {max_val}, Min value: {min_val}, Average value: {avg_val}")

    # Task 2: Clean data
    clean_df = clean_data(df)
    # # Task 3: Add day of the week
    
    clean_df = add_day_of_week(clean_df)

    # Task 4: Filter and save above average volume
    output_file = 'output/filtered_data.csv'
    filter_and_save_above_average_volume(clean_df, output_file)
    print(f"Filtered data saved to {output_file}")

    # Task 5: Aggregate to weekly level
    weekly_df = aggregate_to_weekly(clean_df)

    # Save weekly aggregated data to a new CSV file
    weekly_file = 'output/weekly_data.csv'
    weekly_df.to_csv(weekly_file, index=False)
    print(f"Weekly aggregated data saved to {weekly_file}")

    # Task 6: Graph candlestick chart
    graph_candlestick_chart(weekly_df)
