import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', 8)
general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')

# clean the gender field and drops all empty lines in general dataset
general_df.replace({'gender': {'man': 'm', 'woman': 'f'}}, inplace=True)
general_df.dropna(axis='rows', inplace=True, how='all')

# rename the columns for appending
prenatal_df.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
# fill the gender column and drops all empty rows in general dataset
prenatal_df['gender'].fillna('f', inplace=True)
prenatal_df.dropna(axis='rows', inplace=True, how='all')

# rename the columns for appending
sports_df.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
# clean the gender field and drops all empty rows in general dataset
sports_df.replace({'gender': {'male': 'm', 'female': 'f'}}, inplace=True)
sports_df.dropna(axis='rows', inplace=True, how='all')

# append all data and drop the useless column
data = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
data.drop(columns='Unnamed: 0', inplace=True)

# drop empty rows
data.dropna(axis='rows', inplace=True, thresh=3)

# fill the missing data with 0
cols = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
data[cols] = data[cols].fillna(0)

# print the result
# print('Data shape:', data.shape)
# print(data.sample(n=20, random_state=30))

# Q1
# hospital_max = data["hospital"].value_counts().idxmax()
# print(f"The answer to the 1st question is {hospital_max}")

# Q2
# stomach_ratio = data.loc[(data["diagnosis"] == "stomach") & (data["hospital"] == "general")].shape[0] / general_df.shape[0]
# print(f"The answer to the 2nd question is {round(stomach_ratio, 3)}")

# Q3
# dislocation_ratio = data.loc[(data["diagnosis"] == "dislocation") & (data["hospital"] == "sports")].shape[0] / data.loc[data["hospital"] == "sports"].shape[0]
# print(f"The answer to the 3rd question is {round(dislocation_ratio, 3)}")

# Q4
# age_general = general_df["age"].median()
# age_sports = sports_df["age"].median()
# print("The answer to the 4th question is", int(abs(age_general - age_sports)))

# Q5
# bt_table = data.pivot_table(index=['hospital', 'blood_test'], aggfunc='count')
# bt_table.reset_index(inplace=True, level='blood_test')
# bt_max_hospital = bt_table.loc[bt_table['blood_test'] == 't', 'age'].idxmax()
# bt_max = bt_table.loc[bt_table['blood_test'] == 't', 'age'].max()
# print(f"The answer to the 5th question is {bt_max_hospital}, {bt_max} blood tests")

# Q1
plt.hist(data["age"], bins=5)
plt.show()
print(f"The answer to the 1st question: 15-35")

# Q2
plt.pie(data["diagnosis"].value_counts(), labels=list(data["diagnosis"].value_counts().index))
plt.show()
print(f"The answer to the 2nd question: pregnancy")

# Q3
fig, axes = plt.subplots()
plt.violinplot([data.loc[data["hospital"] == "general", "height"], data.loc[data["hospital"] == "prenatal", "height"],
               data.loc[data["hospital"] == "sports", "height"]])
axes.set_xticks((1, 2, 3))
axes.set_xticklabels(("general", "prenatal", "sports"))
plt.show()
print("It's because the height of people in the sports hospital is measured in feet not meters.")
