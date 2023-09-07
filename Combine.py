import csv

# Nombre de los archivos de entrada
archivo_a = "File_A.csv"
archivo_b = "File_B.csv"

# Nombre del archivo de salida
archivo_salida = "File_C.csv"

# Cabecera para el archivo de salida
cabecera = ["user_id", "email", "first_name", "last_name"]

# Lista para almacenar todos los registros
registros = []

# Leer y combinar los registros de File_A.csv
with open(archivo_a, 'r') as file_a:
    reader = csv.reader(file_a)
    next(reader)  # Saltar la cabecera de File_A.csv
    for row in reader:
        registros.append(row)

# Leer y combinar los registros de File_B.csv
with open(archivo_b, 'r') as file_b:
    reader = csv.reader(file_b)
    next(reader)  # Saltar la cabecera de File_B.csv
    for row in reader:
        registros.append(row)

# Escribir los registros combinados en el archivo de salida
with open(archivo_salida, 'w', newline='') as file_c:
    writer = csv.writer(file_c)
    
    # Escribir la cabecera en el archivo de salida
    writer.writerow(cabecera)
    
    # Escribir los registros en el archivo de salida
    writer.writerows(registros)

print(f"Archivos {archivo_a} y {archivo_b} combinados en {archivo_salida} exitosamente.")
