import csv

# Texto de ejemplo
texto = """user_id,email
oi6IhEzu9R,user_2@example.com
fQFLNRDae8,user_5@example.com
fBYRtPtAlC,user_7@example.com
fOSjdLnNP3,user_9@example.com
uxz2jFwr5I,user_1@example.com
zSbmdNiSHH,user_4@example.com
fjM66woroy,user_0@example.com
oh4mHXh8zN,user_3@example.com
gXWj37JC5d,user_8@example.com
4dBdXURAz3,user_6@example.com
"""

# Dividir el texto en líneas
lineas = texto.split('\n')

# Eliminar la última línea en blanco (si la hubiera)
if not lineas[-1]:
    lineas.pop()

# Dividir cada línea en campos utilizando ',' como delimitador
registros = [linea.split(',') for linea in lineas]

# Nombre del archivo CSV
nombre_archivo = "File_A.csv"

# Escribir los registros en un archivo CSV
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    # Escribir el encabezado
    encabezado = registros[0]
    escritor_csv.writerow(encabezado)

    # Escribir los registros
    for registro in registros[1:]:
        escritor_csv.writerow(registro)

print(f"Archivo CSV '{nombre_archivo}' generado exitosamente.")
