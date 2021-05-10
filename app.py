from flask import Flask, render_template, request

app = Flask(__name__)

# model = pickle.load(open('file_name.pkl', 'rb'))


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/predict", methods=['POST'])
def predict():
    # if request.method == 'POST':
    #     # add form input tag's name to data list
    #     data = []
    #     user_input = list()
    #     for i in data:
    #         x = request.form[i]
    #         if x == '':
    #             output = 1
    #             text = "Invalid Input!"
    #             return render_template('index.html', output=output, text=text)
    #         user_input.append(float(x))
    #     output = model.predict([user_input])
    #     if(output):
    #         return render_template('index.html', output=output, text=text)
    #     else:
    #         return render_template("index.html", output=output, text=text)
    return render_template("index.html")


if(__name__ == '__main__'):
    app.run(debug=True)
