import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tushare as ts
from WindPy import *
import datetime
import time
import math 
from statsmodels import regression, stats
import statsmodels.api as sm

matplotlib.rcParams["figure.figsize"] = (14, 6)


def show_time(label_string):
    t = time.time()
    st = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S:%f")
    print(label_string + ": " + st)


def apidata_to_df(apidata):
    df = pd.DataFrame(apidata.Data, index=apidata.Fields, columns=apidata.Times)
    df = df.T
    return df


def to_industry_df(apidata):
    df1 = pd.DataFrame(apidata.Data[0], index=apidata.Times, columns=apidata.Fields)
    df1["INDUSTRY_SW"] = "银行"
    df2 = pd.DataFrame(apidata.Data[1], index=apidata.Times, columns=apidata.Fields)
    df2["INDUSTRY_SW"] = "非银金融"
    df = pd.concat([df1, df2], axis=0, join="outer")
    return df

