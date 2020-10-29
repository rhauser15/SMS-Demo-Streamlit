import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

#Plotting map data
map_data = pd.DataFrame(
    np.random.randn(516, 2) * [30,45] + [0, 0],
    columns=['lat', 'lon'])

gaus_data = pd.DataFrame(
    np.random.randn(10000000),
    columns=['lat'])
