
function parseData(path, createGraph) {
    Papa.parse(path, {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            createGraph(results.data)
        },
        error: function(err) {
            console.log(err)
        }
    })
}

function reformatTimeData(data, time_label, data_label) {
    var newdata = [];
    for (obj of data) {
        let dto = obj[time_label];
        if (dto != null) {
            // parse the date into a list
            let dtl = dto.split(/[^0-9]/);
            // store the date as a new Date object
            let date = new Date(dtl[0], dtl[1]-1, dtl[2], dtl[3], dtl[4], dtl[5])
            // push desired data to a processed list  
            newdata.push([
                date.valueOf(), 
                obj[data_label]
            ]);
        }
    }
    return newdata;
}

function reformatData(data, label1, label2) {
    let newdata = [];
    for (obj of data) {
        newdata.push(obj[label2]);
    }
    return newdata;
}

function temperatureGraph(target, data) {
    Highcharts.chart(target, {
        chart: {
            zoomType: 'x'
        },
        credits: {
            enabled: false
        },
        title: {
            text: ''
        },
        subtitle: {
            text: 'Temperature (°C) over time'
        },
        xAxis: {
            type: 'datetime',
            tickInterval: 1 * 24 * 3600 * 1000,
            tickWidth: 1,
            gridLineWidth: 1
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series:{color:Highcharts.getOptions().colors[5]},
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[5]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[5]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: [{
            type: 'area',
            name: 'Temperature',
            data: data
        }]
    });
}

function humidityGraph(target, data) {
    Highcharts.chart(target, {
        chart: {
            zoomType: 'x'
        },
        credits: {
            enabled: false
        },
        title: {
            text: ''
        },
        subtitle: {
            text: 'Humidity (%) over time'
        },
        xAxis: {
            type: 'datetime',
            tickInterval: 1 * 24 * 3600 * 1000,
            tickWidth: 1,
            gridLineWidth: 1
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: [{
            type: 'area',
            name: 'USD to EUR',
            data: data
        }]
    });
}

function pressureGraph(target, data) {
    Highcharts.chart(target, {
        chart: {
            zoomType: 'x'
        },
        credits: {
            enabled: false
        },
        title: {
            text: ''
        },
        subtitle: {
            text: 'Pressure (hPa) over time'
        },
        xAxis: {
            type: 'datetime',
            tickInterval: 1 * 24 * 3600 * 1000,
            tickWidth: 1,
            gridLineWidth: 1
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                color: Highcharts.getOptions().colors[2]
            },
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[2]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[2]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: [{
            type: 'area',
            name: 'USD to EUR',
            data: data
        }]
    });
}

function forexGraph(target, data) {
    Highcharts.chart(target, {
        chart: {
            zoomType: 'x'
        },
        credits: {
            enabled: false
        },
        title: {
            text: ''
        },
        subtitle: {
            text: 'GBP to USD exchange rate over time'
        },
        xAxis: {
            type: 'datetime',
            tickInterval: 1 * 24 * 3600 * 1000,
            tickWidth: 1,
            gridLineWidth: 1
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                color: Highcharts.getOptions().colors[1]
            },
            area: {
                fillColor: {
                    linearGradient: {
                        x1: 0,
                        y1: 0,
                        x2: 0,
                        y2: 1
                    },
                    stops: [
                        [0, Highcharts.getOptions().colors[1]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[1]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: [{
            type: 'area',
            name: 'USD to EUR',
            data: data
        }]
    });
}

function normTrendsGraph(data) {
    var temp = reformatTimeData(data, 'TIME', 'TEMPERATURE');
    var humi = reformatTimeData(data, 'TIME', 'HUMIDITY');
    var pres = reformatTimeData(data, 'TIME', 'PRESSURE');
    var forx = reformatTimeData(data, 'TIME', 'FOREX');
    Highcharts.chart('trends', {
        chart: {
            zoomType: 'x'
        },
        credits: {
            enabled: false
        },
        title: {
            text: ''
        },
        subtitle: {
            text: 'Normalised Data Trends over Time'
        },
        xAxis: {
            type: 'datetime',
            tickInterval: 1 * 24 * 3600 * 1000,
            tickWidth: 1,
            gridLineWidth: 0
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        legend: {
            enabled: true
        },

        series: [{
                type: 'line',
                name: 'Temperature',
                data: temp
            },{
                type: 'line',
                name: 'Humidity',
                data: humi
            },{
                type: 'line',
                name: 'Pressure',
                data: pres
            }, {
                type: 'line',
                name: 'GBP/USD',
                data: forx
            }
        ]
    });
}

function correlationGraph(data) {
    var temp = reformatData(data, 'INDEX', 'TEMPERATURE');
    var humi = reformatData(data, 'INDEX', 'HUMIDITY');
    var pres = reformatData(data, 'INDEX', 'PRESSURE');
    Highcharts.chart('correlation', {
        chart: {
            zoomType: 'x'
        },
        credits: {
            enabled: false
        },
        title: {
            text: ''
        },
        subtitle: {
            text: 'Weather series correlated with Exchange Rate at increasing lags'
        },
        xAxis: {
            title: {
                text: 'Lag of Exchange from Weather (in hours)'
            },
            tickInterval: 6,
            tickWidth: 1,
            gridLineWidth: 1,
            labels: {
                formatter: function () {
                    return this.value/6;
                }
            }
        },
        yAxis: {
            title: {
                text: 'Pearson R² Value'
            }
        },
        legend: {
            enabled: true
        },

        series: [{
                type: 'line',
                name: 'Temperature',
                data: temp
            },
            {
                type: 'line',
                name: 'Humidity',
                data: humi
            },
            {
                type: 'line',
                name: 'Pressure',
                data: pres
            }
        ]
    });
}

function createBasicGraphs(data) {

    var temp = reformatTimeData(data, 'TIME', 'TEMPERATURE');
    var humi = reformatTimeData(data, 'TIME', 'HUMIDITY');
    var pres = reformatTimeData(data, 'TIME', 'PRESSURE');
    var forx = reformatTimeData(data, 'TIME', 'FOREX');
    
    temperatureGraph('temperature', temp)
    humidityGraph('humidity', humi)
    pressureGraph('pressure', pres)
    forexGraph('forex', forx)
}

function showPosition(position) {
    lat = position.coords.latitude.toFixed(5);
    lon = position.coords.longitude.toFixed(5);
    x.innerHTML = "Location: " + lat + ", " + lon;
    document.getElementById('ani-control').setAttribute("style", "background-color: #efefef;");
}

function getLocation() {
    x = document.getElementById('geo')
    if (navigator.geolocation) {
        x.innerHTML = 'Trying to fetch your current location...'
        loc = navigator.geolocation.getCurrentPosition(showPosition, function() {
            x.innerHTML = "You've declined location sharing. This is needed for localised animations."
            x.setAttribute("style", "text-align: left; font-size: 8pt;")
            document.getElementById('ani-control').setAttribute("style", "background-color: transparent; padding: 0;");
        });
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

document.getElementById('chart-tip').innerHTML = document.ontouchstart === undefined ?
    'Tip: Click and drag in the plot area to zoom in!' : 'Tip: Pinch the chart to zoom in!'

parseData("./data/data_all.csv", createBasicGraphs);
parseData("./data/data_trends_norm.csv", normTrendsGraph);
parseData("./data/data_correlations.csv", correlationGraph);

getLocation()
