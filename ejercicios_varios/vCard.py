import csv

# función para generar el nombre del archivo
"""
1.- letters = "abcdefghijklmnopqrstuvwxyz": Define una cadena de texto que contiene todas las letras del alfabeto en minúscula.
2.- letter_index = (index // 26) % 26: Divide el índice pasado como argumento entre 26, para determinar el índice de la letra correspondiente en la cadena de letras. El resultado se divide entre 26 de nuevo y se calcula el residuo, para asegurarse de que el índice esté dentro del rango de letras disponibles en la cadena.
3.- number_index = index % 26 + 1: Calcula el índice del número correspondiente al archivo. El índice es el residuo de dividir el índice pasado como argumento entre 26, y se le suma 1 para asegurarse de que el índice esté en el rango de 1 a 26.
4.- file_name = f"{letters[letter_index]}{number_index}": Crea una cadena de texto que representa el nombre del archivo, uniendo la letra correspondiente y el número correspondiente.
5.- return file_name: Devuelve el nombre del archivo. 
Primero, el índice se divide entre 26 y se aplica la operación módulo, para obtener el índice de la letra en el alfabeto. Si el índice es menor que 26, entonces el índice de la letra es simplemente el índice del archivo más 1, ya que en este caso solo se usará la primera letra del alfabeto.
Sin embargo, si el índice es mayor o igual a 26, entonces se deben usar dos letras en el folio. En este caso, se divide el resultado anterior entre 26 y se toma el módulo nuevamente, para obtener el índice de la segunda letra. Luego, se concatenan ambas letras para formar el folio.
Por ejemplo, si el índice es 26, la letra correspondiente será 'b' y el folio será "b1". Si el índice es 27, la letra correspondiente será 'b' (índice 1 de la segunda letra) y el folio será "b2". Si el índice es 53, la letra correspondiente será 'ba' (índice 0 de la primera letra y 1 de la segunda letra) y el folio será "ba2".
"""

def get_file_name(index):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter_index = (index // 26) % 26
    number_index = index % 26 + 1
    file_name = f"{letters[letter_index]}{number_index}"
    return file_name

with open('datos.csv') as f:
    reader = csv.DictReader(f)
    for index, row in enumerate(reader):
        first_name = row['\ufeffNombre']
        last_name = row['Apellido']
        phone = row['Celular']
        email = row['Email']
        work_title = row['Puesto de trabajo']
        office_address = f"{row['Calle Oficina']}, {row['Colonia']}, {row['Ciudad']}, {row['Estado']}, {row['Codigo Postal']}, {row['País']}"
        vcf_file_name = f"{get_file_name(index)}.vcf"
        with open(vcf_file_name, 'w') as vcf_file:
            vcf_file.write(f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name} {last_name}\nORG:\nTEL;TYPE=CELL:{phone}\nEMAIL;TYPE=PREF,INTERNET:{email}\nTITLE:{work_title}\nADR;TYPE=WORK:;;{office_address}\nEND:VCARD\n")
