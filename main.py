import pandas as pd

def extract_files(file_name):
    return pd.read_csv(file_name)

def filter_data(data, country):
    mask = data["country"] == country
    return data[mask]
    
def balance(data):
    data["box_office"] = pd.to_numeric(data["box_office"], errors="coerce")
    data["budget"] = pd.to_numeric(data["budget"], errors="coerce")
    
    data["balance"] = data['box_office'] - data["budget"]
    return data

def remove(data):
    data = data.drop(["language", "country", "duration", "budget", "box_office"], axis=1)
    return data

def sort(data):
    return data.sort_values(by="balance", ascending=False)

def first_ten(data):
    return data.iloc[0:10]

def update(data, country):
    file_name = f"{country}.xlsx"
    data.to_excel(file_name, index = False)
    
extract_files("movies.csv").pipe(filter_data, "USA").pipe(balance).pipe(remove).pipe(sort).pipe(first_ten).pipe(update, "USA")
extract_files("movies.csv").pipe(filter_data, "Russia").pipe(balance).pipe(remove).pipe(sort).pipe(first_ten).pipe(update, "Russia")
extract_files("movies.csv").pipe(filter_data, "UK").pipe(balance).pipe(remove).pipe(sort).pipe(first_ten).pipe(update, "UK")
extract_files("movies.csv").pipe(filter_data, "South Korea").pipe(balance).pipe(remove).pipe(sort).pipe(first_ten).pipe(update, "South Korea")