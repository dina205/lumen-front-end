import mysql.connector

# create a connection object
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# create a cursor object
mycursor = mydb.cursor()

# execute a query
mycursor.execute("SELECT * FROM events")

# fetch the results
results = mycursor.fetchall()

# iterate over the results
for result in results:
    print(result)
