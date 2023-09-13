from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
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
    
        <footer>
            &copy; Долбик Артём, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
""" 

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