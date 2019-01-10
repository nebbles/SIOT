<p align="center">
	<sub>Imperial College London<br>Dyson School of Design Engineering</sub>
</p>
<h1 align="center">
	  Sensing & IoT
</h1>

<h4 align="center">
  <a href="http://nebbles.github.io/siot">View the Project Web Interface</a>
  <br><br>
	<a href="https://github.com/nebbles/SIOT/blob/master/Report.pdf">Read the report</a>
  <br>
  <br>
</h4>

## 1. Sensing (Data Collection)

The `data_collection/` directory contains all scripts and data backups used during part 1 of the coursework. In addition to this, the `ddns/` directory stores the DDNS specific script for the Rasberry Pi.

**Note**: the `Data_Analysis.ipynb` file contains all the Python data analytics for both basic and cross correlation.

<p align="center">
	<a href="https://github.com/nebbles/SIOT/blob/master/data_collection/Data_Analysis.ipynb" target="_blank">View the Jupyter Notebook</a>
</p>


### File descriptions

> **Data_Analysis.ipynb** Analytics of collected data for basic and cross correlation  
> **database_merge.py**   Utility script for analysing any gaps in the data  
> **gsheet.py**           Module for interfacing with Google Sheets API  
> **requirements.txt**    Requirements file for Python libraries; install with `pip install -r requirements.txt`  
> **stocks.csv**          Raw data backup collected from Alpha Vantage  
> **stocks.py**           Data collection script for fetching from Alpha Vantage  
> **utils.py**            Utility module for extra script functions  
> **weather.csv**         Raw data backup collected from Dark Sky  
> **weather.py**          Data collection script for fetching from Dark Sky  

**Note**: the script files will not run without the API keys and credentials files. These have not been committed to GitHub.

## 2. Internet of Things (Interface)

The `docs/` directory contains all files related to the interface and data visualisation. To view the interface, you can see it at http://nebbles.github.io/siot where it is hosted by GitHub Pages.

Alternatively, you can view locally, which requires a local webserver. If you have Python installed this is a simple command. From the resository-level directory, run the following command:

```
$ python -m SimpleHTTPServer 8000
```

Then go to http://127.0.0.1:8000/docs/index.html

## References

This project was powered by:

- [Dark Sky](https://darksky.net/dev)
- [Alpha Vantage](https://www.alphavantage.co/)
- [Highcharts](https://www.highcharts.com/)

## License

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.
