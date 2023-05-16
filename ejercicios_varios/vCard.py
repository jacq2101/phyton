import csv

# función para generar el nombre del archivo
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
