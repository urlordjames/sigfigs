from flask import Flask, request, send_file

app = Flask(__name__)

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
    if len(number) > 50:
        return "too many digits, request refused", 431
    return {"figs": figs(number, dots == 1)}

def figs(number, hasdot):
    for i, char in enumerate(number):
        if char in digits:
            number = number[i:]
            break
    number = number.replace(".", "")
    if hasdot:
        return len(number)
    for i in range(len(number) - 1, -1, -1):
        if number[i] in digits:
            number = number[:i + 1]
            break
    return len(number)

if __name__ == "__main__":
    app.run(debug=True)
