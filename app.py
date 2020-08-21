def chatbot_run():
    import wolframalpha
    import pyttsx3
    from flask import Flask, render_template, request

    app_id = '34U93P-WGR36VG7WE'
    client = wolframalpha.Client(app_id)
    app = Flask(__name__)
    app.static_folder = 'static'


    @app.route("/")
    def home():
        return render_template("index.html")


    @app.route("/get")
    def get_bot_response():
        userText = request.args.get('msg')
        res = client.query(userText)
        answer = next(res.results).text
        engine = pyttsx3.init()
        engine.say(answer)
        engine.runAndWait()
        return str(answer)


    if __name__ == "__main__":
        app.run(debug=True)
def print(n):
    print(n)
