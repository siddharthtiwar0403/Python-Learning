import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv("dummy_data.csv")

# Create report
profile = ProfileReport(
    df,
    title="Student Placement Dataset Report",
    explorative=True
)

# Save report
profile.to_file("student_report.html")