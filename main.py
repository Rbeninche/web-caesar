from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
        <html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action = "" method = "POST">
      <label> Rotate by:
      <input name ="rot" type="text" value="0"/>
      </label>
      
      <textarea name ="text" placeholder={0}></textarea>
      
      <input type="submit" value="Submit Query"/>
      </form>
    </body>
</html>
        """


@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    cypher_ceasar = rotate_string(text, rot)

    return form.format(cypher_ceasar)


app.run()
