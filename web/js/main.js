
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

function reformatData(data) {
    newdata = []
    for (obj of data) {

        var datum = Date.parse(obj['SCRIPT_TIME']);
        newdata.push([
            datum, 
            obj['DS_TEMP']
        ]);
    }
    return newdata;
}

function createGraph(data) {
    console.log(data);

    var data = reformatData(data);

    console.log(data)

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

parseData(createGraph);
