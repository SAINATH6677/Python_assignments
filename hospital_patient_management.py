def search_by_disease(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"] == disease]


# Example usage
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

result = search_by_disease(patients, "Flu")
print("Patients with Flu:", result)
