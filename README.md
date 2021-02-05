# Python-Pandas-DataLib
Testing and experimenting with some simple Pandas functionality using Flask to serve the parsed data.
<br>
This repo uses Pandas to parse a .csv file containing Number Station information and offers endpoints to retrieve the data in the form of JSON responses through Flask.


### Routes <br>

<b>/</b> - List all stations <br>
<b>/station_names</b> - List all stations under the column Name <br>
<b>/is_active_station</b> - Check for active stations <br>
<b>/is_inactive_station</b> - Check for inactive stations <br>
<b>/filter_station_names/{name}</b> - Filter by station names <br>
<b>/filter_station_nickname/{nickname}</b> - Filter by station nicknames <br>
<b>/filter_by_id/{id}</b> - Filter by station id's <br>
<b>/filter_by_location/{loc}</b> - Filter by station locations

<br>

### Terminal <br>

In addition to routes, [Tabular](https://pypi.org/project/tabular/#:~:text=Tabular%20is%20a%20package%20of%20Python%20modules%20for,flexible%20and%20powerful%20than%20a%20native%20Python%20representation.) is used to output table data with Column names as keys to view the associated DataFrames, such as below: <br>

![Imgur](https://imgur.com/L13DfQW.png)
