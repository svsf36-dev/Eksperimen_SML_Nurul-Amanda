import os
import pandas as pd

def preprocess_data(input_path, output_path):
    if not os.path.exists(output_path):
        print(f"Error: File {input_path} tidak ditemukan.")
        return
    
    df = pd.read_csv(input_path)

    df = df.drop_duplicates()
    df = df.dropna()

    if 'thal' in df.columns:
        df = pd.get_dummies(df, columns=['thal'], drop_first=True)
    
    df.to_csv(output_path, index=False)
    print(f"Sukses: Data bersih disimpan di {output_path}")

if __name__ == "__main__":
    input_file = "heart_disease.csv"
    output_file = "dataset_clean.csv"
    
    preprocess_data(input_file, output_file)