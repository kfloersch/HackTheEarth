import os

from imageai.Prediction.Custom import CustomImagePrediction


from flask import Flask, render_template
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename



def run_Image_AI(filename="empty"):
    execution_path = os.getcwd()

    prediction = CustomImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath("model_ex-092_acc-0.959971.h5")
    prediction.setJsonPath("model_class.json")
    prediction.loadModel(num_objects=7)

    predictions, probabilities = prediction.predictImage(filename, result_count=7)
    count = 0
    finPred = ""
    finProb = 0.0
    for eachPrediction, eachProbability in zip(predictions, probabilities):
      finPred = eachPrediction
      finProb = eachProbability
      break

    return finPred


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    UPLOAD_FOLDER = '../HackTheEarth'
    ALLOWED_EXTENSIONS = {'jpg'}

    #app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    # a simple page that says hello
    @app.route('/', methods=['GET', 'POST'])
    def home():
        error = None
        if request.method == 'POST':
        # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                result = run_Image_AI(filename)
                return redirect(url_for(result))
            if not allowed_file(file.filename):
                error = 'Error invalid file type'    
        return render_template('index.html', error = error)

    @app.route('/bottle')
    def bottle():
        return render_template('bottle.html')

    @app.route('/styrofoam')
    def styrofoam():
        return render_template('styrofoam.html')

    @app.route('/cans')
    def cans():
        return render_template('cans.html')

    @app.route('/paper')
    def paper():
        return render_template('paper.html')

    @app.route('/pizzabox')
    def pizzabox():
        return render_template('pizzabox.html')

    @app.route('/battery')
    def battery():
        return render_template('battery.html')

    @app.route('/plasticbag')
    def plasticbag():
        return render_template('plasticbag.html')

    @app.route('/resources')
    def resources():
        return render_template('resources.html')

    @app.route('/info')
    def info():
        return render_template('info.html')

    return app
