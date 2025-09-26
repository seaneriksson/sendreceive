from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")

#Fixed size list
message_slots = ["", "", ""]

@app.route("/")
def sender():
    return render_template('index.html', messages=message_slots)

@app.route("/about/")
def receiver():
    return render_template('about.html', messages=message_slots)

@app.route('/process', methods=['POST'])
def process_message():
    data = request.get_json()
    message = data.get("value")
    index = int(data.get("index", -1))

    if 0 <= index < 3:
        message_slots[index] = message

    return jsonify({"status": "ok", "messages": message_slots})

@app.route('/remove', methods=['POST'])
def remove_message():
    data = request.get_json()
    index = int(data.get("index", -1))

    if 0 <= index < 3:
        message_slots[index] = ""

    return jsonify({"status": "removed", "messages": message_slots})

@app.route('/clear', methods=['POST'])
def clear_all():
    for i in range(3):
        message_slots[i] = ""
    return jsonify({"status": "cleared"})

if __name__ == '__main__':
    app.run(debug=True)
