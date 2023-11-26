import sqlite3
import main


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

# Query the DB ans Return all the records
def show_all():
    # Connect to database and create a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM recipes")
    items = c.fetchall()
    for item in items:
        print(item)

    # Commit our Command
    conn.commit()
    # close our connection
    conn.close()

# Add a new record to the table
def add_one(recipe_name,ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6,recipe_book,recipe_link):
    # Connect to database and create a cursor
    conn = sqlite3.connect('C:/Users/annar/OneDrive/App_Dev/Recipe_Chooser/data/recipes.db')
    c = conn.cursor()

    recipe_to_add = (main.entry_recipe.get(),
                     main.entry_ingredient1.get(),
                     main.entry_ingredient2.get(),
                     main.entry_ingredient3.get(),
                     main.entry_ingredient4.get(),
                     main.entry_ingredient5.get(),
                     main.entry_ingredient6.get(),
                     main.entry_recipe_book.get(),
                     main.entry_recipe_link.get()
                     )

    # Add record to the table
    c.execute("INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?)", recipe_to_add)

    # Commit our Command
    conn.commit()
    # close our connection
    conn.close()

# Commit our command
conn.commit()

# Close our connection
conn.close()