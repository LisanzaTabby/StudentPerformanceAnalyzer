import pandas as pd
import matplotlib.pyplot as plt
# Loading the Student Performance Dataset

df = pd.read_csv('student_performance_dataset.csv')

#print(df)

# Calculating Avergare score of every student to be displayed as an extra column in the dataset
df['Average'] = df[['Maths', 'English', 'Science']].mean(axis=1)
print(df)

top_performing_student = df.loc[df["Average"].idxmax()]
lowest_performing_student = df.loc[df["Average"].idxmin()]
class_average = df["Average"].mean()

print(
    f"Top Performing Student: "
    f"{top_performing_student['FName']} "
    f"{top_performing_student['LName']} "
    f"with Average Score: "
    f"{top_performing_student['Average']}"
)

print(
    f"Lowest Performing Student: "
    f"{lowest_performing_student['FName']} "
    f"{lowest_performing_student['LName']} "
    f"with Average Score: "
    f"{lowest_performing_student['Average']}"
)
print(f"Class Average Score: {class_average}")

# Visualizing the Average Scores of Students using a Bar Chart

vis = df.plot.bar(x='FName', y='Average', title='Average Scores of Students', legend=False, rot=0)

plt.xlabel('Students')
plt.ylabel('Average Score')
plt.show()