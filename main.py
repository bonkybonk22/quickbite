#QuickBite - Canteen/Ordering System 
#ITE 260 Final Project
 import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
 
import database as db
 
NAVY, ORANGE, GOLD, BG = "#0f172a", "#ea7a2b", "#f6bf5f", "#f3f4f6"
STATUS_COLORS = {"Available": "#2e9e5b", "Low Stock": "#d62828", "Out of Stock": "#7f1d1d",
                 "Normal": "#444444", "High": "#2e9e5b"}
