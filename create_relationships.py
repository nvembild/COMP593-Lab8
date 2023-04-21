"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""

import sqlite3
import os
from faker import Faker
import random

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute('''Drop table if exist relationships''')
    cur.execute('''Create table relationships
                   (id integer primary key autoincrement,
                    name1 txt not nullL,
                    name2 txt not null,
                    start_date txt not null,
                    relationship_type txt not null)''')
    
    con.commit()
    con.close()


def populate_relationships_table():
    """Adds 100 random relationships to the DB"""

    fake = Faker()

    relationship_types = ['family', 
                          'workmates', 
                          'spouse', 
                          'friends']
    
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()

        for i in range(100):
            nam1 = fake.name()
            nam2 = fake.name()
            start_date = fake.date_between(start_date='-10y', end_date='today')
            relationship_type = random.choice(relationship_types)

            cur.execute('''Insert into relationships (nam1, nam2, start_date, relationship_type)
                            values (?, ?, ?, ?)''', (nam1, nam2, start_date, relationship_type))
        con.commit()

if __name__ == '_main_':
   main()