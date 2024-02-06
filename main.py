import pandas as pd

# Read the CSV files into DataFrames
df1 = pd.read_csv('data/grouped_skills.csv', header=None)
df2 = pd.read_csv('data/categories.csv')

# Split the 'Skills' column of df2 into three separate columns
df2[['Skill1', 'Skill2', 'Skill3']] = df2['Skills'].str.split(',', n=2, expand=True)

# Create a new column in df1 to store matching values from df2
df1['Matching_Category'] = ""

# Iterate through each row in df1
for index, row in df1.iterrows():
    # Combine all three columns into a single string for each row
    combined_skills = ','.join(map(str, row))

    # Check if any string in the combined skills appears in the 'Skill1', 'Skill2', or 'Skill3' columns of df2
    matching_skills = [skill for skill in combined_skills.split(',') if skill in df2[['Skill1', 'Skill2', 'Skill3']].values.flatten()]

    # If there are matching skills, update the 'Matching_Category' column with the corresponding 'Category' from df2
    if matching_skills:
        df1.at[index, 'Matching_Category'] = df2[df2[['Skill1', 'Skill2', 'Skill3']].isin(matching_skills).any(axis=1)]['Category'].values[0]

# Save the updated DataFrame to a new CSV file or use it as needed
df1.to_csv('data/output.csv', header=False, index=False)
