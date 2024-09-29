document.getElementById("toggleButton").onmouseclick= function() {
    var daten = document.getElementById("daten");
    if (daten.style.display === "block") {
        daten.style.display = "none";
    }
    else {
        daten.style.display = "block";
    }
};
