import pandas as pd
from flask import Flask

from data import data

app = Flask(__name__)
number_stations = data.number_stations

@app.route('/')
def index():
    df = pd.DataFrame(number_stations)
    print(df)
    return df.to_json()
