from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])



def calc():
    if request.method == "POST":
        sum = int(request.form['sum'])
        perc = 1 + (int(request.form['perc']) * 0.01)
        srok = int(request.form['srok'])
        start_sum = sum
        for i in range(srok):
            sum = sum * perc

        itog = "За " + str(srok) + " года Ваши " + str(start_sum) + " денег превратятся в " + str(sum) + " с годовым процентом " + str((perc-1)*100)
        return render_template('calc.html', itog=itog)



    else:
        return render_template("calc.html")

def sum(sum):
    try:
        if type(sum) == float:
            return "Error"
        a = int(sum)
        if a <= 0 :
            return "Error"
    except:
        return "Error"
    return a

def perc(perc):
    try:
        if type(perc) == float:
            return "Error"
        a = int(perc)
        if a <= 0 or a > 100:
            return "Error"
    except:
        return "Error"
    return a

def srok(srok):
    try:
        if type(srok) == float:
            return "Error"
        a = int(srok)
        if a <= 0 or a > 50:
            return "Error"
    except:
        return "Error"
    return a


def start():
    app.run(debug=True)