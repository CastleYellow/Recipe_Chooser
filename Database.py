import sqlite3

# Create and connect to the database
conn = sqlite3.connect('C:/Users/annar/OneDrive/App_Dev/Recipe_Chooser/data/recipes.db')

# Create a cursor
c = conn.cursor()

# Commit our command
conn.commit()

# Close our connection
conn.close()