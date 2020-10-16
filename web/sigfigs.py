from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("static/index.html")

# dumb hack for development, override in production
@app.route("/calculate.js")
def calc():
    return send_file("static/calculate.js")

@app.route("/figures", methods=["POST"])
def signums():
    number = request.json["number"]
    dots = number.count(".")
    if dots > 1:
        return "invalid number", 400
    return {"figs": figs(number, dots == 1)}

def figs(number, hasdot):
    for i, char in enumerate(number):
        if char != "0" and char != ".":
            number = number[i:]
            break
    print(number)
    if hasdot:
        return len(number.replace(".", ""))
    for i in range(len(number) - 1, 0, -1):
        if number[i] != "0":
            number = number[:i + 1]
            break
    return len(number)

if __name__ == "__main__":
    app.run(debug=True)
