import pandas as pd
# from sdv.tabular import CTGAN
import numpy as np

# Sample EHR/EMR dataset schema
def generate_data(num):
    data = pd.DataFrame({
    "Patient_ID": np.arange(1, num+1),
    "Age": np.random.randint(18, 90, num),
    "Gender": np.random.choice(["Male", "Female"], num),
    "Diagnosis": np.random.choice(["Diabetes", "Hypertension", "Healthy", "Cardiac Issue"], num),
    "Medications": np.random.choice(["Metformin", "Lisinopril", "Aspirin", "None"], num),
    "Lab_Results": np.round(np.random.uniform(50, 200, num), 2),
    "Hospital_Stay_Days": np.random.randint(1, 15, num)
})
    return data
        






# data = pd.DataFrame({
#     "Patient_ID": np.arange(1, 101),
#     "Age": np.random.randint(18, 90, 100),
#     "Gender": np.random.choice(["Male", "Female"], 100),
#     "Diagnosis": np.random.choice(["Diabetes", "Hypertension", "Healthy", "Cardiac Issue"], 100),
#     "Medications": np.random.choice(["Metformin", "Lisinopril", "Aspirin", "None"], 100),
#     "Lab_Results": np.round(np.random.uniform(50, 200, 100), 2),
#     "Hospital_Stay_Days": np.random.randint(1, 15, 100)
# })

data=generate_data(1000)

# Export the data to a CSV file
csv_filename = "synthetic_ehr_data.csv"
data.to_csv(csv_filename, index=False)
print(f"Data exported to {csv_filename}")
