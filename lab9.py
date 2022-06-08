import mysql.connector

file = open ("Marvel.txt")
str1 = file.read()
print(str1)
dataBase = mysql.connector.connect(host="localhost",
                                   user = "root",
                                   password = "1234"

)
cursorObj = dataBase.cursor()
cursorObj.execute("CREATE DATABASE MyDatabase")
connection = mysql.connector.connect(host="localhost",
                                     user = "root",
                                     password = "1234"

)
if connection.is_connected():
    info = connection.get_server_info()
    print("connected to version, ",info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("you are connected to database ",record)

try:
    connection  = mysql.connector.connect(host="localhost",
                                         database = "MyDatabase",
                                         user = "root",
                                         password = "1234")


    createTable = """CREATE TABLE Movies(
    ID int(10) NOT NULL,
    MOVIE varchar(30) NOT NULL,
    Date varchar(30) NOT NULL,
    MCUPHASE varchar(20) NOT NULL,
    PRIMARY KEY (ID)
    )"""

    cursor = connection.cursor()
    result = cursor.execute(createTable)
    print("Succesfully created")

    inserting = """ INSERT INTO Movies (ID,MOVIE,Date,MCUPHASE) VALUES (%s,%s,%s,%s)"""
    a = cursor.execute(inserting)
    for i in str1:
        cursor.execute(inserting,i)

    connection.commit()
    connection.close()
    dataBase.commit()
    dataBase.close()





except mysql.connector.Error as error:
    print("Failed to create the table ",error)
