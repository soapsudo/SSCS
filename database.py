from dependencies import *

class Database:
    
    def makeConnection(self):
        try:
            sqliteConnection = sqlite3.connect('database/records.db')
            cursor = sqliteConnection.cursor()
        
        except sqlite3.Error as error:
            print("Error while connecting to sqlite ", error)
        
        return cursor
    
    def runQuery(self, query):
        
        returnArray = []
        
        cursor = self.makeConnection()
        cursor.execute(query)
        
        result = cursor.fetchall()
        cursor.close()
        
        for element in result:
            returnArray += element
            
        return returnArray
        
    def setup(self):
        
        cursor = self.makeConnection()
        
        setupQuery = """
            CREATE TABLE IF NOT EXISTS type (
                type_id INTEGER PRIMARY KEY,
                name VARCHAR
            );
        
            CREATE TABLE IF NOT EXISTS container (
                container_id INTEGER PRIMARY KEY,
                name VARCHAR,
                type_id INTEGER,
                FOREIGN KEY (type_id) REFERENCES type (type_id)
            );
        
            INSERT INTO type (name)
            SELECT 'apache'
            WHERE NOT EXISTS (
                SELECT 1 FROM type WHERE name = 'apache'
            );
        
            INSERT INTO type (name)
            SELECT 'nginx'
            WHERE NOT EXISTS (
                SELECT 1 FROM type WHERE name = 'nginx'
                );
            """
              
        cursor.executescript(setupQuery)
        cursor.close()
        