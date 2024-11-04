#Hypothesis: When a hurricane is projected to hit Florida, insurance companies based in florida stock price, 
#energy companies based in Florida stock price, and cruise line companies based in Florida stock price all go down on the short-term 
#and go back up in the long-term depending on the severity of the Hurricane. I am looking to project these Hurricanes at least a week
#before they hit and their severity (if they will be a direct hit or only hit a certain part)

# Data Collection
import yfinance as yf
import requests
import json

# Data Manipulation and Analysis
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# GUI and Dashboard Creation
import tkinter as tk
import dash
from dash import dcc, html

# Time and Scheduling
from datetime import datetime, timedelta
import time
import schedule

# Machine Learning and Statistical Analysis (optional)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import statsmodels.api as sm



