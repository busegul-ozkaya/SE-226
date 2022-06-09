import mysql.connector
count =0
file = "marvel.txt"


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
    ID int(100) NOT NULL,
    MOVIE varchar(100) NOT NULL,
    Date varchar(100) NOT NULL,
    MCUPHASE varchar(100) NOT NULL,
    PRIMARY KEY(ID)
    )"""

    cursor = connection.cursor()
    result = cursor.execute(createTable)
    print("Succesfully created")


except mysql.connector.Error as error:
    print("Failed to create the table ",error)

try:
    connection=mysql.connector.connect(host="localhost",database="MyDatabase",user="root",passwd="1234")
    cursor = connection.cursor()
    inserting = """INSERT INTO Movies(ID,MOVIE,Date,MCUPHASE) VALUES (%s,%s,%s,%s)"""
    with open(file,"r") as f:
     for line in f:
        split=line.split()
        a=(split[0],split[1],split[2],split[3])
        cursor.execute(inserting, a)
        connection.commit()
    print("successfully inserted")


except mysql.connector.Error as error:
    print("Failed to insert record into Movies table {}".format(error))


#a. select * from Movies
#b. delete from Movies where MOVIE = 'TheIncredibleHulk';
#c. select * from movies where MCUPHASE='Phase2'
#d. update movies set Date = 'November3,2017' where MOVIE = 'Thor:Ragnarok'