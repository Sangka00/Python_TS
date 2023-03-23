import pymssql
#DB SERVER ADDRESS
server ='165.244.44.233'
#DATABASE NAME
database = 'ExPle_DEV'
#Connet USER NAME
username ='sa'
#Password
password='init00!!'
#mssql Connection
cnxn=pymssql.connect(server,username,password,database)
cursor = cnxn.cursor()
#SQL execute
cursor.execute('SELECT * FROM [mesuser].PP_WORK_RESULT;')

#data Fetch output
row = cursor.fetchone()

while row:
    print(row[0],row[1],row[2])
    row = cursor.fetchone()
#connect 끊기
cnxn.close()
