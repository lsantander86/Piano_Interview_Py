import requests
import csv

# Define los parámetros
url = "https://sandbox.piano.io/id/api/v1/publisher/users/get"
aid = "o1sRRZSLlw"
api_token = "xeYjNEhmutkgkqCZyhBn6DErVntAKDx30FqFOS6D"
email_template = "user_{}@example.com"

# Crear un archivo CSV para escribir los datos
csv_filename = "datos_usuarios.csv"
with open(csv_filename, "w", newline="") as csv_file:
    # Definir el encabezado del archivo CSV
    fieldnames = ["user_id", "email", "first_name", "last_name"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Loop para obtener los datos para cada correo
    for i in range(10):  # user_0@example.com hasta user_9@example.com
        email = email_template.format(i)

        # Define los datos que se enviarán en la solicitud POST
        data = {
            "aid": aid,
            "api_token": api_token,
            "email": email
        }

        # Realiza la solicitud POST
        response = requests.post(url, data=data)

        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            user_data = response.json()  # Suponiendo que la respuesta es JSON
            first_name = user_data.get("first_name")
            last_name = user_data.get("last_name")
            uid = user_data.get("user_id")

            # Escribe los datos en el archivo CSV
            csv_writer.writerow({
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "user_id": uid
            })
        else:
            print(f"Error al obtener datos para {email}: Código de estado {response.status_code}")

print(f"Los datos se han guardado en {csv_filename}")
