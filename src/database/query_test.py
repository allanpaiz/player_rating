from src.database.database import *


# Create a connection to the database
database_file = "player_rating.db"
connection = create_connection(database_file)

# Test the query
box_score = fetch_box_data(connection)
print("Box Scores: ", box_score)

# Close the connection
connection.close()