from flask import Flask, request
from flask.templating import render_template_string
from flask_restx import fields, Api, Resource

app = Flask(__name__)

api = Api(app)

@app.route('/index')
def get():
  name = request.args.get('name')

  HTML_PAGE = f"""<html>
  <head>
    <title>This is the title of the webpage!</title>
  </head>
  <body>
    <p>Meu nome é {name}</p>
  </body>
</html>"""

  return render_template_string(HTML_PAGE)

app.run(debug=False)