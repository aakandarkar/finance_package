from finance_package import (
    load_data,
    compute_summary_stats,
    clean_data,
    add_day_of_week,
    filter_and_save_above_average_volume,
    aggregate_to_weekly,
    graph_candlestick_chart
)

if __name__ == "__main__":
    # Load data
    file_path = './data/finance_charts_apple.csv'
    df = load_data(file_path)

    # Task 1: Compute summary statistics
    max_val, min_val, avg_val = compute_summary_stats(df)
    print(f"Max value: {max_val}, Min value: {min_val}, Average value: {avg_val}")

    # Task 2: Clean data
    df = clean_data(df)

    # Task 3: Add day of the week
    df = add_day_of_week(df)

    # Task 4: Filter and save above average volume
    output_file = './output/filtered_data.csv'
    filter_and_save_above_average_volume(df, output_file)
    print(f"Filtered data saved to {output_file}")

    # Task 5: Aggregate to weekly level
    weekly_df = aggregate_to_weekly(df)

    # Save weekly aggregated data to a new CSV file
    weekly_file = './output/weekly_data.csv'
    weekly_df.to_csv(weekly_file, index=False)
    print(f"Weekly aggregated data saved to {weekly_file}")

    # Task 6: Graph candlestick chart
    graph_candlestick_chart(weekly_df)
