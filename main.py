import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set display options for better readability
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Load data
df = pd.read_csv('OnlineRetail.csv', encoding='unicode_escape')  # Handle encoding issues

# Immediately preserve original
df_original = df.copy()