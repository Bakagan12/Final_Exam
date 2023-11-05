console.log("js loaded !!!!......")

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

const homeLink = document.getElementById("homeLink");
const albumsLink = document.getElementById("albumsLink");

homeLink.addEventListener("click", function () {
  homeLink.classList.add("bgColor");
  albumsLink.classList.remove("bgColor");
});

albumsLink.addEventListener("click", function () {
  albumsLink.classList.add("bgColor");
  homeLink.classList.remove("bgColor");
});