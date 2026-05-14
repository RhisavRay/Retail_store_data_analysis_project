import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Stage 1: Data Acquisition & Environment Setup



# Set display options for better readability
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Load data
df = pd.read_csv('OnlineRetail.csv', encoding='unicode_escape')  # Handle encoding issues

"""
What unicode_escape Does

When you set encoding='unicode_escape', you are essentially giving pandas a workaround to bypass that crash.

How it works: It tells pandas, "If you find a weird, non-standard byte that you can't read, don't crash. Just escape it and print its raw
unicode value."

The Result: The file will successfully load into your DataFrame without throwing an error.
"""

# Immediately preserve original
df_original = df.copy()



# Stage 2: Initial Data Inspection



