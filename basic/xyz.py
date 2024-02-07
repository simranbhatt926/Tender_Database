import mysql.connector\

mydb1=mysql.connector.connect(host="localhost",
                             user="root",
                             password="root",
                             database="tender_management_system")
print(mydb1)
