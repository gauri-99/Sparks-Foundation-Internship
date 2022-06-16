# Sparks-Foundation-Internship
Task 1 - Optical Character Recognition :
      In this task, text characters are detected from an image.
      To do this, first original image is processed to make the text easily recognisable for computer which consist of converting image to gray scale image, using threshold function/using edge detection.
      Then using 'Pytesseract' function, the text is detected from the image and is printed as the output.

Task 3 - Social Distancing Detection
       In this task, Social distancing detector is created using Open-CV. For this, first object detection is performed on the input image to detect the persons in the image and then the distance between two persons is measured and according to it. If the distance is less than the specific limit then that person is surrounded by red box indicating social distancing violation and if the person is at the safe distance from all the people then it is surrounded by green box indicating safe. 
