#QuickBite - Database Layer
#ITE 260 Final Project

import sqlite3
from datetime import datetime
 
DB_NAME = "quickbite.db"
LOW_STOCK_THRESHOLD = 5
 
 
class Database:
    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.create_tables()