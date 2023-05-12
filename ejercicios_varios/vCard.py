import csv
import vobject

# Abrir archivo CSV con los datos
# ruta_archivo = "C:/Usuarios/TuUsuario/Documentos/empleados.csv"
with open('datos.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Crear objeto vCard
        card = vobject.vCard()

        # Agregar nombre y apellido
        card.add('n')
        card.n.value = vobject.vcard.Name(family=row['Apellido'], given=row['Nombre'])

        # Agregar teléfono celular
        card.add('tel')
        card.tel.type_param = 'cell'
        card.tel.value = row['Celular']

        # Agregar email
        card.add('email')
        card.email.value = row['email']

        # Agregar puesto
        card.add('title')
        card.title.value = row['Puesto']

        # Agregar ciudad
        card.add('adr')
        card.adr.type_param = 'work'
        card.adr.value = vobject.vcard.Address(city=row['Ciudad'])

        # Guardar archivo vCard
        with open(f"{row['Nombre']}_{row['Apellido']}.vcf", 'w') as f:
            f.write(card.serialize())
