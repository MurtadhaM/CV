import random
from flask_tools import *
import os
import base64
from flask import Flask, render_template, request, jsonify,flash, redirect, url_for
from werkzeug.exceptions import RequestEntityTooLarge
from flask import Flask, render_template, redirect, request, send_from_directory
from werkzeug.utils import secure_filename
from flask import Flask, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename
# serve_image
from flask import Flask, send_from_directory
from flask import Flask, render_template, redirect, request, send_from_directory
from flask_toastr import Toastr
from flask import flash
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG', 'PNG', 'JPEG', 'GIF', 'bmp', 'BMP', 'svg', 'SVG'}

app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['SECRET'] = 'secret'
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_DIRECTORY'] = 'static/panorama'
app.config['SECRET_KEY'] = 'supersecretkeygoeshere'
app.config['TOASTR_POSITION_CLASS'] = 'toast-top-center'
app.config['TOASTR_CLOSE_BUTTON'] = True
app.config['TOASTR_PROGRESS_BAR'] = True

app.config['PANORAMA'] = 'static/panorama'
app.config['UPLOAD_FOLDER'] = 'static/panorama'


toastr = Toastr(app)
# USE NIMAGES instead of IMAGES to accept .JPG as IMAGES doesn't accept .JPG images
NIMAGES = tuple('JPG jpg jpe jpeg png gif svg bmp'.split())



@app.route('/api/delete/<path:filename>', methods=['GET'])
def delete_file(filename):
    if os.path.exists(f'static/panorama/{filename}'):
        os.remove(f'static/panorama/{filename}')
        return jsonify({"message": "Deleted"})
    else:
        return jsonify({"message": "File not found"})
    
@app.route('/api/delete_all', methods=['GET'])
def delete_all():
    # Delete the files
    Files = os.listdir('static/panorama')
    for file in Files:
        os.remove(f'static/panorama/{file}')
    return jsonify({"message": "Deleted"})





@app.route('/', methods=['GET'])
def home() -> str:
    return render_template("detect.html")


public = os.path.join(os.path.dirname(__file__), 'static')

@app.route('/detect', methods=['GET'])
def detect():
    FILES =  os.listdir('static/panorama')
    # FIND FIELS THAT HAVE output in them
    FILES = [file for file in FILES if 'output' in file]
    if FILES.__len__() > 0:
        # read the image
        image = cv2.imread(f'static/panorama/{FILES[0]}')
        # Generate a random name for the image
        # Save the image to static folder
        output_name = f"{random.randint(0, 100000000)}-output.jpg"
        SAVE_DIR = "static/"
        # Save the image to static folder
        
        ##### SAVE THE IMAGE TO THE INPUT static/input.png
        os.system(f"cp static/panorama/*output* static/input.jpg")
        os.system(f"rm  static/labels/input.txt ; touch static/labels/input.txt")
        
        ###
        Output_Image_Path, Output_Label_Path = infer(
            WEIGHTS, SOURCE, 640, CONF_THRES, IOU_THRES, CLASSES, NAME, SAVE_DIR, Base64_Encoded_Image=image, Output_Name=output_name)
        # Save the image to static folder
        with open(Output_Image_Path, "wb") as fh:
            fh.write(image)
        # Read the label file
        labels = []
        with open('static/labels/input.txt', "r") as fh:
            labels = fh.readlines()
        # Remove the file
        os.remove('static/labels/input.txt')
        # Total number of objects detected
        total_objects = len(labels)
        print("Total Objects Detected: ", total_objects)
        Output_Image_Path = '/static/' + Output_Image_Path
        JSON = {"image": Output_Image_Path, "total_objects": total_objects, "labels": labels}
        return jsonify(JSON)
    else:
        return render_template("detect.html")
    

    
        
        

def allowed_file(filename):
    return '.' in filename and \
           filename.split('.')[1].lower() in ALLOWED_EXTENSIONS


# API
@app.route('/api/detect', methods=['POST'])
def api_detect():

    try:
        # If the image is not provided
        if 'image' not in request.files:
            errorcode = 400
            return jsonify({"error": "No image provided"}), 400

        image = request.files['image']
        image = image.read()

        #  Save the image to static folder
        # Generate a random name for the image
        # Save the image to static folder
        with open('static/input.jpg', "wb") as fh:
            fh.write(image)
        output_name = f"{random.randint(0, 100000000)}-output.jpg"
        SAVE_DIR = "static/"
        # Save the image to static folder
        Output_Image_Path, Output_Label_Path = infer(
            WEIGHTS, SOURCE, 640, CONF_THRES, IOU_THRES, CLASSES, NAME, SAVE_DIR, Base64_Encoded_Image=image, Output_Name=output_name)
        # Save the image to static folder
        with open(Output_Image_Path, "wb") as fh:
            fh.write(image)

        # Read the label file
        labels = []
        with open('static/labels/input.txt', "r") as fh:
            labels = fh.readlines()
        # Remove the file
        os.remove('static/labels/input.txt')
        # Total number of objects detected
        total_objects = len(labels)
        print("Total Objects Detected: ", total_objects)
        Output_Image_Path = '/static/' + Output_Image_Path
        JSON = {"image": Output_Image_Path,
                "total_objects": total_objects, "labels": labels}
        
        

    except Exception as e:
        print(e)
        return jsonify({"error": "No image provided"})
    return jsonify(JSON)

