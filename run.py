# _*_ coding: utf-8 _*_

from flask import Flask, request, render_template, Markup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from stuff import player_stuff

app = Flask(__name__)

name = "리루크"

piles = {'나무':1, '양':1, '사람':1,'원':1}

@app.route("/", methods=['GET'])
def main():
	#return "안녕하센요 %s"%name
    return render_template("template.html")

@app.route("/phase_one", methods=['GET', 'POST'])
def p_one():
    items_list = ""
    piles_list = ""
    for k, v in player_stuff.items():
        if v > 0:
            items_list = items_list+"<li>"+k+": "+str(v)+"</li>"
    for k, v in piles.items():
        piles_list = piles_list+str(v)+" free "+k+" OR <br/>"
    items_list = Markup(items_list)
    piles_list = Markup(piles_list)
    return render_template("phase_one.html", the_list=items_list, piles=piles_list, name=request.form.get("name", ""))

@app.route("/phase_two", methods=['GET', 'POST'])
def p_two():
    return render_template("phase_two.html")

if __name__ == "__main__":
    app.run(debug=True)
