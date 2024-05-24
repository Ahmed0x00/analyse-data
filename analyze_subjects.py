import json
import pandas as pd

# Read data from Faculty of CS.json
with open('Faculty of CS.json', 'r') as f:
    faculty_data = json.load(f)

# Create a pandas DataFrame from the data
df = pd.DataFrame(faculty_data)

# Extract the marks into a separate DataFrame
marks_df = pd.DataFrame(df['Marks'].tolist())

# Define the mark ranges and labels
mark_ranges = {
    '45-50': (45, 50),
    '50-55': (50, 55),
    '60-65': (60, 65),
    '65-70': (65, 70),
    '70-75': (70, 75),
    '75-80': (75, 80),
    '80-85': (80, 85),
    '85-95': (85, 95),
}

# Analyze the marks for each subject
def analyze_marks():
    with open('results/subject-analysis.txt', 'w') as f:
        for subject in marks_df.columns:           
            f.write(f"Analyzing {subject} marks:\n")
            
            for mark_label, (low, high) in mark_ranges.items():
                count = ((marks_df[subject] >= low) & (marks_df[subject] < high)).sum()
                f.write(f"  Number of students with mark {mark_label}: {count}\n")
            
            count = (marks_df[subject] < 50).sum()
            f.write(f"  Number of students who Failed: {count}\n")
            
            count = (marks_df[subject] > 95).sum()
            f.write(f"  Number of students with mark Higher than 95: {count}\n")
            f.write(f"  Average mark in {subject}: {round(marks_df[subject].mean())}\n\n")


# Analyze the number of students who failed in each subject
def analyze_failed_students(marks_df):
    num_failed_students = (marks_df < 45).sum()
    return num_failed_students

# Analyze the number of students who failed in a certain number of subjects
def analyze_num_subjects_failed(marks_df):
    num_subjects_failed = marks_df.lt(45).sum(axis=1)
    num_students_failed = num_subjects_failed.value_counts()
    return num_students_failed

def analyze_students():
    with open('results/subject-analysis.txt', 'a') as f:
        f.write("Student Analysis:\n")
        
        num_students_failed = analyze_num_subjects_failed(marks_df)
        for subject_num, students_num in num_students_failed.items():
            f.write(f"Number of students failed in {subject_num} subjects: {students_num}\n")
        
        f.write("\nSubject Analysis:\n")
        num_failed_students = analyze_failed_students(marks_df)
        for subject, num_failed in num_failed_students.items():
            f.write(f"{subject}: {num_failed} failed students\n")
