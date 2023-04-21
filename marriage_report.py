"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""

import pandas as pd
import os
import sqlite3
from create_relationships import db_path

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (nam1, nam2, start_date) of married couples 
    """

    # TODO: Function body

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("select r.nam1, r.nam2, r.start_date from relationships r where r.relationship_type = 'spouse'")
    married_couples = cur.fetchall()
    con.close()
    return married_couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (nam1, nam2, start_date) of married couples
        csv_path (str): Path of CSV file
    """

    # TODO: Function body

    married_couples_df = pd.DataFrame(married_couples, columns=['Person 1', 'Person 2', 'Anniversary'])
    married_couples_df.to_csv(csv_path, index=True)
    return

if __name__ == '__main__':
   main()