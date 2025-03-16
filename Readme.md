## GDP DATA - WEB Scarping using lxml
---
#### Required Libraries :

```
(if in Jupyter Notebook)
!pip install numpy pandas
!pip install lxml
```

```
(if on Windows, in Windows Shell)
pip install numpy pandas
pip install lxml
```

---
#### Objectives:
- Using webscraping to extract required information from a website.
- Using Pandas to load and process the tabular data as a dataframe.
- Using numpy to manipulate the information contained in the dataframe.
- Load the updated DataFrame into a CSV file.
---
#### Project Scenario:
An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating a script that can extract the list of the top 10 largest economies of the world in descending order of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF).
---
##### The required data seems to be available on the URL mentioned below:

> URL used : https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29

#### Operations performed:
1. Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
2. Replace the column headers with column numbers
3. Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
4. Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
5. Assign column names as "Country" and "GDP (Million USD)"
6. Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
7. Convert the GDP value in Million USD to Billion USD
8. Use numpy.round() method to round the value to 2 decimal places.
9. Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
10. Load the DataFrame to the CSV file named "Largest_economies.csv" or "top 5.csv"
---
#### Top 15 Leading Companies - [Largest Economies](./Largest_Economies.csv)
---
#### Top 5 Leading Companies - [Top 5 Leading Economies](./top5.csv)
---
#### License:
This Py file licensed under [MIT](./LICENSE) License.
