const {app, BrowserWindow} = require('electron')
const url = require('url')
const path = require('path')
const chart = require('chartjs')

let win

function createWindow() {
    // Create a new browser window
    win = new BrowserWindow()
    // Load html into window
    win.loadFile('src/index.html');

    win.webContents.openDevTools()

    win.on('closed', () => {
        // Dereference window object when closed
        win = null
    })
}

// Listen for app to be ready
app.on('ready', createWindow)

app.on('window-all-closed', () => {
    // When all windows of the application are closed then shut down the app automatically
    app.quit()
})

app.on('activate', () => {
    if (win == null) {
        createWindow()
    }
})

function goChart() {
    var ctx = document.getElementById("chart1").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}