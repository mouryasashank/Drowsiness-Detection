# Drowsiness-Detection
## Description
The objective is to keep mishaps by showing the drivers from the tiredness like when they feel lethargic yet they are in driving. Yet, this will distinguish the eyes and make the most of an after some tally it will caution the drives that they are dozing this may cause to mishaps.

We used Machine Learning and Computer Vision to detect the drowsiness.

![](/sample.png)

When we our eyes looks normally the output image looks like this.
Blue border indicates the face and the green borders indicates the eyes.

Drowsiness is one of the main issues that the drivers are facing nowadays due to long hours of journey.
It is merely nothing but a microsleep . Due to this many accidents can happen, to avoid this we are using a deep-learning algorithm to detect and warn the driver when he is about to sleep. Our approach is based on eye blink rate, eye closure. For this, we trained our model by using a Convolutional neural network(CNN) as they are well suited to extract important features and high accuracy for the image classification. At last, we used the softmax layer to classify whether the eyes are open or closed. The dataset contains the eyes of 5 different persons with a total of 7400 images without having glasses by doing data augmentations. Initially, we use open cv to detect the face and eyes using the Haar classifier. After that, each frame is passed through a trained model to classify whether the eyes are closed or open, If eyes are closed for more than 3 sec it triggers the warning by ringing the sound.
Maybe in future, we can also do that decreasing velhicle's acceleration by using the Internet of Things(IOT) when the drivers eyes are closed for more than 5 sec to prevent from the accidents.
