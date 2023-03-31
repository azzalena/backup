
# import mysql.connector

# mydb = mysql.connector.connect(
#   host='104.198.155.19',
#   user="root",
#   password="*L3r>&^0fF_U^N/o",
#   database="cen4010sp23g08"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM yourtable")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

import mysql.connector

mydb = mysql.connector.connect(user='Admin', password='pb27783141',
                              host='35.238.214.142',
                              database='cen4010sp23g08')
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM login")

myresult = mycursor.fetchall()

for x in myresult:
   print(x)

mydb.close()