/*Quiero un listado de ciudades y paises.
Tengo lso datos en dos tablas
person.StateProvince
person.CountryRegion

Para unir dos tablas, usare JOIN*/


Select top 10 * From Person.StateProvince
Select Top 10 * From Person.CountryRegion

Select paises.Name, ciudades.Name  From Person.StateProvince as ciudades
inner join Person.CountryRegion as paises
on ciudades.CountryRegionCode = paises.CountryRegionCode
order by paises.Name, ciudades.Name DESC;

/*Encontrar los 5 paises con mas clientes*/
Select top 5 * from Person.StateProvince;
Select top 5 * from Person.CountryRegion;
Select top 5 * from Person.Address;

Select p.Name, count(a.AddressLine1) as numcli from Person.Address as a
inner join Person.StateProvince as e
on e.StateProvinceID = a.StateProvinceID
inner join Person.CountryRegion as p
on p.CountryRegionCode = e.CountryRegionCode
group by p.name;