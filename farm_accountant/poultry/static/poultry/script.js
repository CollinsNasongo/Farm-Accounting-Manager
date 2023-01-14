// Adding the active class to the navigation links
var navlinks_cont = document.getElementById("the_links");

// Get all buttons with class="btn" inside the container
var btns = navlinks_cont.getElementsByClassName("btn");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
