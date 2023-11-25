import sqlite3

# Create and connect to the database
conn = sqlite3.connect('C:/Users/annar/OneDrive/App_Dev/Recipe_Chooser/data/recipes.db')

# Create a cursor
c = conn.cursor()

# Create a table
# c.execute(""" CREATE TABLE customers (
#         recipe_name text,
#         ingredient_1 text,
#         ingredient_2 text,
#         ingredient_3 text,
#         ingredient_4 text,
#         ingredient_5 text,
#         ingredient_6 text,
#         recipe_book text,
#         recipe_link blob
#     )""")



# Commit our command
conn.commit()

# Close our connection
conn.close()