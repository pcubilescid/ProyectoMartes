SELECT
	Gender,
	COUNT(*) AS TOTAL
FROM
	HumanResources.Employee
GROUP BY
	HumanResources.Employee.Gender;	


DECLARE @TotalEmployees INT;

SELECT @TotalEmployees = COUNT(*) FROM HumanResources.Employee;

SELECT
	Gender,
	COUNT(*) * 100.0 / @TotalEmployees AS Percentage
FROM
	HumanResources.Employee
GROUP BY
	HumanResources.Employee.Gender;
	 