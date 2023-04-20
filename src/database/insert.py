import pandas as pd
from .database import *

# Read in the csv file
box_csv = 'data/priv/test1/box.csv'
box_df = pd.read_csv(box_csv)
box_data = box_df.values.tolist()

# Read in the csv file
line_csv = 'data/priv/test1/line.csv'
line_df = pd.read_csv(line_csv)
line_data = line_df.values.tolist()

# Create a connection to the database
database_file = "player_rating.db" # Name of the database file
connection = create_connection(database_file)   # Creates a connection to the database

# Create the tables
create_box_table(connection)
create_line_table(connection)

# Insert the data
for box in box_data:
    insert_box_data(connection, box)

for line in line_data:
    insert_line_data(connection, line)

# Close the connection
connection.close()