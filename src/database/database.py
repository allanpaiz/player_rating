import sqlite3

def create_connection(db_file): # Creates a connection to the database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


# Broken code

# def create_box_score_table(conn):
#     cursor = conn.cursor()
#     cursor.execute(
#         CREATE TABLE IF NOT EXISTS box_score (
#             id INTEGER PRIMARY KEY,
#             gameId TEXT NOT NULL,
#             team TEXT NOT NULL,
#             player TEXT NOT NULL,
#             name TEXT NOT NULL,
#             result TEXT NOT NULL,
#             loc TEXT NOT NULL,
#             MinP TEXT NOT NULL,
#             FGMade TEXT NOT NULL,
#             FGAtt TEXT NOT NULL,
#             FGPer TEXT NOT NULL,
#             twoPMade TEXT NOT NULL,
#             twoPAtt TEXT NOT NULL,
#             twoPPer TEXT NOT NULL,
#             threePMade TEXT NOT NULL,
#             threePAtt TEXT NOT NULL,
#             threePPer TEXT NOT NULL,
#             FTMade TEXT NOT NULL,
#             FTAtt TEXT NOT NULL,
#             FTPer TEXT NOT NULL,
#             OffReb TEXT NOT NULL,
#             DefReb TEXT NOT NULL,
#             TotReb TEXT NOT NULL,
#             Ast TEXT NOT NULL,
#             Stl TEXT NOT NULL,
#             Blk TEXT NOT NULL,
#             Tov TEXT NOT NULL,
#             PFoul TEXT NOT NULL,
#             Pts TEXT NOT NULL
        
#     )
#    )

