import os

def find_files_with_content(root_path, text):
    for dirpath, dirnames, files in os.walk(root_path):
        for file_name in files:
            file_path = os.path.join(dirpath, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    if text in file.read():
                        print(f"Encontrado en: {file_path}")
            except Exception as e:
                print(f"No se pudo leer el archivo {file_path}: {e}")

# Reemplaza '/' con el directorio raíz si es necesario
root_search_path = '/Users/andy/Projects/search-py/'
search_text = '0x01'

find_files_with_content(root_search_path, search_text)