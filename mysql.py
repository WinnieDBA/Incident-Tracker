import mysql.connector

connection = mysql.connector.connect(
   host="localhost",
    user="root",
    password="Trump2019",
    database="incident_tracker"
)
cursor = connection.cursor()

query ="insert into tanzania (platform,features,source,mno,raiser) values ('mobile','good','Aggregator','airtel','Winnie');"
cursor.execute(query)

print(cursor.rowcount,"record added successfuly")

connection.commit()
connection.close()

