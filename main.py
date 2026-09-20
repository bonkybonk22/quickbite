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
        notebook.pack(fill="both", expand=True)
 
        self.menu_tab = ttk.Frame(notebook)
        self.order_tab = ttk.Frame(notebook)
        self.sales_tab = ttk.Frame(notebook)
        self.stock_tab = ttk.Frame(notebook)
 
        notebook.add(self.menu_tab, text="Menu")
        notebook.add(self.order_tab, text="Place Order")
        notebook.add(self.sales_tab, text="Daily Sales")
        notebook.add(self.stock_tab, text="Low Stock")
 
        self.build_menu_tab()
        self.build_order_tab()
        self.build_sales_tab()
        self.build_stock_tab()