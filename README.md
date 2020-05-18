# HackTheEarth
This is our repository for our Hack The Earth 2020 project

What we've created for this hackathon is a web app, "IsThisRecyclable", which allows users to upload photos of something they are usnure whether is or is not recyclable. And then redirects them to a page providing them with information about that given item.

The project uses the ImageAI python library, to perform the analysis, coupled with the Flask library to host, to do this image recognition and redirection.

The Image Recognition was accomplished by using a model that we trained on several hundred images of recyclable objecs, like cans, bottles, and paper, and non recyclable objects, like stryofoam, batteries, and pizzaboxes. And then parsing in an image submitted by the user to try and identify if its one of the objects the model was trianed on and categorize it correctly to Recyclable or not recyclable.

The frontend of this app is run through a combination of the Flask library which allows us to host and manage our webpage locally, and html/javascript, which creates the pages and allows movement and design between.

Because this webapp is hosted locally, and not on a public server, in order to run the app we created a virtual environment using python 3.7.7, using the libraries: tensorflow (version 1.13.1), opencv, keras, flask, and imageai.


Within this virtual environment we run the Flask app and open the defauly local domain, http://127.0.0.1:5000/.

From here usig the web app is quite simple, just hit the upload image button, select the jpg of your choosing, and wait for the wepapp to send you to the related page. You can navigate the website like any other and look at the resources attatched.
