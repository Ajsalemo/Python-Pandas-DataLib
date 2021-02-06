import json

import pandas as pd
from flask import Flask, jsonify
from tabulate import tabulate

app = Flask(__name__)
number_stations = pd.read_csv("./data/number_stations.csv")

# Print tabular data
def tabular_output(i):
    print(tabulate(i, tablefmt='simple', headers=["ID", "Name", "Country", "Active Counterparts", "Inactive Counterparts", "Nickname", "Status", "Frequency", "Voice", "Emission Mode", "Location"], showindex='never'))  


# List all stations
@app.route('/')
def index():
    f = number_stations.to_json()
    return json.loads(f)


# List all stations under the column Name
@app.route('/station_names')
def station_names():
    # Filter the DataFrame columns to retrieve all stations under 'Name' column
    st_name = number_stations['Name']
    # If the DataFrame returns a response, convert the Series to a JSON string
    f = st_name.to_json()
    # Then convert the JSON string to a dict to properly format it when sending the response to the client
    return json.loads(f)


# Check for active stations
@app.route('/is_active_station')
def is_active_station():
    # Pass the parameter from the URL and check if it matches against an active station
    active_df = number_stations[number_stations['Status'] == 'Active']
    # Use tabulate to print the response to the terminal
    tabular_output(active_df)
    r = active_df.to_json()
    return json.loads(r)


# Check for inactive stations
@app.route('/is_inactive_station')
def is_inactive_station():
    # Pass the parameter from the URL and check if it matches against an inactive station
    inactive_df = number_stations[number_stations['Status'] == 'Inactive']
    # Use tabulate to print the response to the terminal
    tabular_output(inactive_df)
    r = inactive_df.to_json()
    return json.loads(r)


# Filter by station names
@app.route('/filter_station_names/<name>')
def filer_station_names(name):
    if name is None:
        return jsonify({ 'error': 'Station name cannot be blank' })
    # Pass the parameter from the URL and check if it matches against a known station name
    f_name = number_stations[number_stations['Name'] == name]
    # Use tabulate to print the response to the terminal
    tabular_output(f_name)
    # If the DataFrame returns empty, send an error back to the client
    if f_name.empty:
        return jsonify({ 'error': 'That station does not exist'})
    # If the DataFrame returns a response, convert the Series to a JSON string
    r = f_name.to_json()
    # Then convert the JSON string to a dict to properly format it when sending the response to the client
    return json.loads(r)


# Filter by station nicknames
@app.route('/filter_station_nickname/<nickname>')
def filer_station_nickname(nickname):
    if nickname is None:
        return jsonify({ 'error': 'Station nickname cannot be blank' })
    # Pass the parameter from the URL and check if it matches against a known station nickname
    f_nickname = number_stations[number_stations['Nickname'].str.contains(nickname)]
    # Use tabulate to print the response to the terminal
    tabular_output(f_nickname)
    # If the DataFrame returns empty, send an error back to the client
    if f_nickname.empty:
        return jsonify({ 'error': 'That station does not exist'})
    # If the DataFrame returns a response, convert the Series to a JSON string
    r = f_nickname.to_json()
    # Then convert the JSON string to a dict to properly format it when sending the response to the client
    return json.loads(r)


# Filter by station id's
@app.route('/filter_by_id/<id>')
def filter_by_id(id):
    if id is None:
        return jsonify({ 'error': 'ID cannot be empty' })
    # Pass the parameter from the URL and check if it matches against a known station id
    f_id = number_stations[number_stations['ID'] == id]
    # Use tabulate to print the response to the terminal
    tabular_output(f_id)
    # If the DataFrame returns empty, send an error back to the client
    if f_id.empty:
        return jsonify({ 'error': 'That ID does not exist'})
    # If the DataFrame returns a response, convert the Series to a JSON string
    r = f_id.to_json()
    # Then convert the JSON string to a dict to properly format it when sending the response to the client
    return json.loads(r)


# Filter by station locations
@app.route('/filter_by_location/<loc>')
def filter_by_location(loc):
    if loc is None:
        return jsonify({ 'error': 'Location cannot be empty' })
    # Pass the parameter from the URL and check if it matches against a known location - 'na=False' ignores any possibly empty values in the column to avoid throwing an error
    f_loc = number_stations[number_stations['Location'].str.contains(loc, na=False)]
    # Use tabulate to print the response to the terminal
    tabular_output(f_loc)
    # If the DataFrame returns empty, send an error back to the client
    if f_loc.empty:
        return jsonify({ 'error': 'That location does not exist'})
    # If the DataFrame returns a response, convert the Series to a JSON string
    r = f_loc.to_json()
    # Then convert the JSON string to a dict to properly format it when sending the response to the client
    return json.loads(r)


# Catch all HTTP 404's and return the below JSON message
@app.errorhandler(404)
def route_not_found(e):
    return jsonify({ "error": "The specified route does not exist" })
