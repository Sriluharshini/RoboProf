import pandas as pd

# Read the first CSV file
df1 = pd.read_csv(r"C:\Users\anmol\Downloads\Intelligent_System_6741\project\main_course_files\CU_SR_OPEN_DATA_CATALOG_DESC.csv", encoding='utf-16')

# Read the second CSV file
df2 = pd.read_csv(r"C:\Users\anmol\Downloads\Intelligent_System_6741\project\main_course_files\CU_SR_OPEN_DATA_CATALOG_main.csv", encoding='utf-16')

# Merge the two DataFrames based on a common column
# For example, if 'Course ID' is the common column
merged_df = pd.merge(df1, df2, on='Course ID', how='inner')

# Write the merged DataFrame to a new CSV file
merged_df.to_csv("merged_file.csv", index=False)
