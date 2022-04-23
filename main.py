from flask import Flask, url_for, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "as;dfijqwo83ru0q idfjasdpo8fuawer"

def index():
    session["question_num"] = 0
    test_url = url_for("test")
    print(test_url)
    res = f"""<h1>Главная страница</h1>
    <h3>Список викторин:</h3>
    <ul>
        <li><a href="{test_url}">Викторина 1</a></li>
        <li>Викторина 2</li>
        <li>Викторина 3</li>
    </ul>
    """
    return res

def test():
    if session["question_num"] == 4:
        return redirect(url_for("result"))

    next_url = url_for("test")
    res = f"""Вопрос N {session["question_num"]}
    <br><a href="{next_url}">Следующий вопрос</a>
    """
    session["question_num"] += 1
    return res
        

def result():
    index_url = url_for("index")
    return f"""<h1>Вы справились!</h1>
    <a href="{index_url}">Перейти на главную</a>
    """

app.add_url_rule("/", "index", index)
app.add_url_rule("/test", "test", test)
app.add_url_rule("/result", "result", result)
app.run()