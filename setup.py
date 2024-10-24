from setuptools import setup, find_packages


setup(
    name="DatabricksPipeline",
    version="0.1.0",
    description="DatabricksPipeline",
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
            "etl_query=main:main",
        ],
    },
)
