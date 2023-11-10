import cv2
import io
import base64
import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import torch
from torch import nn
import torchvision
from torchvision import transforms
import os


def decode_image(image):
    """
    Decode image from base64 to numpy array
    """
    image = base64.b64decode(image) 
    image = Image.open(io.BytesIO(image))
    image = np.array(image)
    return image

def imageToString(image):
    """
    Convert image to base64 string
    """
    image = Image.fromarray(image.astype('uint8'), 'RGB')
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def base64ToImage(base64_string):
    """
    Convert base64 string to image
    """
    imgdata = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(imgdata))

def read_image(path):
    """
    Read image from path
    """
    
    if os.path.exists(path):
        image = cv2.imread(path, cv2.IMREAD_COLOR)
        return image

    
def write_image(image, path):
    """
    Write image to path
    """
    cv2.imwrite(path, image)

WEIGHTS="yolov6s.pt"
SOURCE="static/input.jpg"
CONF_THRES=0.25
IOU_THRES=0.4
CLASSES=0
NAME="output"
SAVE_DIR="output"
import numpy as np
import os

import random
def infer(weights, source, img_size, conf_thres, iou_thres, classes, name, save_dir,Output_Name,Base64_Encoded_Image=None):
    if Base64_Encoded_Image is not None:
        img=Base64_Encoded_Image
        print("Image saved to ",source)
    else:
        assert os.path.exists(source), "Image not found"
    CMD=f"python3 infer.py --weights {weights} --source {source} --hide-labels  --img-size {img_size} --conf-thres {conf_thres} --iou-thres {iou_thres} --classes {classes} --name {name} --save-txt --save-dir {save_dir}"
    os.system(CMD)
    Output_Image_Path=os.path.join(save_dir ,source.split("/")[-1])
    Output_Label_Path=os.path.join(save_dir+"/labels" ,source.split("/")[-1].split(".")[0]+".txt")
    print("Output Image Path: ",Output_Image_Path)
    print("Output Label Path: ",Output_Label_Path)
    ## Save the image to static folder
    image=cv2.imread(Output_Image_Path)
    output_name =  f"{random.randint(0, 100000000)}-output.jpg"
    cv2.imwrite(f"static/{output_name}",image)    
    print("Output Image saved to ",f"static/{output_name}")
    Output_Image_Path=f"{output_name}"
    return Output_Image_Path,Output_Label_Path

def stitch(source='static/panorama/',output='static/panorama/'):
    """
    Stitch the image
    """
    # remove all the files that contain the word output
    os.system(f"rm {source}/*output*")
    
    print(f"stitch  {source}/*      --output {output}")
    os.system(f"stitch   {source}/*     --output {output}")
    
  #  image=cv2.imread(output)
    
    print("Output Image saved to ",output)
    
    return  output


    
    

