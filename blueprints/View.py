from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models.article import Article
from models.Camera import Camera


main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():  # put application's code here
    return render_template("home.html", title="This is a title")


@main_blueprint.route('/knowledge')
def knowledge():
    # Read database
    articles = Article.query.all()
    return render_template("knowledge.html", articles = articles)


@main_blueprint.route('/select')
def select():
    return render_template("select.html")


@main_blueprint.route('/search')
def search():
    # get all cameras parameter
    items = Camera.query.all()
    return render_template("search.html", items = items)

@main_blueprint.route('/search/<Name>')
def search_item(Name):
    camera = Camera.query.get_or_404(id)
    print(camera)
    return render_template("camera.html", camera = camera)


@main_blueprint.route('/Video')
def video():
    return render_template('SelectVideo.html')


@main_blueprint.route('/Choice', methods=['GET', 'POST'])
def Choice_input():
    if request.method == 'POST':
        LowLight = True if "LowLight" in request.form.keys() and request.form['LowLight'] == 'True' else False
        LightCamera = True if "LightCamera" in request.form.keys() and request.form['LightCamera'] == 'True' else False
        QPRatio = True if "QPRatio" in request.form.keys() and request.form['QPRatio'] == 'True' else False
        LargePiece = True if "LargePiece" in request.form.keys() and request.form['LargePiece'] == 'True' else False
        Sport = True if "Sport" in request.form.keys() and request.form['Sport'] == 'True' else False
        list_option = {'LowLight': LowLight, 'LightCamera': LightCamera, 'QPRatio':QPRatio, 'LargePiece':LargePiece, 'Sport':Sport}
        # check point
        # print(list_option)
        return redirect(url_for('main.result',**list_option))

    return render_template('SelectChoice.html')

@main_blueprint.route('/knowledge/<id>')
def knowledge_article(id):
    article = Article.query.get_or_404(id)
    # check point
    # brand = Camera.query.all()
    # for camera in brand:
    #     print(camera.Brand)
    return render_template('knowledgePage.html',  article = article)

@main_blueprint.route('/result')
def result():
    # get chocie for choice pages and get cameras data for database
    kwargs = request.args
    Camera_Date = Camera.query.all()

    # manage data by Choice page option
    if kwargs["LowLight"] == 'True':
        Camera_Date = [i for i in Camera_Date if i.Type == "Mirrorless"]
    if kwargs["LightCamera"] == 'True':
        Camera_Date = [i for i in Camera_Date if i.Weight <= 600]
    if kwargs["QPRatio"] == 'True':
        Camera_Date = [i for i in Camera_Date if i.Price <= 1500]
    if kwargs["LargePiece"] == 'True':
        Camera_Date = [i for i in Camera_Date if i.EffectivePixels >= 2500]
    if kwargs["Sport"] == 'True':
        Camera_Date = [i for i in Camera_Date if i.FrameAdvanceRate >= 7]

    # Reorganization of data
    images = [camera.Herf for camera in Camera_Date]
    names = ["Name"] + [camera.Name for camera in Camera_Date]
    brand = ["Brand"] + [camera.Brand for camera in Camera_Date]
    Type = ["Type"] + [camera.Type for camera in Camera_Date]
    ImageSensor = ["Image Sensor"] + [camera.ImageSensor for camera in Camera_Date]
    EffectivePixels = ["Effective Pixels (MP)"] + [camera.EffectivePixels for camera in Camera_Date]
    FrameAdvanceRate = ["Frame Advance Rate"] + [camera.FrameAdvanceRate for camera in Camera_Date]
    ShutterSpeed = ["Shutter Speed"] + [camera.ShutterSpeed for camera in Camera_Date]
    Dimensions = ["Dimensions (W x H x D)"] + [camera.Dimensions for camera in Camera_Date]
    Weight = ["Weight (g)"] + [camera.Weight for camera in Camera_Date]
    Price = ["Price (£)"] + [camera.Price for camera in Camera_Date]

    # translate it to a two-dimensional array
    # title need another group

    datas = [names, brand, Type, ImageSensor, EffectivePixels, FrameAdvanceRate, ShutterSpeed, Dimensions, Weight, Price]

    return render_template('result.html', datas= datas, images = images)