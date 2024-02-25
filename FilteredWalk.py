import os
import pandas as pd

# Define the base directory where the folders are located
base_directory = "Data"

# Function to process the labels.txt file
def process_labels_file(file_path):
    # Read the file into a pandas DataFrame
    df = pd.read_csv(file_path, sep='\t')
    
    # Filter out rows where the transportation mode is 'walk'
    df_filtered = df[df['Transportation Mode'] != 'walk']
    
    # Save the filtered DataFrame back to the file
    df_filtered.to_csv(file_path, sep='\t', index=False)

# Function to search for labels.txt files and process them
def search_and_process_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == "labels.txt":
                file_path = os.path.join(root, file)
                process_labels_file(file_path)
                print(f"Processed file: {file_path}")

# Call the function with the base directory
search_and_process_files(base_directory)