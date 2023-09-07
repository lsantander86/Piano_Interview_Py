import requests
import csv

BASE_URL = "https://sandbox.piano.io/id/api/v1/publisher/users/get"
API_TOKEN = "xeYjNEhmutkgkqCZyhBn6DErVntAKDx30FqFOS6D"
APP_ID = "o1sRRZSLlw" 

def get_user_id(email, user_id):

    # Define API endpoint and parameters
    params = {
        "aid": "o1sRRZSLlw",
        "api_token": "xeYjNEhmutkgkqCZyhBn6DErVntAKDx30FqFOS6D",
        "email": email,
        "uid": ""
    }

    # Hit the API
    response = requests.post(BASE_URL, params=params)

    uid = ""
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        uid = data["uid"]

    if uid == user_id or uid == "":
        return user_id
    else:
        return uid

def read_csv_as_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return {row["user_id"]: row for row in reader}

# Read both files
data_a = read_csv_as_dict('file_a.csv')
data_b = read_csv_as_dict('file_b.csv')

# Combine the two datasets
combined_list = []

for user_id, user_data in data_a.items():
    if user_id in data_b:
        uid = get_user_id(user_data["email"], user_id)
        combined_entry = {
            "user_id": uid,
            "email": user_data["email"],
            "first_name": data_b[user_id]["first_name"],
            "last_name": data_b[user_id]["last_name"]
        }
        combined_list.append(combined_entry)

# Write the result to a CSV file
with open('combined_PYTHON.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=["user_id", "email", "first_name", "last_name"])
    writer.writeheader()
    for item in combined_list:
        writer.writerow(item)