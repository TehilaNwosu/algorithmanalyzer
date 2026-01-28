from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        algorithm = request.form.get("algorithm")
        n = request.form.get("n")

        results = {
            "best": "O(n)",
            "average": "O(n log n)",
            "worst": "O(n^2)"
        }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
