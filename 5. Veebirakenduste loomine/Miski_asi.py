from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    esinumber =request.args.get("esinumber", default = 1, type= float)
    teinenumber = request.args.get("teinenumber", default = 1, type= float)
    tüüp =request.args.get("tüüp", default = "")
    arv = 1
    if tüüp == "+":
        arv = esinumber + teinenumber
    elif tüüp == "-":
        arv = esinumber - teinenumber
    elif tüüp == "*":
        arv = esinumber * teinenumber
    elif tüüp == "/":
        arv = esinumber / teinenumber
    elif tüüp == "√":
        arv = esinumber ** (1/teinenumber)
    elif tüüp == "^":
        arv = esinumber ** teinenumber
        
    #Kui tahad midagi siia lisada, siis üldvalem on järgmine
    #elif tüüp == "x": (x = märk)
    #    arv = esinumber x teinenumber x = märk või valem
    
    esinumber = arv
    return render_template("index.html",
                          arv=arv,
                           esinumber =  esinumber,  
                           teinenumber = teinenumber,
                           tüüp = tüüp
                        )
 
if __name__ == "__main__":
    app.run(debug=True)


