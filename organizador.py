import os
import shutil

# Ruta de la carpeta que querés organizar
carpeta_origen = '/home/f0f0/Documentos/prueba'  

# Diccionario con categorías de archivos
tipos_archivos = {
    'Documentos': ['.pdf', '.docx', '.txt'],
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'Hojas de cálculo': ['.xls', '.xlsx'],
    'Presentaciones': ['.pptx'],
    'Código': ['.py', '.js', '.html', '.css'],
    'Otros': []
}

# Crear carpetas si no existen
for categoria in tipos_archivos:
    ruta = os.path.join(carpeta_origen, categoria)
    if not os.path.exists(ruta):
        os.mkdir(ruta)

# Mover archivos
for archivo in os.listdir(carpeta_origen):
    ruta_archivo = os.path.join(carpeta_origen, archivo)
    
    if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()
        movido = False
        
        for categoria, extensiones in tipos_archivos.items():
            if extension in extensiones:
                destino = os.path.join(carpeta_origen, categoria, archivo)
                shutil.move(ruta_archivo, destino)
                movido = True
                break

        if not movido:
            destino = os.path.join(carpeta_origen, 'Otros', archivo)
            shutil.move(ruta_archivo, destino)

print("Archivos organizados correctamente 🚀")
