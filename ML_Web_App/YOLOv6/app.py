import random
from flask_tools import *
import os
from torchvision import transforms
import torchvision
from torch import nn
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import base64
import io
import cv2
from flask import Flask, render_template, request, jsonify
import torch
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home() -> str:
    return render_template("detect.html")


public = os.path.join(os.path.dirname(__file__), 'static')


@app.route('/detect', methods=['POST', 'GET'])
def detect_objects():
    if request.method == 'GET':
        return render_template("detect.html")
    try:
        image = request.files['image']
        image = image.read()
       
        #  Save the image to static folder
        # Generate a random name for the image
        # Save the image to static folder
        with open('static/input.jpg', "wb") as fh:
            fh.write(image)
        output_name =  f"{random.randint(0, 100000000)}-output.jpg" 
        SAVE_DIR = "static"        
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
        
            
    except Exception as e:
        print(e)
        print("Output Image Path: ", Output_Image_Path)
        return jsonify({"error": "No image provided"})
    return render_template("detect.html", image=Output_Image_Path, total_objects=total_objects)

# API
@app.route('/api/detect', methods=['POST'])
def api_detect():
    
    try:
        # If the image is not provided
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"})
        
        image = request.files['image']
        image = image.read()
       
        #  Save the image to static folder
        # Generate a random name for the image
        # Save the image to static folder
        with open('static/input.jpg', "wb") as fh:
            fh.write(image)
        output_name =  f"{random.randint(0, 100000000)}-output.jpg" 
        SAVE_DIR = "static"        
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
        JSON = {"image": Output_Image_Path,        "total_objects": total_objects,        "labels": labels    } 
        

        
    except Exception as e:
        print(e)
        print("Output Image Path: ", Output_Image_Path)
        return jsonify({"error": "No image provided"})
    return jsonify(JSON)


if __name__ == '__main__':
    app.run(debug=True)
