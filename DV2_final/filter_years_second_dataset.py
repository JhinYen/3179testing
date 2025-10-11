import pandas as pd

def filter_demographic_data(input_file, output_file, start_year=2000, end_year=2015):
    """
    Filter the demographic data to only include records from specified year range
    
    Parameters:
    input_file (str): Path to input CSV file
    output_file (str): Path to output filtered CSV file
    start_year (int): Starting year (inclusive)
    end_year (int): Ending year (inclusive)
    """
    
    # Read the CSV file
    print(f"Reading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    # Display original size
    original_rows = len(df)
    print(f"Original dataset has {original_rows} rows")
    
    # Filter data for years 2000-2015
    print(f"Filtering data for years {start_year} to {end_year}...")
    filtered_df = df[(df['Time'] >= start_year) & (df['Time'] <= end_year)]
    
    # Display filtered size
    filtered_rows = len(filtered_df)
    print(f"Filtered dataset has {filtered_rows} rows")
    print(f"Reduced by {original_rows - filtered_rows} rows ({((original_rows - filtered_rows)/original_rows)*100:.1f}%)")
    
    # Save the filtered data
    print(f"Saving filtered data to {output_file}...")
    filtered_df.to_csv(output_file, index=False)
    
    print("Done!")
    
    # Show year range in filtered data
    years_in_filtered = filtered_df['Time'].unique()
    print(f"Years in filtered data: {sorted(years_in_filtered)}")

# Usage
if __name__ == "__main__":
    input_filename = "Demographic_Indicators_Medium.csv"
    output_filename = "Demographic_Indicators_2000_2015.csv"
    
    filter_demographic_data(input_filename, output_filename)