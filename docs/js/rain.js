function getLocation() {
    x = document.getElementById('geo')
    if (navigator.geolocation) {
        x.innerHTML = 'Trying to fetch your current location...'
        loc = navigator.geolocation.getCurrentPosition(showPosition, function () {
            x.innerHTML = "You've declined location sharing. This is needed for localised animations."
            document.getElementById('ani-control').setAttribute("style", "background-color: transparent; padding: 0;");
        });
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    lat = position.coords.latitude.toFixed(5);
    lon = position.coords.longitude.toFixed(5);
    x.innerHTML = "Location: " + lat + ", " + lon;
    // document.getElementById('ani-control').setAttribute("style", "background-color: #efefef;");
    document.getElementById('ani-control').setAttribute("style", "background-color: transparent; padding: 0;");
    url = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&APPID=3715b8bf474b3d5f1f556a20573c7619`
    // console.log(url)
    loadJSON(url, cb);
}

function cb(data) {
    console.log(data);
    x.innerHTML = "Location: " + lat + ", " + lon + "; current forecast status: " + data.weather[0].main;
    let groupNum = Math.floor(data.weather[0].id / 100);
    // console.log('Group num calculated as ', groupNum);
    // groupNum = 3; // for DEBUGGING
    let groups = [2, 3, 5]
    if (groups.includes(groupNum)) {
        toggle = document.getElementById('enableAni').checked = true;
    }
}

function preload() {
    getLocation()
}

class Drop {
    constructor() {
        this.initPosition = function() {
            this.x = random(width);
            this.y = random(-height, 0);
            this.z = random(0, 20);
            this.len = map(this.z, 0, 20, 10, 20);
            this.yspeed = map(this.z, 0, 20, 4, 10);
        }
        this.initPosition();
    }

    fall() {
        this.y = this.y + this.yspeed;
        this.yspeed = this.yspeed + 0.05;
        this.yspeed = map(this.z, 0, 20, 4, 10);

        if (this.y > height) {
            this.initPosition();
        }
    }

    show() {
        stroke(138, 43, 226, 50);
        line(this.x, this.y, this.x, this.y + 10)
    }
}

var drops;
var toggle;

function setup() {
    canvas = createCanvas(windowWidth, windowHeight);
    // canvas.style('position', 'fixed'); // broken - see https://github.com/processing/p5.js/issues/3447
    canvas.elt.style.position = 'fixed';
    canvas.style('top', '0');
    canvas.style('left', '0');
    canvas.style('z-index', '-1');

    drops = [];
    for (let i = 0; i < 500; i++) {
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
