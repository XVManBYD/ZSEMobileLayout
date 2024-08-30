const weekday_span = document.getElementById("weekday-span");
const weekdays = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"];

let days = document.querySelectorAll(".day");

// days[weekday].classList.toggle("shown");

weekday_span.innerText = weekdays[weekday];
function prev_day() {
    // days[weekday].classList.toggle("shown");
    if (weekday > 0) {
        weekday -= 1;
    }
    // days[weekday].classList.toggle("shown");
    r.style.setProperty("--day-move", `-${weekday * 100}vw`)
    weekday_span.innerText = weekdays[weekday];
}

function next_day() {
    // days[weekday].classList.toggle("shown");
    if (weekday < 4) {
        weekday += 1;
    }
    r.style.setProperty("--day-move", `-${weekday * 100}vw`)
    // days[weekday].classList.toggle("shown");
    weekday_span.innerText = weekdays[weekday];
}