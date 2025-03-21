import pandas as pd
import numpy as np 

# Load the CSV file
file_path = "les_wind_speeds.csv"
df = pd.read_csv(file_path,  skiprows=3)


wind_speeds = df.iloc[:, -1] # Last column contains wind speeds

#print(wind_speeds)

output_file_path = 'extracted_real_wind_speeds.csv'
wind_speeds.to_csv(output_file_path, index=False)


# Replace 'file.csv' with your file name
df = pd.read_csv("les_wind_speeds.csv", skiprows=4, header=None)

third_column_list = np.array(df.iloc[:, -1])
  
print(third_column_list)