# Query Commands

This file contains the queries used to generate each of the formatted tables needed for the graph figures. These queries can either be scripted or pasted into preferred SQL tool.

### playlists_false.csv

```
SELECT \*
FROM playlists
WHERE collaborative = false
ORDER BY numfollowers DESC
```

### playlists_true.csv

```
SELECT \*
FROM playlists
WHERE collaborative = true
ORDER BY numfollowers DESC
```

### playlists.csv

```
SELECT \*
FROM playlists
```
