from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/', methods=["get","post"])
def index():

    message =""
    if request.method == "POST":
        model = request.form.get("area")

        message = f'Вычисленное значение'

    return render_template('html.html', message=message)


app.run()



