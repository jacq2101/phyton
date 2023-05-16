import csv

with open('datos.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        first_name = row['\ufeffNombre']
        last_name = row['Apellido']
        phone = row['Celular']
        email = row['Email']
        work_title = row['Puesto de trabajo']
        office_address = f"{row['Calle Oficina']}, {row['Colonia']}, {row['Ciudad']}, {row['Estado']}, {row['Codigo Postal']}, {row['País']}"

        vcf_file_name = f"{first_name}_{last_name}.vcf"
        with open(vcf_file_name, 'w') as vcf_file:
            vcf_file.write(f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nFN:{first_name} {last_name}\nORG:\nTEL;TYPE=CELL:{phone}\nEMAIL;TYPE=PREF,INTERNET:{email}\nTITLE:{work_title}\nADR;TYPE=WORK:;;{office_address}\nEND:VCARD\n")
