

function detect(){
    let image = document.querySelector(".preview");
    let total = document.querySelector(".total");
    let totalcount = document.querySelector(".total-count");
    let imageInput = document.getElementById("image");
    let filelabel = document.querySelectorAll(".file-cta");
    let panorama = document.getElementById("panorama");
    let stitchbtn = document.getElementById("stitchbtn");
    let previewImage = document.querySelector(".preview");
    let imagessection = document.querySelector(".images-section"); 
    let panoramaSection = document.querySelector(".panorama-section");
      let detectBTN = document.getElementById('detectbtn')
    let panoramaimg = document.querySelector(".panorama-image");  


    stitchbtn.addEventListener("click", stitch);
    detectBTN.addEventListener("click", detect);

    console.log("Detecting");

    detectBTN.style = "display:none";
    panoramaimg.src = 'https://miro.medium.com/v2/resize:fit:1400/1*e_Loq49BI4WmN7o9ItTADg.gif'
    panoramaimg.style = "width: 100%; height: 100%;"
    

    axios.get('/detect').then(function(response){
        console.log(response.data);
        let img = response.data.image;
        console.log(`Image: ${img}`)
        console.log(`total_objects: ${response.data.total_objects}`)
        console.log(`labels: ${response.data.labels}`)
        // Replace the image with a random gif
        
        panoramaimg.src = img;
        /**
         * Display the total number of objects detected
         */
        let panoramaSection = document.querySelector(".panorama-section").querySelector("h1");
        // <p class="total  subtitle is-bold">Number of Students:                        <span class="total-count  fa-sharp fa-solid  fa-beat is-offset-1" style="color:red !important; margin-left:5px;"></span>                        </p>
        panoramaSection.innerHTML += `<p class="total  subtitle is-bold">Total Objects Detected: <span class="total-count  fa-sharp fa-solid  fa-beat is-offset-1" style="color:red !important; margin-left:5px;">${response.data.total_objects}</span></p>`
        
        /**
         * DELETE THE IMAGES FROM THE SERVER
         */
        delete_image();

        stitchbtn.addEventListener("click", stitch);
        detectBTN.addEventListener("click", detect);
        }
    ).catch(function(error){
        console.log(error);

        // display the error message
        let errormsg = `<p class="error">${error}</p>`
        panoramaSection.innerHTML += errormsg;

    }
    );
}


  function stitch(){
    /**
     * Make a get request to the server to stitch the images
     */

  // Variables for Elements
    let image = document.querySelector(".preview");
    let total = document.querySelector(".total");
    let totalcount = document.querySelector(".total-count");
    let imageInput = document.getElementById("image");
    let filelabel = document.querySelectorAll(".file-cta");
    let panorama = document.getElementById("panorama");
    let stitchbtn = document.getElementById("stitchbtn");
    let previewImage = document.querySelector(".preview");
    let imagessection = document.querySelector(".images-section"); 
    let panoramaSection = document.querySelector(".panorama-section");
      let detectBTN = document.getElementById('detectbtn')
    let panoramaimg = document.querySelector(".panorama-image");  
    console.log("Stitching Images");
    // Hide the button
    stitchbtn.style = "display:none";
    // Hide the images section
    imagessection.style = "display:none";
    // Remove the form-section element
    document.querySelector(".form-section").remove(); 
    // Display the panorama section

    let myGift = 'https://miro.medium.com/v2/resize:fit:1400/1*e_Loq49BI4WmN7o9ItTADg.gif'
     panoramaimg = `<a href="${myGift}" target="_blank"><img src="${myGift}" alt="Panorama Image" class="panorama-image" style="width=100%;height:100%"></a>`
    panoramaSection.innerHTML += panoramaimg;

    axios.get('/api/stitch').then(function(response){
        let img = response.data.image;
        console.log(img);
        // Create an image element
        let panoramaimg  = document.querySelector(".panorama-image");
        // Append the image to the images section
        panoramaimg.src = img;
        document.getElementById("detectbtn").style = "display:block";
        // Display the stitched image

        stitchbtn.addEventListener("click", stitch);
        detectBTN.addEventListener("click", detect);
        }
    ).catch(function(error){
        console.log(error);
        // display the error message
        

        let panoramaimg  = document.querySelector(".panorama-image");
        let panoramaSection = document.querySelector(".panorama-section").querySelector("h1");
        panoramaimg.src = 'https://media1.giphy.com/media/l2R06FEpVRk6IroNq/giphy.gif'
        // Add the error message to the panorama section
        
        panoramaSection.innerHTML += `<i class="fas fa-exclamation-triangle" style="color: #eb0045;"></i>  <p class="error"> Stitching Failed. Please try again with better aligned images. </p> <a href="/upload"> <button href="/upload" class="button is-warning is-fullwidth is-outlined is-offset-2">Try Again</button></a>`
        
        panoramaimg.style = "width: 80%; height: 80%; margin-left: 10%; margin-right: 10%;"
        console.log(`Error: ${error}`);



    }
    );
   
    }

    function delete_image(){
        /**
         * Make a get request to the server to delete the images
         */
        axios.get('/api/delete_all').then(function(response){
            console.log(response.data);
            // display the success message
            let successmsg = `<p class="success">${response.data.message}</p>`
            document.querySelector(".images-section").innerHTML += successmsg;
            }
        ).catch(function(error){
            console.log(error);
            // display the error message
            let errormsg = `<p class="error">${error}</p>`
            document.querySelector(".images-section").innerHTML += errormsg;
    
        }
        );
    }


    addEventListener("DOMContentLoaded", () => {
        let image = document.querySelector(".preview");
        let total = document.querySelector(".total");
        let totalcount = document.querySelector(".total-count");
        let imageInput = document.getElementById("image");
        let filelabel = document.querySelectorAll(".file-cta");
        let panorama = document.getElementById("panorama");
        let stitchbtn = document.getElementById("stitchbtn");
        let previewImage = document.querySelector(".preview");
        let imagessection = document.querySelector(".images-section"); 
        let panoramaSection = document.querySelector(".panorama-section");
        let detectBTN = document.getElementById('detectbtn')
    
    });
