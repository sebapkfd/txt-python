import os

# Obtiene nombre y ubicación de los archivos
# Funciona para todos los archivos de la carpeta y sub carpetas
# No ingresa el nombre del script ni del archivo recopilatorio
archivos = []
for root, dirs, files in os.walk("."):
	for filename in files:
		if filename != "Reload.py" and filename != "00-Text.txt":
			file_path = os.path.join(root, filename)
			archivos.append((filename,file_path))
        
for archivo in archivos:
	print(archivo)

# Recopila toda la info en un solo string
# Solo ingresa info de archivos .txt
# No copia ni el codigo propio ni la info del archivo recopilatorio
texto = ""
for archivo in archivos:
	if archivo[0].endswith('.txt') and archivo[0] != "Reload.py" and archivo[0] != "00-Text.txt":
		string = open(archivo[1], "r", encoding='latin-1')
		texto += string.read() + '\n'
		string.close()


# Crea el archivo de texto donde se juntará la informacion
# Si el archivo ya estaba creado, lo vacía
# Abre el archivo, copia todo en "00-Text.txt" y cierra el archivo
open("00-Text.txt","w").close()
text = open("00-Text.txt","a")
text.write(texto +'\n')
text.close()