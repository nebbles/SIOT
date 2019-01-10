# SIOT

Coursework for Design Engineering Sensing & Internet of Things

# Contents

## Coursework 1 - Sensing

The `data_collection/` directory contains all scripts and data backups used during part 1 of the coursework. In addition to this, the `ddns/` directory stores the DDNS specific script for the Rasberry Pi.

**Note** the `Data_Analysis.ipynb` file contains all the Python data analytics for both basic and cross correlation.

### File descriptions

| **Data_Analysis.ipynb** Analytics of collected data for basic and cross correlation
| **database_merge.py**   Utility script for analysing any gaps in the data
| **gsheet.py**           Module for interfacing with Google Sheets API
| **requirements.txt**    Requirements file for Python libraries; install with `pip install -r requirements.txt`
| **stocks.csv**          Raw data backup collected from Alpha Vantage
| **stocks.py**           Data collection script for fetching from Alpha Vantage
| **utils.py**            Utility module for extra script functions
| **weather.csv**         Raw data backup collected from Dark Sky
| **weather.py**          Data collection script for fetching from Dark Sky
| 

**Note** the script files will not run without the API keys and credentials files. These have not been committed to GitHub.

## Cousework 2 - Internet of Things

The `web/` directory contains all files required for the interface.

`cd` to that directory and start up a webserver `python -m SimpleHTTPServer 8000`

Then go to http://127.0.0.1:8000/web/index.html

or http://127.0.0.1:8000/index.html

depending on your starting directory.

# References

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.
