import mysql.connector
mydb=mysql.connector.connect(host="localhost",
							user="Debasmita",
                            password="tiger",
                            database="pythonpp")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE pythonpp")
mycursor.execute("CREATE TABLE customers( name char(20), address varchar(100)")
add_customer = ("INSERT INTO customers"
               "(name, address)"
               "VALUES (%s, %s)")
data_customer = {
  'name': 'debasmita',
  'address': 'abcsd1234',
}
mycursor.execute(add_customer, data_customer)

mycusror.execute("SELECT * FROM customers")
myresult=mycursor.fetchall()
for x in myresult:
	print(x)
							
