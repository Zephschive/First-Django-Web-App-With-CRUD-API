# postgres-sample-dbs

A collection of sample Postgres databases for learning, testing, and development.

# How the dataset files were created

Data was loaded into [Neon Serverless Postgres](https://neon.tech/) (Postgres 15). The data was then dumped using the [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html) utility. For example:

```bash
pg_dump "postgres://<user>:<password>@<hostname>/<dbname>" --file=[file_name].sql --format=p --no-owner --no-privileges
```

For larger datasets, such as the [employees](#employees-database) database, the following format option was used: `--format=c`

### Clone the repository to your local machine

```bash
git clone https://github.com/danieltprice/postgres-sample-dbs.git
```

### Download an individual dump file

You can download an individual dump file from this repo on the GitHub site or using `wget`.

From this repo on the GitHub site:

1. Click on the dump file to open it.
2. Above the content of the file, you should see a button labeled "Raw". Click it. This will open a new tab or window in your browser displaying the raw contents of the file.
3. Right-click anywhere in the window or tab displaying the raw file contents, and select "Save As..." or "Save Page As ..." from the context menu. Choose a location on your computer to save the file, and click "Save".

Using wget:

get https://raw.githubusercontent.com/danieltprice/postgres-sample-dbs/main/<dump_file_name.sql>


## Prerequisites

- A `psql` client for connecting to your Neon database and loading data. This client is included with a standalone PostgreSQL installation. See [PostgreSQL Downloads](https://www.postgresql.org/download/).
- A `pg_restore` client if you are loading the [employees](#employees-database) or [postgres_air](#postgres-air-database) database. The `pg_restore` client is also included with a standalone PostgreSQL installation. See [PostgreSQL Downloads](https://www.postgresql.org/download/).
- A Neon database connection string to load data and connect to your database. After creating a database, you can obtain the connection string from the **Connection Details** widget on the Neon **Dashboard**. In the instructions that follow, replace `postgres://<user>:<password>@<hostname>/[dbname]` with your Neon database connection string. For further information, see [Connect from any application](https://neon.tech/docs/connect/connect-from-any-app).
- Instructions for each dataset require that you create a database. You can do so from a client such as `psql` or from the [Neon SQL Editor](https://neon.tech/docs/get-started-with-neon/query-with-neon-sql-editor).
- A Neon [Pro](/https://neon.tech/docs/introduction/pro-plan) account is required to install datasets larger than 3 GBs.

## Sample data

Sample datasets are listed in order of the smallest to largest installed size. Please be aware that the Neon Free Tier has a storage limit of 3 GBs per branch. Datasets larger than 3 GBs cannot be loaded on the Free Tier.

| Name                                                | Tables | Records | Source file size      | Installed size |
|-----------------------------------------------------|--------|------   |-----------------------|----------------|
| [Periodic table data](#periodic-table-data)         | 1      | 118     | 17 KB                 | 7.2 MB         |
| [World Happiness Index](#world-happiness-index)     | 1      | 156     | 9.4 KB                | 7.2 MB         |
| [Titanic passenger data](#titanic-passenger-data)   | 1      | 1309    | 220 KB                | 7.5 MB         |
| [Netflix data](#netflix-data)                       | 1      | 8807    | 3.2 MB                | 11 MB          |
| [Pagila database](#pagila-database)                 | 33     | 62322   | 3 MB                  | 15 MB          |
| [Chinook database](#chinook-database)               | 11     | 77929   | 1.8 MB                | 17 MB          |
| [Lego database](#lego-database)                     | 8      | 633250  | 13 MB                 | 42 MB          |
| [Employees database](#employees-database)           | 6      | 3919015 | 34 MB                 | 333 MB         |
| [Wikipedia vector embeddings](#wikipedia-vector-embeddings) | 1    | 25000    | 1.7 GB         | 850 MB         |
| [Postgres air](#postgres-air-database)              | 10     | 67228600 | 1.2 GB               | 6.7 GB         |

<Admonition type="note">
Installed size is measured using the query: `SELECT pg_size_pretty(pg_database_size('your_database_name'))`. The reported size for small datasets may appear larger than expected due to inherent Postgres storage overhead.
</Admonition>

### Periodic table data

A table containing data about the periodic table of elements.

1. Create a `periodic_table` database:

    ```sql
    CREATE DATABASE periodic_table;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/periodic_table.sql
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    <CodeBlock shouldWrap>

    ```bash
    psql -d "postgres://<user>:<password>@<hostname>/periodic_table" -f periodic_table.sql
    ```

    </CodeBlock>

4. Connect to the `periodic_table` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/periodic_table
    ```

5. Look up the the element with the Atomic Number 10:

    ```sql
    SELECT * FROM periodic_table WHERE "AtomicNumber" = 10;
    ```

- Source: [https://github.com/andrejewski/periodic-table](https://github.com/andrejewski/periodic-table)
- License: [ISC License](https://github.com/andrejewski/periodic-table/blob/master/LICENSE)

`Copyright (c) 2017, Chris Andrejewski <christopher.andrejewski@gmail.com>`

### World Happiness Index

A dataset with multiple indicators for evaluating the happiness of countries of the world.

1. Create a `world_happiness` database:

    ```sql
    CREATE DATABASE world_happiness;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/happiness_index.sql
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    ```bash
    psql -d "postgres://<user>:<password>@<hostname>/happiness_index" -f happiness_index.sql
    ```

4. Connect to the `titanic` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/world_happiness_index
    ```

5. Find the countries where the happiness score is above average but the GDP per capita is below average:

    ```sql
    SELECT 
        country_or_region,
        score,
        gdp_per_capita
    FROM 
        "2019"
    WHERE 
        score > (SELECT AVG(score) FROM "2019") 
        AND 
        gdp_per_capita < (SELECT AVG(gdp_per_capita) FROM "2019")
    ORDER BY 
        score DESC;
    ```

- Source: [https://www.kaggle.com/datasets/unsdsn/world-happiness](https://www.kaggle.com/datasets/unsdsn/world-happiness)
- License: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

### Titanic passenger data

A dataset containing information on the passengers aboard the RMS Titanic, which sank on its maiden voyage in 1912.

1. Create a `titanic` database:

    ```sql
    CREATE DATABASE titanic;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/titanic.sql
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    <CodeBlock shouldWrap>

    ```bash
    psql -d "postgres://<user>:<password>@<hostname>/titanic" -f titanic.sql
    ```

    </CodeBlock>

4. Connect to the `titanic` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/titanic
    ```

5. Query passengers with the most expensive fares:

    ```sql
    SELECT name, fare
    FROM passenger
    ORDER BY fare DESC
    LIMIT 10;
    ```

- Source: [https://www.kaggle.com/datasets/ibrahimelsayed182/titanic-dataset](https://www.kaggle.com/datasets/ibrahimelsayed182/titanic-dataset)
- License: [Unknown](https://www.kaggle.com/datasets/vinicius150987/titanic3)

### Netflix data

A dataset containing information about movies and tv shows on Netflix.

1. Create a `netflix` database:

    ```sql
    CREATE DATABASE netflix;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/netflix.sql
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    <CodeBlock>

    ```bash
    psql -d "postgres://<user>:<password>@<hostname>/netflix" -f netflix_shows.sql
    ```

    </CodeBlock>

4. Connect to the `netflix` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/netflix
    ```

5. Find the directors with the most movies in the database:

    ```sql
    SELECT 
        director,
        COUNT(*) AS "Number of Movies"
    FROM 
        netflix_shows
    WHERE 
        type = 'Movie'
    GROUP BY 
        director
    ORDER BY 
        "Number of Movies" DESC
    LIMIT 5;
    ```

- Source: [https://www.kaggle.com/datasets/shivamb/netflix-shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- License: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

### Pagila database

Sample data for a fictional DVD rental store. Pagila includes tables for films, actors, film categories, stores, customers, payments, and more.

1. Create a `pagila` database:

    ```sql
    CREATE DATABASE pagila;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/pagila.sql
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    ```bash
    psql -d "postgres://<user>:<password>@<hostname>/pagila" -f pagila.sql
    ```

4. Connect to the `pagila` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/pagila
    ```

5. Find the top 10 most popular film categories based on rental frequency:

    ```sql
    SELECT c.name AS category_name, COUNT(r.rental_id) AS rental_count
    FROM category c
    JOIN film_category fc ON c.category_id = fc.category_id
    JOIN inventory i ON fc.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    GROUP BY c.name
    ORDER BY rental_count DESC
    LIMIT 10;
    ```

- Source: [https://github.com/devrimgunduz/pagila](https://github.com/devrimgunduz/pagila)
- License: [LICENSE.txt](https://github.com/devrimgunduz/pagila/blob/master/LICENSE.txt)
- `Copyright (c) Devrim Gündüz <devrim@gunduz.org>`

### Chinook database

A sample database for a digital media store, including tables for artists, albums, media tracks, invoices, customers, and more.

1. Create a `chinook` database:

    ```sql
    CREATE DATABASE chinook;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/chinook.sql
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    <CodeBlock shouldWrap>

    ```bash
    psql -d "postgres://<user>:<password>@<hostname>/chinook" -f chinook.sql
    ```

    </CodeBlock>

4. Connect to the `chinook` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/chinook
    ```

5. Find out the most sold item by track title:

    ```sql
    SELECT 
    T."Name" AS "Track Title",
    SUM(IL."Quantity") AS "Total Sold"
    FROM 
        "Track" T
    JOIN 
        "InvoiceLine" IL ON T."TrackId" = IL."TrackId"
    GROUP BY 
        T."Name"
    ORDER BY 
        "Total Sold" DESC
    LIMIT 1;
    ```

- Source: [https://github.com/lerocha/chinook-database](https://github.com/lerocha/chinook-database)
- License: [LICENSE.md](https://github.com/lerocha/chinook-database/blob/master/LICENSE.md)
- `Copyright (c) 2008-2017 Luis Rocha`

### Lego database

A dataset containing information about various LEGO sets, their themes, parts, colors, and other associated data.

1. Create a `lego` database:

    ```sql
    CREATE DATABASE lego;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/lego.sql
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    ```bash
    psql -d "postgres://<user>:<password>@<hostname>/lego" -f lego.sql
    ```

4. Connect to the `lego` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/lego
    ```

5. Find the top 5 LEGO themes by the number of sets:

    ```sql
    SELECT lt.name AS theme_name, COUNT(ls.set_num) AS number_of_sets
    FROM lego_themes lt
    JOIN lego_sets ls ON lt.id = ls.theme_id
    GROUP BY lt.name
    ORDER BY number_of_sets DESC
    LIMIT 5;
    ```

- Source: [https://www.kaggle.com/datasets/rtatman/lego-database](https://www.kaggle.com/datasets/rtatman/lego-database)
- License: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

### Employees database

A dataset containing details about employees, their departments, salaries, and more.

1. Create the database and schema:

    ```sql
    CREATE DATABASE employees;
    \c employees
    CREATE SCHEMA employees;
    ```

2. Download the source file:

    <CodeBlock shouldWrap>

    ```bash
    wget https://raw.githubusercontent.com/neondatabase/postgres-sample-dbs/main/employees.sql.gz
    ```

    </CodeBlock>

3. Navigate to the directory where you downloaded the source file, and run the following command:

    <CodeBlock shouldWrap>

    ```bash
    pg_restore -d postgres://<user>:<password>@<hostname>/employees -Fc employees.sql.gz -c -v --no-owner --no-privileges
    ```

    </CodeBlock>

    Database objects are created in the `employees` schema rather than the `public` schema.

4. Connect to the `employees` database:

    ```bash
    psql postgres://<user>:<password>@<hostname>/employees
    ```

5. Find the top 5 departments with the highest average salary:

    ```sql
    SELECT d.dept_name, AVG(s.amount) AS average_salary
    FROM employees.salary s
    JOIN employees.department_employee de ON s.employee_id = de.employee_id
    JOIN employees.department d ON de.department_id = d.id
    WHERE s.to_date > CURRENT_DATE AND de.to_date > CURRENT_DATE
    GROUP BY d.dept_name
    ORDER BY average_salary DESC
    LIMIT 5;
    ```

- Source: The initial dataset was created by Fusheng Wang and Carlo Zaniolo from Siemens Corporate Research, and can be found in XML format at this location: [http://timecenter.cs.aau.dk/software.htm](http://timecenter.cs.aau.dk/software.htm). Designing the relational schema was undertaken by Giuseppe Maxia while Patrick Crews was responsible for transforming the data into a format compatible with MySQL. Their work can be accessed here: [https://github.com/datacharmer/test_db](https://github.com/datacharmer/test_db). Subsequently, this information was adapted to a format suitable for PostgreSQL: [https://github.com/h8/employees-database](https://github.com/h8/employees-database). The data was generated, and there are inconsistencies.
- License: This work is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.

## Licensing

This repository is provided under the MIT License. However, please note that each individual database included in this repository is subject to its own license terms.

The MIT License applies to the scripts and other components that we created. We respect the rights of the original creators of the databases, and we only redistribute these databases in compliance with their respective licenses.

For each individual database, we have clearly indicated where the full text of the license can be found. If you choose to use any of these databases, you must comply with the terms specified in their respective licenses.
