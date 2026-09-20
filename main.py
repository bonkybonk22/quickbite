#QuickBite - Canteen/Ordering System 
#ITE 260 Final Project
 
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
 
from database import Database, LOW_STOCK_THRESHOLD

 
class QuickBiteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db = Database()
 
        self.title("QuickBite - Canteen Ordering System")
        self.geometry("900x600")
 
        notebook = ttk.Notebook(self)
        