console.log("js loaded !!!!......")

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

const btnPhoto = document.getElementById('showImages');
const btnPhoto1 = document.getElementById('showImages1');
const btnPhoto2 = document.getElementById('showImages2');

const showPhoto = document.getElementById('hidden-div');
const showPhoto1 = document.getElementById('hidden1-div');

const backButton = document.getElementById('backButton');

const hidePhoto = document.getElementById('container_flex');

btnPhoto.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'block'; // Show the hidden div
  hidePhoto.style.display = 'none';
});
btnPhoto1.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'block'; // Show the hidden div
  hidePhoto.style.display = 'none';
});
btnPhoto2.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'block'; // Show the hidden div
  hidePhoto.style.display = 'none';
});
backButton.addEventListener('click', function () {
  // Add code to show the hidden div and hide the button, e.g., using CSS classes or inline style changes
  showPhoto.style.display = 'none';
  showPhoto.style.display = 'none';
  hidePhoto.style.display = 'block';
  hidePhoto.classList.add("container_flex");
});