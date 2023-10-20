import urllib.request
import json
import os
import ssl
import base64


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Read Image path from command line
import sys


def get_image(image_path):
    with open(image_path, 'rb') as f:
        image = f.read()
        # Base64 encode the input image
        image = base64.b64encode(image)
        return image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def print_result(result, image_path):
  bounding_boxes = json.loads(result)
  original_image = mpimg.imread(image_path)
  
  # Display the image and draw the predicted boxes onto it.
  plt.imshow(original_image)
  current_axis = plt.gca()
  for box in bounding_boxes:
    print(box)
    # Transform the predicted bounding boxes for the 300x300 image to the original image dimensions.
    xmin = box['bottomX'] * original_image.shape[1] / 300
    ymin = box['bottomY'] * original_image.shape[0] / 300
    xmax = box['topX'] * original_image.shape[1] / 300
    ymax = box['topY'] * original_image.shape[0] / 300
    color = np.random.rand(3)
    current_axis.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, color=color, fill=False, linewidth=2))  
    label = '%s: %.2f' % (box['label'], box['probability'])
    current_axis.text(xmin, ymin, label, size='x-large', color='white', bbox={'facecolor':color, 'alpha':1.0})  
  plt.show()
  
    
    
  
  
  

def predict(image):
  # Request data goes here
  # The example below assumes JSON formatting which may be updated
  # depending on the format your endpoint expects.
  # More information can be found here:
  # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
  print("Predicting...")
  print(image)
  data =  {
    "input_data": {
      "columns": [
        "image"
      ],
      "index": [
        "0"
      ],
      "data":  [
        "\"" + image.decode("utf-8") + "\""
      ]
    },
    "params": {}
  }

  body = str.encode(json.dumps(data))

  url = 'https://findasnake-pvhjn.eastus2.inference.ml.azure.com/score'
  # Replace this with the primary/secondary key or AMLToken for the endpoint
  api_key = 'habe780dcbjzqaYhmPp8O7T4EY7RWh2f'
  if not api_key:
      raise Exception("A key should be provided to invoke the endpoint")

  # The azureml-model-deployment header will force the request to go to a specific deployment.
  # Remove this header to have the request observe the endpoint traffic rules
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'yolof-r50-c5-8x8-1x-coco-6' }

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)

      result = response.read()
      return result
    
  except urllib.error.HTTPError as error:
      print("The request failed with status code: " + str(error.code))

      # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())
      print(error.read().decode("utf8", 'ignore'))

      
      
  

  

def main():
    # Get the image path from the command line
  if len(sys.argv) < 2:
    print("Usage: python predict_image.py <image path>")
    exit(-1)
  else:
    image_path = sys.argv[1]
    image = get_image(image_path)
    prediction_json = predict(image)
    
    print_result(prediction_json, image_path)

if __name__ == "__main__":
    main()

