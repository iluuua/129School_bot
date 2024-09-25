from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Game data
users = {
    "hamster1": {"level": 1, "power": 1, "xp": 0},
    "hamster2": {"level": 1, "power": 1, "xp": 0},
}
base_power = 10
game_running = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_game():
    global game_running
    game_running = True
    return jsonify({"success": True})


@app.route('/stop', methods=['POST'])
def stop_game():
    global game_running
    game_running = False
    return jsonify({"success": True})


@app.route('/status', methods=['GET'])
def status():
    return jsonify({"game_running": game_running, "users": users})


@app.route('/tap', methods=['POST'])
def tap():
    global users
    for hamster in users:
        users[hamster]["xp"] += base_power * users[hamster]["level"]
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
