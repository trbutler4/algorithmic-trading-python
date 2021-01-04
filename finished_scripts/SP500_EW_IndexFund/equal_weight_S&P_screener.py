# equal weight S&P 500 screener script

# library imports
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math


# import list of stocks
stocks = pd.read_csv('sp_500_stocks.csv')

# sandbox API token (random stock data)
IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'

#


