console.log("Loading js ");

//for a tags show and hide
const btn = document.getElementById('back-button');
const BtnAlbum = document.getElementById('btnAlbum');
const BtnStories = document.getElementById('btnStories');
const BtnPictures = document.getElementById('btnPictures');

// for pages of image
const Album = document.getElementById('album');
const Stories = document.getElementById('stories');
const Pictures = document.getElementById('pictures');
const Pictures1 = document.getElementById('PICTURE');



BtnAlbum.addEventListener('click', function () {
    console.log("Album");
    Album.style.display = 'block';
    Stories.style.display = 'none';
    Pictures.style.display = 'none';
    btn.style.display = 'block';
    Pictures1.style.display = 'none';
});

BtnStories.addEventListener('click', function () {
    console.log("Stories");
    Album.style.display = 'none';
    Stories.style.display = 'block';
    Pictures.style.display = 'none';
    btn.style.display = 'block';
    Pictures1.style.display = 'none';
});

BtnPictures.addEventListener('click', function () {
    console.log("pictures");
    Album.style.display = 'none';
    Stories.style.display = 'none';
    Pictures.style.display = 'block';
    btn.style.display = 'block';
    Pictures1.style.display = 'none';
});

function goBack() {
    Album.style.display = 'none';
    Stories.style.display = 'none';
    Pictures.style.display = 'none';
    Pictures1.style.display = 'block';
    btn.style.display = 'none';
}

// for viewing the Image
const Image1 = document.getElementById('view-images1');
const Image2 = document.getElementById('view-images2');
const Image3 = document.getElementById('view-images3');
const Image4 = document.getElementById('view-images4');
const Image5 = document.getElementById('view-images5');
const Image6 = document.getElementById('view-images16');



// Get the button and image modal elements
const showImageButton1 = document.getElementById("show-image-button1");
const showImageButton2 = document.getElementById("show-image-button2");
const showImageButton3 = document.getElementById("show-image-button3");
const showImageButton4 = document.getElementById("show-image-button4");
const showImageButton5 = document.getElementById("show-image-button5");
const showImageButton6 = document.getElementById("show-image-button6");


const imageModal = document.querySelector(".image-modal");
const closeImageButton = document.getElementById("close-image-button");

// Add a click event to the "Show Image" button
showImageButton1.addEventListener("click", function () {
    console.log("Image 1 loaded successfully");
    Image1.style.display = "block";
});
showImageButton2.addEventListener("click", function () {
    console.log("Image 2 loaded successfully");
    imageModal.style.display = "block";
});
showImageButton3.addEventListener("click", function () {
    console.log("Image 3 loaded successfully");
    imageModal.style.display = "block";
});
showImageButton4.addEventListener("click", function () {
    console.log("Image 4 loaded successfully");
    imageModal.style.display = "block";
});
showImageButton5.addEventListener("click", function () {
    console.log("Image 5 loaded successfully");
    imageModal.style.display = "block";
});
showImageButton6.addEventListener("click", function () {
    console.log("Image 6 loaded successfully");
    imageModal.style.display = "block";
});

// Add a click event to the close button to hide the modal
closeImageButton.addEventListener("click", function () {
    console.log("Closed loaded successfully");
    imageModal.style.display = "none";
});
