var myIndex = 0;

function carousel() {
    var slides = document.getElementsByClassName("mySlides");

    // Is page par carousel slides nahi hain to kuch na karein.
    if (slides.length === 0) return;

    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    myIndex++;
    if (myIndex > slides.length) {
        myIndex = 1;
    }

    slides[myIndex - 1].style.display = "block";
    setTimeout(carousel, 5000);
}

function ha(element) {
    if (!element || !element.value) return;
    window.location.href =
        "/homeblood?bloodgroup=" + encodeURIComponent(element.value);
}

window.onscroll = function () {
    var nav = document.getElementById("nav");
    if (!nav) return;

    if (document.body.scrollTop > 150 ||
        document.documentElement.scrollTop > 150) {
        nav.style.position = "fixed";
        nav.style.top = "0";
        nav.style.left = "0";
        nav.style.backgroundColor = "rgba(82, 127, 99, 1.0)";
    } else {
        nav.style.position = "absolute";
        nav.style.top = "150px";
        nav.style.left = "0";
        nav.style.backgroundColor = "rgba(82, 127, 99, 0.5)";
    }
};

function myMap() {
    var mapElement = document.getElementById("map");
    if (!mapElement || !window.google || !google.maps) return;

    var mapOptions = {
        center: new google.maps.LatLng(16.247496, 80.408831),
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.HYBRID
    };

    new google.maps.Map(mapElement, mapOptions);
}

function showUser(str) {
    if (!str) {
        var hint = document.getElementById("txtHint");
        if (hint) hint.innerHTML = "";
        return;
    }

    // Yeh purana function getuser.php maangta hai.
    // Flask app mein ise chalane ke liye Flask route banana hoga.
    var request = new XMLHttpRequest();

    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            var hint = document.getElementById("txtHint");
            if (hint) hint.innerHTML = this.responseText;
        }
    };

    request.open("GET", "/getuser?q=" + encodeURIComponent(str), true);
    request.send();
}