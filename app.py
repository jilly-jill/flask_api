from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
import json with open['mutants.json', "rw" ]

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            name = data["name"]
            roles = data["roles"]
            powers = data["powers"]
            mutant.append({"name": name, "powers": powers, "roles": roles})

    return jsonify(mutant)
    # return render_template('index.html' mutant=)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 2224)
