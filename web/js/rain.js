// function makeRequest() {
//     url = "https://api.darksky.net/forecast/{apikey}/{loc[0]:},{loc[1]:}?exclude=minutely,hourly,daily&units=si"
//     var request = new XMLHttpRequest();
//     request.open('GET', url, true);
//     request.onload = function () {
//         var data = JSON.parse(this.response);
//         if (request.status >= 200 && request.status < 400) {
//             console.log(data)
//         } else {
//             console.log('There was an error with the API request.');
//         }
//     }
//     request.send();
// }
function showPosition(position) {
    lat = position.coords.latitude.toFixed(5);
    lon = position.coords.longitude.toFixed(5);
    x.innerHTML = "Location: " + lat + ", " + lon;
    document.getElementById('ani-control').setAttribute("style", "background-color: #efefef;");
    makeRequest([lat,lon]);
}

function getLocation() {
    x = document.getElementById('geo')
    if (navigator.geolocation) {
        x.innerHTML = 'Trying to fetch your current location...'
        loc = navigator.geolocation.getCurrentPosition(showPosition, function () {
            x.innerHTML = "You've declined location sharing. This is needed for localised animations."
            x.setAttribute("style", "text-align: left; font-size: 8pt;")
            document.getElementById('ani-control').setAttribute("style", "background-color: transparent; padding: 0;");
        });
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

getLocation()

class Drop {
    constructor() {
        this.x = random(width);
        this.y = random(-height, 0);
        this.z = random(0, 20);
        this.len = map(this.z, 0, 20, 10, 20);
        this.yspeed = map(this.z, 0, 20, 4, 10);
    }

    fall() {
        this.y = this.y + this.yspeed;
        this.yspeed = this.yspeed + 0.05;

        if (this.y > height) {
            this.y = random(-200, -100);
            this.yspeed = map(this.z, 0, 20, 4, 10);
        }
    }

    show() {
        stroke(138, 43, 226, 50);
        line(this.x, this.y, this.x, this.y+10)
    }
}

var drops;
var toggle;

function setup() {
    canvas = createCanvas(windowWidth, windowHeight);
    canvas.style('z-index', '-1');

    drops = [];
    for (let i=0; i < 500; i++) {
        drops.push(new Drop());
    }
}

function draw() {
    toggle = document.getElementById('enableAni').checked; // TODO
    background(255);
    if (toggle) {
        for (drop of drops) {
            drop.fall()
            drop.show()
        }
    }
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}

