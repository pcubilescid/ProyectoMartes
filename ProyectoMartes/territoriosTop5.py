import pyodbc

server = "DESKTOP-P6M1FBC"
user = "python_conect"
password = "Pyth0n_R3ad3r!!!"
data_base = "AdventureWorks2022"
conexion_str = "DRIVER={SQL Server};" + f'SERVER={server};DATABASE={data_base};UID={user};PWD={password}'
conn = pyodbc.connect(conexion_str)
cursor = conn.cursor()
cursor.execute('Select top 5 [Name] as Nombre, [CountryRegionCode] as Pais, [SalesLastYear] From Sales.SalesTerritory Order by SalesLastYear desc;')
for row in cursor:
    values = [
        row[0],                   # Asumimos que la primera columna es un integer
        row[1],                   # Asumimos que la segunda columna es un string
        float(row[2])
    ]
    print(values)
conn.close()