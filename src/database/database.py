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

def create_box_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS box_score (id INTEGER PRIMARY KEY, 
                gameId TEXT NOT NULL, team TEXT NOT NULL, player TEXT NOT NULL, name TEXT NOT NULL, result TEXT NOT NULL, loc TEXT NOT NULL,
                MP TEXT NOT NULL, FG TEXT NOT NULL, FGA TEXT NOT NULL, FG% TEXT NOT NULL, 2P TEXT NOT NULL, 2PA TEXT NOT NULL, 2P% TEXT NOT NULL,   
                3P TEXT NOT NULL, 3PA TEXT NOT NULL, 3P% TEXT NOT NULL, FT TEXT NOT NULL, FTA TEXT NOT NULL, FT% TEXT NOT NULL,
                ORB TEXT NOT NULL, DRB TEXT NOT NULL, TRB TEXT NOT NULL, AST TEXT NOT NULL, STL TEXT NOT NULL, BLK TEXT NOT NULL, TOV TEXT NOT NULL, 
                PF TEXT NOT NULL, PTS TEXT NOT NULL,
                TS% TEXT NOT NULL, eFG% TEXT NOT NULL, 3PAr TEXT NOT NULL, FTr TEXT NOT NULL, ORB% TEXT NOT NULL, DRB% TEXT NOT NULL, TRB% TEXT NOT NULL,
                AST% TEXT NOT NULL, STL% TEXT NOT NULL, BLK% TEXT NOT NULL, TOV% TEXT NOT NULL, USG% TEXT NOT NULL, ORtg TEXT NOT NULL, DRtg TEXT NOT NULL, 
                BPM TEXT NOT NULL
)""")

def create_line_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS line_score (id INTEGER PRIMARY KEY, 
                gameId TEXT NOT NULL, date TEXT NOT NULL, team TEXT NOT NULL, 1 TEXT NOT NULL, 2 TEXT NOT NULL, T TEXT NOT NULL, result TEXT NOT NULL, loc TEXT NOT NULL,
                Pace TEXT NOT NULL, eFG% TEXT NOT NULL, TOV% TEXT NOT NULL, ORB% TEXT NOT NULL, FT/FGA TEXT NOT NULL, ORtg TEXT NOT NULL
)""")                   
    
def insert_box_data(conn, basic_box_data):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO box_score (gameId, team, player, name, result, loc, 
            MP, FG, FGA, FG%, 2P, 2PA, 2P%, 
            3P, 3PA, 3P%, FT, FTA, FT%, 
            ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS,
            TS%, eFG%, 3PAr, FTr, ORB%, DRB%, TRB%,
            AST%, STL%, BLK%, TOV%, USG%, ORtg, DRtg, BPM
            )
            VALUES (?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,
                    ?,?,?,?,?,?,?,?
                    )""", basic_box_data)
    conn.commit()

def insert_line_data(conn, line_data):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO line_score (gameId, date, team, 1, 2, T, result, loc, Pace, eFG%, TOV%, ORB%, FT/FGA, ORtg)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) """, line_data)
    conn.commit()

def fetch_box_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM box_score")
    return cursor.fetchall()

def fetch_line_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM line_score")
    return cursor.fetchall()

def fetch_box_data_by_player(conn, player_name):   
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM box_score WHERE name = ?", (player_name,))
    return cursor.fetchall()

def fetch_line_data_by_team(conn, team_name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM line_score WHERE team = ?", (team_name,))
    return cursor.fetchall()
