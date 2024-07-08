import os
import pandas as pd

def standardize_headers(folder_path, header_variances):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    for file_name in csv_files:
        file_path = os.path.join(folder_path, file_name)

        df = pd.read_csv(file_path)

        new_columns = {}
        for column in df.columns:
            for key, value in header_variances.items():
                if column in value:
                    new_columns[column] = key
                    break
            else:
                new_columns[column] = column

        df = df.rename(columns=new_columns)

        df.to_csv(file_path, index=False)

header_variances = {
    'Email': ['Email', 'email', 'Email address', 'email id', 'e-mail'],
    'Name': ['Name', 'name', 'Full Name', 'First Name', 'Last Name'],
    'Age': ['Age', 'age', 'DOB', 'Date of birth', 'Birthday']
}

standardize_headers(r"\Users\Daniel\Desktop\DataA\python csvs", header_variances)