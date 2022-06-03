import os
import shutil
ruta_itla = 'C:\\Users\\bryan\\OneDrive - itla.edu.do\\TAREAS ITLA\\'
ext_documento = ['.docx','.doc']
ext_pdf = ['.pdf']
ext_pptx = ['.pptx']
ext_excel = ['.xlsx','.xlsm','.xlsb','.xltx']
ext_foto = ['.png','.jpg','.jpeg','.gif']
ext_video = ['.mov','.mp4']
ext_ejecutables = ['.exe']
ext_sql = ['.sql']
ext_archivos = ['.rar']
ext_otros = ['.eddx','.txt','.cmd','.xls','.crdownload','.ppsx']

def ordenar (archivo, ext):
    for i in ext_documento:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'WORD')
    for i in ext_pdf:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'PDF')
    for i in ext_pptx:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'Diapositivas')
    for i in ext_excel:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'Excel')
    for i in ext_foto:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'Imagenes')
    for i in ext_video:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'Videos')
    for i in ext_ejecutables:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'Ejecutables')
    for i in ext_sql:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'SQL')
    for i in ext_archivos:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'Archivos')
    for i in ext_otros:
        if ext == i:
            shutil.move(ruta_itla + archivo, ruta_itla + 'Otros')
def main():
    for archivo in os.listdir(ruta_itla):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar(archivo, ext)
main()
