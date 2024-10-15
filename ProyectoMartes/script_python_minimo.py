import pyodbc

server = "DESKTOP-P6M1FBC"
user = "python_reader"
password = "Pyth0n_R3ad3r!!!"
data_base = "AdventureWorks2022"
conexion_str = "DRIVER={SQL Server};" + f'SERVER={server};DATABASE={data_base};UID={user};PWD={password}'
conn = pyodbc.connect(conexion_str)
cursor = conn.cursor()
cursor.execute('SELECT * FROM [AdventureWorks2022].[Production].[Location]')
for row in cursor:
    values = [
        row[0],                   # Asumimos que la primera columna es un integer
        row[1],                   # Asumimos que la segunda columna es un string
        float(row[2]),            # Convertimos la tercera columna a Decimal a float
        float(row[3]),            # Convertimos la cuarta columna Decimal a float
        row[4].strftime("%d/%m/%Y")# Formateamos la quinta columna como fecha datetime
    ]
    print(values)
conn.close()