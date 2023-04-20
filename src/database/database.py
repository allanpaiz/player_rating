import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def create_box_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS box_score (
                gameId TEXT NOT NULL, team TEXT NOT NULL, player TEXT NOT NULL, name TEXT NOT NULL, result REAL NOT NULL, loca TEXT NOT NULL,
                MinP INTEGER NOT NULL, FGMade INTEGER NOT NULL, FGAtt INTEGER NOT NULL, FGPer REAL, twoPMade INTEGER NOT NULL, twoPAtt INTEGER NOT NULL, twoPPer REAL,
                threePMade INTEGER NOT NULL, threePAtt INTEGER NOT NULL, threePPer REAL, FTMade INTEGER NOT NULL, FTAtt INTEGER NOT NULL, FTPer REAL,
                OffReB INTEGER NOT NULL, DefReB INTEGER NOT NULL, TotReB INTEGER NOT NULL, ASST INTEGER NOT NULL, Steal INTEGER NOT NULL, Block INTEGER NOT NULL, TurnOver INTEGER NOT NULL, PersFoul INTEGER NOT NULL, PTSMade INTEGER NOT NULL,
                TS_percent REAL, eFG_percent REAL, threePAr REAL, aFTr REALL, ORB_percent REAL, DRB_percent REAL, TRB_percent REAL,
                AST_percent REAL, STL_percent REAL, BLK_percent REAL, TOV_percent REAL, USG_percent REAL, ORtg REAL, DRtg REAL,BPM REAL
)""")

def create_line_table(conn):
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS line_score (
                gameId TEXT NOT NULL, date TEXT NOT NULL, team TEXT NOT NULL, half1 TEXT NOT NULL, half2 TEXT NOT NULL, gameTotal TEXT NOT NULL, result TEXT NOT NULL, loca TEXT NOT NULL,
                Pace TEXT NOT NULL, eFG_percent TEXT NOT NULL, TOV_percent TEXT NOT NULL, ORB_percent TEXT NOT NULL, FT_FGA TEXT NOT NULL, ORtg TEXT NOT NULL
)""")                 
    
def insert_box_data(conn, basic_box_data):
    cursor = conn.cursor()
    cursor.executemany("""INSERT INTO box_score (gameId, team, player, name, result, loca, 
                MinP, FGMade, FGAtt, FGPer, twoPMade, twoPAtt, twoPPer,
                threePMade, threePAtt, threePPer, FTMade, FTAtt, FTPer,
                OffReB, DefReB, TotReB, ASST, Steal, Block, TurnOver, PersFoul, PTSMade,
                TS_percent, eFG_percent, threePAr, aFTr, ORB_percent, DRB_percent, TRB_percent,
                AST_percent, STL_percent, BLK_percent, TOV_percent, USG_percent, ORtg, DRtg, BPM
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", basic_box_data)
    conn.commit()

def insert_line_data(conn, line_data):
    cursor = conn.cursor()
    cursor.executemany("""INSERT INTO line_score (
                gameId, date, team, half1, half2, gameTotal, result, loca,
                Pace, eFG_percent, TOV_percent, ORB_percent, FT_FGA, ORtg
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", line_data)
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

############################################################################################################
# Eventually create its own file to run this code
# from database.database import * # I cannot get this part to work for some reason

# box_csv = 'data/box.csv'
# box_df = pd.read_csv(box_csv)
# box_data = box_df.values.tolist()
# line_csv = 'data/line.csv'
# line_df = pd.read_csv(line_csv)
# line_data = line_df.values.tolist()

# database_file = "player_rating.db"

# with create_connection(database_file) as connection:
#     create_box_table(connection)
#     create_line_table(connection)
#     insert_box_data(connection, box_data)
#     insert_line_data(connection, line_data)


############################################################################################################
# Test the database
# Will be own file, for querying the database

# # Create a connection to the database
# database_file = "player_rating.db"
# connection = create_connection(database_file)

# # Test the query
# player = fetch_box_data_by_player(connection, 'Brandon Miller')
# print(player)

# # Close the connection
# connection.close()


############################################################################################################
# Test Plot IT WORKS!!!!
# def fetch_team_results_and_rebounds(conn):
#     cursor = conn.cursor()
#     cursor.execute("""
#         SELECT team, result, SUM(TotReB) as total_rebounds, COUNT(*) as games
#         FROM box_score
#         GROUP BY team, result
#     """)
#     return cursor.fetchall()

# conn = sqlite3.connect("player_rating.db")
# data = fetch_team_results_and_rebounds(conn)
# conn.close()

# df = pd.DataFrame(data, columns=["team", "result", "total_rebounds", "games"])
# df["average_rebounds"] = df["total_rebounds"] / df["games"]

# plt.figure(figsize=(12, 6))
# plt.scatter(df["average_rebounds"], df["result"], c=df["result"].apply(lambda x: "green" if x == "W" else "red"), alpha=0.5)
# plt.xlabel("Average Rebounds per Game")
# plt.ylabel("Game Result (Win/Loss)")
# plt.title("Correlation between Wins/Losses and Rebounds per Game")
# plt.show()