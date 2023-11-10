 window.onload = function() {
  // Variables for Elements
  let image = document.querySelector(".preview");
  let total = document.querySelector(".total");
  let totalcount = document.querySelector(".total-count");
  let imageInput = document.getElementById("image");
  let filelabel = document.querySelectorAll(".file-cta");
  let panorama = document.getElementById("panorama");
  let stitchbtn = document.getElementById("stitchbtn");
  let previewImage = document.querySelector(".preview");

  const MAX_WIDTH = 19200;
  const MAX_HEIGHT = 10800;
  const MIME_TYPE = "image/jpeg";
  const QUALITY = 0.6; //0.7 => 70% quality
  var fileinput = document.getElementById("panorama");
  var max_width = MAX_WIDTH;
  var max_height = MAX_HEIGHT;
  var preview = document.getElementById("root");
  var form = document.getElementById("root");
  previewImage.src = "static/background.png";


  const GIPHY_API_KEY = "yFFYGkuRU6aN8fLvvkMrYOAubuJu6nzT";

function get_random_gif(GIPHY_API_KEY) {
  let tag = "waiting";
  let url = `https://api.giphy.com/v1/gifs/random?api_key=${GIPHY_API_KEY}&tag=${tag}&rating=g`;
  fetch(url)
    .then(response => response.json())
    .then(content => {
      let image = document.querySelector(".preview");
      image.src = content.data.images.original.url;
    })
    .catch(err => {
      console.error(err);
    });
}




async function SendPanoramaImages() {
  let Images = document.querySelectorAll("#panoramaImages");


  /**
   * Send the resized images to server as JSON
   *  */

  let json = {};
  let ImagesArray = [];
  /**
   * Loop through the resized images and add them to the JSON Array
   */
  for (let i = 0; i < Images.length; i++) {
    ImagesArray.push({
      name: Images[i]["dataset"].filename,
      value: Images[i]["value"]
    });
    json = ImagesArray;
  }

  /**
   * Send the JSON Array to the server
   * */
  console.log(`Sending ${Images.length} images to server...`);

  axios
    .post("/api/stitch", JSON.stringify(json), {
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      }
    })
    .then(function(response) {
      console.log(response);


      // Enable & Disable Elements
      stitchbtn.style.display = "none";
      // Display the total stitching prog
      total.innerText =        "Stitching  Progress";
      total.style.display = "block";
      totalcount.innerHTML = response.data.total_objects;

      if (response.data.total_objects > 0) {
        totalcount.style.color = "red";
      } else {
        totalcount.style.color = "green";
      }

      // Replace the preview image with the stitched image
      image.src = response.data.image;

      // Enable the image input
      imageInput.disabled = false;
      panorama.disabled = false;
      filelabel[0].hidden = false;
      filelabel[1].hidden = false;
      filelabel[0].querySelectorAll("p")[0].innerText = "Choose Image";

      /**
       * Submit the stitched image to the server for detection
       */
    })
    .catch(function(error) {

      // If the response contains an error then display the error
      if  (error.response) {
        
        console.log(error.response.data);
        return false;
      }
      
    });
}


  document.getElementById("image").onchange = function() {
    document.getElementById("submit").classList.remove("disabled");
  };

  document.getElementById("submit").onclick = function() {
    document.getElementById("submit").classList.add("disabled");
  };
  // If the image is selected then display the name of the image
  imageInput.addEventListener("change", function() {
    let file = document.querySelectorAll("#image")[0].files[0];
    let reader = new FileReader();
    reader.addEventListener(
      "load",
      function() {
        //   document.querySelectorAll('#image')[0].parentElement.innerText=document.querySelectorAll('#image')[0].files[0].name
      },
      false
    );

    if (file) {
      reader.readAsDataURL(file);
      //            imageInput.disabled = true;
      filelabel[0].querySelectorAll("p")[0].innerText = "Processing";

      submitImage(file);
      image.src =
        "https://miro.medium.com/v2/resize:fit:1400/1*e_Loq49BI4WmN7o9ItTADg.gif";
    }
  });

  /**
     * Send the stitched image to the server for Stitching & Replace the preview image with the Wait GIF
     
     */
  stitchbtn.addEventListener("click", function() {
    SendPanoramaImages();
  });

  panorama.onchange = function(ev) {
    var files = ev.target.files; // FileList object
    // When the user selects 5 or more images, then send the images to the server
    if (files.length > 4) {
      panorama.disabled = true;

      filelabel[0].hidden = true;
      filelabel[1].hidden = true;
      stitchbtn.style.display = "block";

      /**
            * Send the resized images to server as JSON
            */

      if (files) {
        readfiles(files);
      }

      console.log("Sending images to server...");
    } else {
      alert("Please select 5 or more images");
      return false;
    }
  }

  /**
    Panorama
    */

  function submitImage(image) {
    let formData = new FormData();
    formData.append("image", image);
    axios
      .post("/api/detect", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          "Access-Control-Allow-Origin": "*",
          "Content-Disposition": "attachment; filename="
        }
      })
      .then(function(response) {
        console.log(response);
        let image = document.querySelector(".preview");
        image.src = response.data.image;
        totalcount.innerHTML = response.data.total_objects;
        // unhides the total count

        total.style.display = "block";
        //            imageInput.disabled = false;
        filelabel[0].querySelectorAll("p")[0].innerText = "Choose Image";
      })
      .catch(function(error) {
        console.log(error);
      });
  }

  /**
    Compress Image

    */

  function resizeMe(img) {
    var canvas = document.createElement("canvas");

    var width = img.width;
    var height = img.height;

    // calculate the width and height, constraining the proportions
    if (width > height) {
      if (width > MAX_WIDTH) {
        //height *= max_width / width;
        height = Math.round((height *= MAX_WIDTH / width));
        width = MAX_WIDTH;
      }
    } else {
      if (height > MAX_HEIGHT) {
        //width *= max_height / height;
        width = Math.round((width *= MAX_HEIGHT / height));
        height = MAX_HEIGHT;
      }
    }


    // resize the canvas and draw the image data into it
    canvas.width = width;
    canvas.height = height;
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0, width, height);
    let previewImage = document.querySelector(".preview");

    previewImage.appendChild(canvas); // do the actual resized preview

    return canvas.toDataURL("image/jpeg", 0.4); // get the data from canvas as 70% JPG (can be also PNG, etc.)
  }

  // Utility functions for demo purpose

  function displayInfo(label, file) {
    const p = document.createElement("p");
    p.innerText = `${label} - ${readableBytes(file.size)}`;
    document.getElementById("root").append(p);
  }

  function readableBytes(bytes) {
    const i = Math.floor(Math.log(bytes) / Math.log(1024)),
      sizes = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];

    return (bytes / Math.pow(1024, i)).toFixed(2) + " " + sizes[i];
  }

  function readfiles(files) {
    // remove the existing canvases and hidden inputs if user re-selects new pics
    var existinginputs = document.getElementsByName("images[]");
    var existingcanvases = document.getElementsByTagName("canvas");
    while (existinginputs.length > 0) {
      // it's a live list so removing the first element each time
      // DOMNode.prototype.remove = function() {this.parentNode.removeChild(this);}
      form.removeChild(existinginputs[0]);
      preview.removeChild(existingcanvases[0]);
    }

    for (var i = 0; i < files.length; i++) {
      processfile(files[i]); // process each file at once
    }
    fileinput.value = ""; //remove the original files from fileinput
    // TODO remove the previous hidden inputs if user selects other files
  }

  function processfile(file) {
    if (!/image/i.test(file.type)) {
      alert("File " + file.name + " is not an image.");
      return false;
    }
    // read and display the image into canvas
    var reader = new FileReader();
    reader.onload = function(event) {
      var img = new Image();
      img.onload = function() {
        if (file.size > 200000000) {
          alert("File " + file.name + " is too big.");
          return false;
        }

        var canvas = document.createElement("canvas");
        canvas.style.display = "none";
        canvas.width = MAX_WIDTH;
        canvas.height = MAX_HEIGHT;
        var ctx = canvas.getContext("2d");
        ctx.drawImage(img, 0, 0, MAX_WIDTH, MAX_HEIGHT);
        preview.appendChild(canvas); // do the actual resized preview

        /**
            * Create a hidden input with the resized data URL as value
            */

        var newinput = document.createElement("input");
        newinput.type = "hidden";
        newinput.id = "panoramaImages";
        newinput.name = "panoramaImages";
        newinput.value = canvas.toDataURL("image/jpeg", 0.7);
        newinput.className = "panoramaImages";
        newinput.setAttribute("data-filename", file.name); // get the value of "name" tag in HTML
        form.appendChild(newinput);
      };
      img.src = event.target.result;
    };
    reader.readAsDataURL(file);
  }



}