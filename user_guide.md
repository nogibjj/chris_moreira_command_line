# Available Actions
The following actions are available in the CLI. Each action corresponds to a different ETL or query operation. Pass one of these actions as a command-line argument when running the tool.


# Prerequisites: 
Python 3.8+ installed on your machine.

Key Package Requirenments:
1. databricks-sql-connector
2. pandas
3. python-dotenv

Databricks environment variables properly set up in a .env file (e.g., DATABRICKS_API_KEY, SERVER_HOST, SQL_HTTP). These will be automatically loaded by the tool.

# Action 1: Extract Dataset
Description: Extracts data from a predefined source and saves it locally.

Run the following
```bash

python main.py extract


```

# Action 2: Load Dataset
Description: Transforms the extracted data and loads it into Databricks.

Run the following
```bash

python main.py load


```

# Action 3: Join Data
Description: Performs a SQL query that joins tables in the Databricks database.

Run the following
```bash

python main.py query_join


```

# Action 4: Aggregate Data
Description: Performs a SQL aggregation query to summarize data by certain fields.

Run the following
```bash

python main.py query_aggregate


```

# Action 5: Sort Data
Description: Performs a SQL query that sorts data by specified fields.

Run the following
```bash

python main.py query_sort


```