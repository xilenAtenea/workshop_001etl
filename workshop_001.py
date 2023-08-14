import mysql.connector
import csv
import json

with open('config_db.json') as config_json:
    config = json.load(config_json)
conx = mysql.connector.connect(**config) 

mycursor = conx.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS candidates (id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(20),last_name VARCHAR(20),email VARCHAR(50),application_date DATE,country VARCHAR(60),yoe int,seniority VARCHAR(15),technology VARCHAR(50),code_challenge_Score int,technical_intrvw_score int)")

count = "SELECT count(*) FROM candidates"
mycursor.execute(count)
data_in_db = mycursor.fetchone()[0]>0
print(data_in_db)

consulta = "INSERT INTO candidates (first_name, last_name, email, application_date, country, yoe, seniority, technology, code_challenge_Score, technical_intrvw_score) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

if not data_in_db:
    with open('C:/dataset/candidates.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Saltar la primera línea que contiene los nombres de las columnas
        for row in reader:
            datos = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            mycursor.execute(consulta, datos)

    conx.commit()

mycursor.execute("SELECT * FROM candidates ORDER BY id DESC LIMIT 5")
results = mycursor.fetchall()

for row in results:
    print(row)

conx.commit()
mycursor.close()
conx.close()
