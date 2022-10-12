#Ejercicio proximos 6 meses.
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

meses = 5
lista = [] #hace una lista
mes_inicial = datetime.strptime((input("Introduce el mes inicial YYMM: ")), '%y%m')
lista.append(mes_inicial) #agrega un elemento al final de la lista 
for i in range(1, meses + 1):
  lista.append(mes_inicial + relativedelta(months=i))
for fecha in lista:  
  print(fecha.strftime('%y%m'))
