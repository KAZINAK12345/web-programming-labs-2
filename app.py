from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Долбик Артём Евгеньевич, лабораторная1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <p>Flask - фреймворк для создания веб-приложений на языке программирования Python, 
        <br />использующий набор инструментов Werkzeug, а также шаблонизатор jinja2. 
        <br />Относится к категории так называемых микрофреймворков - минималистичных каркасов 
        <br />веб-приложений, сознательно предоставляющих лишь самые базовые возможности</p>
        <footer>
            &copy; Долбик Артём, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
""" 

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1><a href="/lab1" target="blank">Лабораторная работа 1</a></h1>
    
        <footer>
            &copy; Долбик Артём, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
""" 

@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <body>
       <h1>Дуб</h1>
       <img src="'''+ url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
''' 