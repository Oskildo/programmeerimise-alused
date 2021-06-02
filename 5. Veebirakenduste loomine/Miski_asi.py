import random
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    miinimum =request.args.get("miinimum", default = 1, type= int)
    maksimum = request.args.get("maksimum", default = 100, type= int)
    kogus = request.args.get("kogus", default = 1, type= int)
    if kogus < 0:
        kogus = 0
    n = kogus
    arv = []
    while n != 0:
        arv +=[random.randint(miinimum, maksimum)]
        n -=1
    return render_template("index.html",
                           arv=arv,
                           miinimum =  miinimum,  
                           maksimum = maksimum,
                           kogus = kogus
                        )
 
if __name__ == "__main__":
    app.run(debug=True)


