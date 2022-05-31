let currentMinute = 25;
let currentSecond = 00;
let countingDown = false;
let minutes = document.getElementById("minutes");
let seconds = document.getElementById("seconds");
let secondsCountDown, minutesCountDown;

minutes.innerHTML = styleNumber(currentMinute);
seconds.innerHTML = styleNumber(currentSecond);

let startButton = document.getElementById("start");
startButton.onclick = startTimer;

let stopButton = document.getElementById("stop");
stopButton.onclick = stopTimer;

let continueButton = document.getElementById("continue");
continueButton.onclick = continueTimer;

let breakButton = document.getElementById("break");
breakButton.onclick = startBreak;

function startTimer() {
    this.style.display = "none";
    stopButton.style.display = "flex";
    currentSecond = 59;
    seconds.innerHTML = styleNumber(currentSecond);
    currentMinute = 24;
    minutes.innerHTML = styleNumber(currentMinute);
    secondsCountDown = setInterval(function () {
        if (currentSecond == 0) {
            currentSecond = 59;
        } else {
            currentSecond -= 1;
        }
        seconds.innerHTML = styleNumber(currentSecond);
        if (currentMinute == 0 && currentSecond == 0) {
            clearInterval(secondsCountDown);
            clearInterval(minutesCountDown);
            stopButton.style.display = "none";
            breakButton.style.display = "flex";
            seconds.innerHTML = "00";
            minutes.innerHTML = "05";
        }
    },1000);
    minutesCountDown = setInterval(function () {
        if (currentMinute == 0) {
            currentMinute = 1;
        } else {
            currentMinute -= 1;
        }
        minutes.innerHTML = styleNumber(currentMinute);
    },60000);
}

function stopTimer() {
    this.style.display = "none";
    continueButton.style.display = "flex";
    clearInterval(secondsCountDown);
    clearInterval(minutesCountDown);
}

function continueTimer() {
    this.style.display = "none";
    stopButton.style.display = "flex";
    secondsCountDown = setInterval(function () {
        if (currentSecond == 0) {
            currentSecond = 59;
        } else {
            currentSecond -= 1;
        }
        seconds.innerHTML = styleNumber(currentSecond);
        if (currentMinute == 0 && currentSecond == 0) {
            clearInterval(secondsCountDown);
            clearInterval(minutesCountDown);
            stopButton.style.display = "none";
            breakButton.style.display = "flex";
            seconds.innerHTML = "00";
            minutes.innerHTML = "05";
        }
    },1000);
    minutesCountDown = setInterval(function () {
        if (currentMinute == 0) {
            currentMinute = 1;
        } else {
            currentMinute -= 1;
        }
        minutes.innerHTML = styleNumber(currentMinute);
    },60000);
}

function styleNumber(num) {
    if (num < 10) {
        return "0" + num;
    } else {
        return String(num);
    }
}

function startBreak() {
    this.style.display = "none";
    currentSecond = 59;
    currentMinute = 4;
    seconds.innerHTML = styleNumber(currentSecond);
    minutes.innerHTML = styleNumber(currentMinute);
    secondsCountDown = setInterval(function () {
        if (currentSecond == 0) {
            currentSecond = 59;
        } else {
            currentSecond -= 1;
        }
        seconds.innerHTML = styleNumber(currentSecond);
        if (currentMinute == 0 && currentSecond == 0) {
            clearInterval(secondsCountDown);
            clearInterval(minutesCountDown);
            stopButton.style.display = "none";
            startButton.style.display = "flex";
        }
    },1000);
    minutesCountDown = setInterval(function () {
        if (currentMinute == 0) {
            currentMinute = 1;
        } else {
            currentMinute -= 1;
        }
        minutes.innerHTML = styleNumber(currentMinute);
    },60000);
}