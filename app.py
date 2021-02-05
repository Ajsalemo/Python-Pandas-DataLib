import json

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
number_stations = pd.read_csv("./data/number_stations.csv")


@app.route('/')
def index():
    df = pd.DataFrame(number_stations)
    print(df)
    f = df.to_json()
    return json.loads(f)


@app.route('/station_names')
def station_names():
    st_df = pd.DataFrame(number_stations)
    # Filter the DataFrame columns to retrieve all stations under 'Number Station name'
    st_name = st_df['Name']
    # If the DataFrame returns a response, convert the Series to a JSON string
    f = st_name.to_json()
    # Then convert the JSON string to a dict to properly format it when sending the response to the client
    return json.loads(f)


@app.route('/is_active_station')
def is_active_station():
    # Pass the parameter from the URL and check if it matches against an active station
    active_df = number_stations[number_stations['Status'] == 'Active']
    r = active_df.to_json()
    return json.loads(r)


@app.route('/is_inactive_station')
def is_inactive_station():
    inactive_df = number_stations[number_stations['Status'] == 'Inactive']
    r = inactive_df.to_json()
    return json.loads(r)


@app.route('/filter_station_names/<name>')
def filer_station_names(name):
    if name is None:
        return jsonify({ 'error': 'Station name cannot be blank' })
    # Pass the parameter from the URL and check if it matches against a known station name
    f_name = number_stations[number_stations['Name'] == name]
    # If the DataFrame returns empty, send an error back to the client
    if f_name.empty:
        return jsonify({ 'error': 'That station does not exist'})
    # If the DataFrame returns a response, convert the Series to a JSON string
    r = f_name.to_json()
    # Then convert the JSON string to a dict to properly format it when sending the response to the client
    return json.loads(r)
