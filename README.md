# HackTheEarth
This is our repository for our Hack The Earth 2020 project

For this hackathon, we have created a web app, Is This Recyclable?, which allows users to upload photos of items to determine whether they are recyclable, and provide them with a page with the necessary information about recycling the given item.

The project uses the ImageAI python library to perform the analysis, coupled with the Flask framework for the web app. This allows us to power our web pages with a python back-end, in order to do this image recognition on user-provided images.

The Image Recognition was accomplished by using a model that we trained on over one thousand images of recyclable objects, like cans, bottles, and paper, and non recyclable objects, like styrofoam, batteries, and pizza boxes. The user can upload an image, and our model will try and identify it as one of the objects that it was trained on. When the item has been identified, the user is redirected to a page with information about recycling their item.

The web app is created with html/css/javascript on the front-end combined with python and the Flask framework on the back-end. Flask allows us to serve our pages and do image processing using a python back-end, while html/css/javascript creates the pages, styling, and allows us to dynamically display info based on user interactions.

Because this web app is hosted locally, and not on a public server, in order to run the app we created a virtual environment using python 3.7.7, using the libraries: tensorflow (version 1.13.1), opencv, keras, flask, and imageAI.

Within this virtual environment we run the Flask app and open the default local domain, http://127.0.0.1:5000/.

From here using the web app is quite simple: just hit the upload image button, select the .jpg of your choosing, and wait for the web app to send you to the related page. You can navigate the website like any other and look at the attached resources.