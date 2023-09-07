import csv

# Texto de ejemplo
texto = """user_id,first_name,last_name
oh4mHXh8zN,Julie,Mosser
zSbmdNiSHH,Taryn,Jaycox
fBYRtPtAlC,John,Smith
fjM66woroy,Yadira,Irving
fQFLNRDae8,Vella,Lynam
fOSjdLnNP3,Qiana,Walk
uxz2jFwr5I,Benito,Festa
oi6IhEzu9R,Leatrice,Oquinn
4dBdXURAz3,Jacques,Cuellar
gXWj37JC5d,Shaun,Kreiger
"""

# Dividir el texto en líneas
lineas = texto.split('\n')

# Eliminar la última línea en blanco (si la hubiera)
if not lineas[-1]:
    lineas.pop()

# Dividir cada línea en campos utilizando ',' como delimitador
registros = [linea.split(',') for linea in lineas]

# Nombre del archivo CSV
nombre_archivo = "File B.csv"

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