@app.route('/api/stitch', methods=['GET'])
def process_stitch():
    # Get the files from the panorama folder
    Files = os.listdir('static/panorama')
    # Filter the images that are not required
    Files = [file for file in Files if os.path.splitext(file)[1].lower().replace('.', '') not in NIMAGES]
    # Delete the files
    for file in Files:
        os.remove(f'static/panorama/{file}')
    # Get the files from the panorama folder
    Files = os.listdir('static/panorama')
    # Filter the images
    Files = [file for file in Files if os.path.splitext(file)[1].lower().replace('.', '') in NIMAGES]
    if Files.__len__() < 3:
        return jsonify({"error": "5 images are required"}, 400)
    # Stitch the images
    output_name = f"{random.randint(0, 100000000)}-output.jpg"
    SAVE_DIR = "static/panorama"
    full_path = os.path.join(SAVE_DIR, output_name)
    # Perform the stitching
    Output_Image_Path = stitch( SAVE_DIR, full_path)
    if os.path.exists(Output_Image_Path):    
        JSON = {"image": Output_Image_Path}
        return jsonify(JSON)
    else:   
        return jsonify({"error": "Stitching was not possible with the provided images....deleting now"}), 400
    
    

    

# API
@app.route('/api/stitch', methods=['POST'])
def api_stitch():
    # if 5 or more images are not provide
    # d
    # GET THE FILES FROM THE JSON
    Request_FILES = request.json
    
    # Parse the JSON
    files = []    
    
    for file in Request_FILES:
        name = file['name']
        file = file['value']
        files.append(file)
    # Number of images
    number_of_images = files.__len__()
    print(f"Number of images: {number_of_images}")

    if number_of_images < 5:
        return jsonify({"error": "5 images are required"})
    # Delete all the images from the panorama folder
    currentDirFiles = os.listdir('static/panorama')
    print(f"List of files: {Request_FILES[0]['name']}")
    # fi
    for file in currentDirFiles:
        if  file not in Request_FILES[0]['name']:
            os.remove(f'static/panorama/{file}')
            #image = file['value']
            #name = file['name']
    
    # Save the images to the panorama folder
    for file in Request_FILES:
        # Save the image to static folder
        name = file['name']
        file = file['value']
        with open(f'static/panorama/{name}', "wb") as fh:
            fh.write(base64.b64decode(file.split(',')[1]))
            
            
            
            fh.write(base64.b64decode(file))
    # Stitch the images
    
        
    JSON = {"image": "static/panorama/panorama.jpg"}
    return jsonify(JSON)



@app.route('/upload', methods=['GET'])
def upload_multi():
    Missing = (3 - os.listdir('static/panorama').__len__())
    files = os.listdir('static/panorama')
    # Filter the images
    files = [file for file in files if os.path.splitext(file)[1].lower().replace('.', '') in NIMAGES]
    
    
    if Missing > 0:
        Ready=False
        files = os.listdir('static/panorama')
        
        return  render_template('upload.html', error=f'{Missing} more image(s) required', ready=False,Missing=Missing, images=files)
    images = []
    for file in files:
        if os.path.splitext(file)[1].lower().replace('.', '') in NIMAGES:
          images.append(file)
    print(images)
    return render_template('upload.html', images=images, ready=True,Missing=0)


@app.route('/upload', methods=['POST'])
def upload():
    try:
        files = request.files.getlist('file')
        Missing = (3 - os.listdir('static/panorama').__len__())
        
        for file in files:
                if file:
                    extension = os.path.splitext(file.filename)[1].lower().replace('.', '')
                    print(extension)
                    if extension not in app.config['ALLOWED_EXTENSIONS']:
                        print('not allowed')
                    filename = secure_filename(file.filename  )
                    file.save(os.path.join('static/panorama/', filename))
        return redirect(url_for('upload_multi'), code=302)
            
            
            
                   
    except Exception as e:
        print(e)
        flash('Ready to Process', 'success')
        return  redirect(url_for('upload_multi'), code=302)
    return render_template('upload.html', ready=True, code=302, error='Ready to Process', images=os.listdir('static/panorama'),Missing=0)     

# serve_image
@app.route('/serve_image/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/panorama', filename)


if __name__ == '__main__':
    app.run(debug=True)
