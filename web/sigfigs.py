from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "bruh"

@app.route("/figures")
def signums():
    number = request.args["number"]
    dots = number.count(".")
    if dots > 1:
        return "invalid number", 400
    return {"figs": figs(number, dots == 1)}

def firstoccurence(string, find):
    for i, char in enumerate(string):
        if char == find:
            return i

def figs(number, hasdot):
    for i, char in enumerate(number):
        if char != "0":
            number = number[i:]
            break
    if hasdot:
        return len(number) - 1
    for i in range(len(number) - 1, 0, -1):
        print(i)
        if number[i] != "0":
            number = number[:i + 1]
            break
    return len(number)

if __name__ == "__main__":
    app.run(debug=True)
