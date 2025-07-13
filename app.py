from flask import Flask, render_template, request, session
import math

app = Flask(__name__)
app.secret_key = "smartcalc_secret"

def safe_eval(expr):
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({'abs': abs, 'round': round})
    try:
        return str(eval(expr, {"__builtins__": {}}, allowed_names))
    except Exception:
        return "Error"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        expression = request.form.get("expression")
        result = safe_eval(expression)
        session["history"].append(f"{expression} = {result}")
        session["history"] = session["history"][-5:]  # Keep last 5
        session.modified = True

    return render_template("index.html", result=result, history=session["history"])

if __name__ == "__main__":
    app.run(debug=True)
