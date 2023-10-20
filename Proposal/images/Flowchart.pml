# This is an AI system train on faces and recognize them using webcam 

```plantuml
@startuml
Camera -> FaceRecognition: Take a picture
FaceRecognition -> FaceRecognition: Detect faces
FaceRecognition -> FaceRecognition: Crop faces
FaceRecognition -> FaceRecognition: Resize faces
FaceRecognition -> FaceRecognition: Convert to grayscale
FaceRecognition -> FaceRecognition: Convert to numpy array
FaceRecognition -> FaceRecognition: Recognize faces
FaceRecognition -> FaceRecognition: Draw rectangle around faces
FaceRecognition -> FaceRecognition: Show image




@enduml
```
