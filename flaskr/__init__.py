import os
from unicodedata import name

from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import jsonify
from flask import request

objects = [
    {"id": 1, "name": "Red apple", "color": "Red", "type": "Fruit"},
    {"id": 2, "name": "Blue backpack", "color": "Blue", "type": "Accessory"},
    {"id": 3, "name": "Wooden chair", "color": "Brown", "material": "Wood"},
    {"id": 4, "name": "Silver spoon", "color": "Silver", "material": "Metal"},
    {"id": 5, "name": "Green tennis ball", "color": "Green", "sport": "Tennis"},
    {"id": 6, "name": "Leather wallet", "color": "Brown", "material": "Leather"},
    {"id": 7, "name": "Ceramic coffee mug", "color": "White", "material": "Ceramic"},
    {"id": 8, "name": "Rubber duck", "color": "Yellow", "type": "Toy"},
    {"id": 9, "name": "Glass vase", "color": "Clear", "material": "Glass"},
    {"id": 10, "name": "Plastic flashlight", "color": "Black", "material": "Plastic"}
]
filtered = []

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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/tanya')
    def tanya():
        name = "Saite"
        return render_template("tanya.html", name=name, objects = objects)

    @app.route('/test')
    def testing_page():
        name = "Testing..."
        return render_template("testing.html", name=name)


    @app.route('/delete/<int:id>',methods=('POST',) )
    def delete(id):
        print(id)
        return render_template("delete_message.html", id = id)

    
    @app.route('/select')
    def select():
        return render_template('select.html')
    
    @app.route('/selected', methods=['POST'])
    def selected():
        selected_number = request.form['selected_number']
        return f'You selected: {selected_number}'




    

    return app