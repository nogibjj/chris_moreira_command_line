import os
from databricks import sql
from dotenv import load_dotenv
import logging
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.DEBUG)

logging.debug(f"Before loading .env - SERVER_HOST: " f"{os.getenv('SERVER_HOST')}")
logging.debug(f"Before loading .env - SQL_HTTP: " f"{os.getenv('SQL_HTTP')}")
logging.debug(
    f"Before loading .env - DATABRICKS_API_KEY: " f"{os.getenv('DATABRICKS_API_KEY')}"
)

load_dotenv(override=True)

logging.debug(f"After loading .env - SERVER_HOST: " f"{os.getenv('SERVER_HOST')}")
logging.debug(f"After loading .env - SQL_HTTP: " f"{os.getenv('SQL_HTTP')}")
logging.debug(
    f"After loading .env - DATABRICKS_API_KEY: " f"{os.getenv('DATABRICKS_API_KEY')}"
)


def get_connection():
    server_h = os.getenv("SERVER_HOST")
    access_token = os.getenv("DATABRICKS_API_KEY")
    http_path = os.getenv("SQL_HTTP")

    logging.debug(f"Connecting to Databricks at: {server_h}{http_path}")

    try:
        connection = sql.connect(
            server_hostname=server_h, http_path=http_path, access_token=access_token
        )
        return connection
    except Exception as e:
        logging.error(f"Failed to connect to Databricks: {e}")
        raise


def query_join():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        WITH artist_version AS (
            SELECT DISTINCT artist_name,
                CASE 
                    WHEN artist_name LIKE '%,%' 
                    THEN 'Multiple Artists'
                    ELSE 'Single Artist'
                END AS Single_Double
            FROM csm_87_SpotifyDB
        )
        SELECT s.*, a.Single_Double
        FROM csm_87_SpotifyDB s
        LEFT JOIN artist_version a
        ON s.artist_name = a.artist_name
    """
    cursor.execute(query)
    cursor.fetchall()
    connection.close()
    return "Join Success"


def query_aggregate():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT s.released_year, COUNT(s.track_name) AS track_count,
               SUM(s.in_spotify_playlists) AS total_in_spotify_playlists,
               COUNT(CASE WHEN a.Single_Double = 'Single Artist' THEN 1 END) 
               AS single_artist_count,
               COUNT(CASE WHEN a.Single_Double = 'Multiple Artists' THEN 1 END) 
               AS multiple_artist_count
        FROM csm_87_SpotifyDB s
        LEFT JOIN (
            SELECT DISTINCT artist_name,
                CASE 
                    WHEN artist_name LIKE '%,%' 
                    THEN 'Multiple Artists'
                    ELSE 'Single Artist'
                END AS Single_Double
            FROM csm_87_SpotifyDB
        ) a
        ON s.artist_name = a.artist_name
        GROUP BY s.released_year
    """
    cursor.execute(query)
    cursor.fetchall()
    connection.close()
    return "Aggregate Success"


def query_sort():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT s.released_year, COUNT(s.track_name) AS track_count,
               SUM(s.in_spotify_playlists) AS total_in_spotify_playlists,
               COUNT(CASE WHEN a.Single_Double = 'Single Artist' THEN 1 END) 
               AS single_artist_count,
               COUNT(CASE WHEN a.Single_Double = 'Multiple Artists' THEN 1 END) 
               AS multiple_artist_count
        FROM csm_87_SpotifyDB s
        LEFT JOIN (
            SELECT DISTINCT artist_name,
                CASE 
                    WHEN artist_name LIKE '%,%' 
                    THEN 'Multiple Artists'
                    ELSE 'Single Artist'
                END AS Single_Double
            FROM csm_87_SpotifyDB
        ) a
        ON s.artist_name = a.artist_name
        GROUP BY s.released_year
        ORDER BY s.released_year
    """
    cursor.execute(query)
    records = cursor.fetchall()
    logging.debug(f"Sort Query Results: {records}")
    connection.close()

    return "Sort Success" if records else "Sort Failed"
