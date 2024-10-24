from setuptools import setup, find_packages

# Setup for packaging and installing the DatabricksPipeline project
setup(
    name="DatabricksPipeline",
    version="0.1.0",
    description="DatabricksPipeline for ETL and querying",
    author="Christian Moreira",
    author_email="chris.moreira@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",  # This allows `etl_query` to run your main() function in main.py
        ],
    },
)
