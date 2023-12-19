from flask import Flask, redirect, url_for
app = Flask(__name__)



@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)
    

@app.route("/lab1")
def lab1():
    return'''

<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Долбик Артём Евгеньевич, лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="/static/lab1.css">
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
    
        <p><a href="/menu" target="blank">Меню</a></p>

    <h2>Реализованные роуты</h2>
        <p><a href="/lab1/oak" target="blank">Дуб</a></p>
        <p><a href="/lab1/student" target="blank">Студент</a></p>
        <p><a href="/lab1/python" target="blank">Питон</a></p>
        <p><a href="/lab1/helicopter" target="blank">Вертолёт</a></p>
        

        <footer>
            &copy; Долбик Артём, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/menu")
def menu():
    return """

<!doctype html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" type="text/css" href="/static/lab1.css">    
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
    <head>
    <link rel="stylesheet" type="text/css" href="/static/lab1.css">
    </head>
    <html>
    <body>
        <h1>Дуб</h1>
        <img src="'''+ url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
    <head>
    <link rel="stylesheet" type="text/css" href="/static/lab1.css">
    </head>
    <html>
    <body>
        <h1>Долбик Артём Евгеньевич</h1>
        <img src="'''+ url_for('static', filename='NGTU.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
    <head>
    <link rel="stylesheet" type="text/css" href="/static/lab1.css">
    </head>
    <html>
    <body>
        <p>Высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, 
        <br />ориентированный на повышение производительности разработчика, читаемости кода и его качества, 
        <br />а также на обеспечение переносимости написанных на нём программ.</p>
        <img src="'''+ url_for('static', filename='python.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/helicopter")
def helicopter():
    return '''
<!doctype html>
    <head>
    <link rel="stylesheet" type="text/css" href="/static/lab1.css">
    </head>
    <html>
    <body>
        <p>Вертолёт — винтокрылый летательный аппарат вертикального взлёта и посадки, 
        <br />у которого подъёмная и движущая силы на всех этапах полёта создаются одним или несколькими несущими винтами 
        <br/>с приводом от одного или нескольких двигателей.</p>
        <img src="'''+ url_for('static', filename='helicopter.jpg') + '''">
    </body>
</html>
'''