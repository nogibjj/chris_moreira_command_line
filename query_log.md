# Query Log

This document captures the SQL queries executed and their respective results from the Databricks pipeline.

## Structure

- **Query**: The SQL query that was executed.
- **Results**: The output of the query execution.

---

## Query 1: [Placeholder for Query Description]

The following SQL operations are performed: 


```sql
#JOINING
 WITH artist_version AS (
            SELECT 
                DISTINCT artist_name,
                CASE 
                    WHEN artist_name LIKE '%,%' THEN 'Multiple Artists'
                    ELSE 'Single Artist'
                END AS Single_Double
            FROM csm_87_SpotifyDB
        )
        SELECT 
            s.*,
            a.Single_Double
        FROM csm_87_SpotifyDB s
        LEFT JOIN artist_version a
        ON s.artist_name = a.artist_name
```
```sql
#Aggregating
SELECT 
            s.released_year,
            COUNT(s.track_name) AS track_count,
            SUM(s.in_spotify_playlists) AS total_in_spotify_playlists,
            COUNT(
                CASE WHEN a.Single_Double = 'Single Artist' THEN 1 END
            ) AS single_artist_count,
            COUNT(
                CASE WHEN a.Single_Double = 'Multiple Artists' THEN 1 END
            ) AS multiple_artist_count
        FROM csm_87_SpotifyDB s
        LEFT JOIN (
            SELECT 
                DISTINCT artist_name,
                CASE 
                    WHEN artist_name LIKE '%,%' THEN 'Multiple Artists'
                    ELSE 'Single Artist'
                END AS Single_Double
            FROM csm_87_SpotifyDB
        ) a
        ON s.artist_name = a.artist_name
        GROUP BY s.released_year
```

```sql
#SORTING
SELECT 
            s.released_year,
            COUNT(s.track_name) AS track_count,
            SUM(s.in_spotify_playlists) AS total_in_spotify_playlists,
            COUNT(
                CASE WHEN a.Single_Double = 'Single Artist' THEN 1 END
            ) AS single_artist_count,
            COUNT(
                CASE WHEN a.Single_Double = 'Multiple Artists' THEN 1 END
            ) AS multiple_artist_count
        FROM csm_87_SpotifyDB s
        LEFT JOIN (
            SELECT 
                DISTINCT artist_name,
                CASE 
                    WHEN artist_name LIKE '%,%' THEN 'Multiple Artists'
                    ELSE 'Single Artist'
                END AS Single_Double
            FROM csm_87_SpotifyDB
        ) a
        ON s.artist_name = a.artist_name
        GROUP BY s.released_year
        ORDER BY s.released_year
```