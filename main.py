import mysql.connector

DB_HOST = "127.0.0.1"
DB_NAME = "spotify"
DB_USER = "root"
DB_PASS = "Fizzladygel1@"


def main():
    spotifyDataBase = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    passwd = DB_PASS,
    database = DB_NAME
    )
    
    print(spotifyDataBase)

    # preparing a cursor object
    cursorObj = spotifyDataBase.cursor()
    
    # Disconnecting from the server
    spotifyDataBase.close()

if __name__ == "__main__":
    main()