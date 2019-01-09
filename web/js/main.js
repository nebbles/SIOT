
function parseData(createGraph) {
    Papa.parse("./data/weather.csv", {
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

function reformatData(data, time_label, data_label) {
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

function tempGraph(data) {
    Highcharts.chart('weather', {
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'USD to EUR exchange rate over time'
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            title: {
                text: 'Exchange rate'
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

function createGraph(data) {

    var data = reformatData(data, 'SCRIPT_TIME', 'DS_TEMP');
    tempGraph(data)


    
}

parseData(createGraph);
