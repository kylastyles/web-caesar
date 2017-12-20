from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
            .error {{
                color: red;
            }}

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
            <form action="/" method="post">
                <p class="error">{rot_error}</p>
                <label>Rotate by:<input name="rot" type="text" value=0 /></label>
                <textarea name="text">{text}</textarea>
                <button>Submit Query</button>
            </form>
        </body>
    </html>
"""

#check that rot entry is a valid number
def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

#show form on index page
@app.route("/")
def index():
    return form.format(rot_error="", text="")

#respond to user entry
@app.route("/", methods=["post", "get"])
def encrypt():

    #set variables
    rot = request.form["rot"]
    text = request.form["text"]

    #check for valid numerical entry
    if is_integer(rot) == True:
        rot = int(rot)
        text = cgi.escape(text)
        rotated = rotate_string(text, rot)
        #return encrypted text if all good
        return form.format(rot_error="", text=rotated)
    else:
        rot_error = "Please enter whole numbers only."
        #return error message and blank form if bad
        return form.format(rot_error=rot_error, text="")

app.run()