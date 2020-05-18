# HackTheEarth
This is our repository for our Hack The Earth 2020 project

For this hackathon, we have created a web app, Is This Recyclable?, which allows users to upload photos of items to determine whether they are recyclable, and provide them with a page  with the necessary information about recycling the given item.

The project uses the ImageAI python library, to perform the analysis, coupled with the Flask library to host, as well to do this image recognition and redirection.

The Image Recognition was accomplished by using a model that we trained on several hundred images of recyclable objecs, like cans, bottles, and paper, and non recyclable objects, like stryofoam, batteries, and pizza boxes. Thus, the user can parse in an image and it will try and identify it as one of the objects that the model was trained on to then provide the corresponding information about recycling it.

The front end of this app is run through a combination of the Flask library which allows us to host and manage our webpage locally, and html/javascript, which creates the pages and allows movement and design between.

Because this web app is hosted locally, and not on a public server, in order to run the app we created a virtual environment using python 3.7.7, using the libraries: tensorflow (version 1.13.1), opencv, keras, flask, and imageAI.

Within this virtual environment we run the Flask app and open the default local domain, http://127.0.0.1:5000/.

From here using the web app is quite simple: just hit the upload image button, select the .jpg of your choosing, and wait for the web app to send you to the related page. You can navigate the website like any other and look at the attached resources.
