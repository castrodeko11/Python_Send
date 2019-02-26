# # Read CSV
import sap_send
import csv

with open('C:/Users/re91528z/Softtek/csv/data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    email = []
    search = []
    next(readCSV, None)# skip the headers
    for row in readCSV:
       # print(row[10],row[11])
       #email.append(row[10])  # Column e-mail
       #search.append(row[11]) # Column search
       sap_send.enviaremail("deko123456789@hotmail.com", row[10],row[11])

