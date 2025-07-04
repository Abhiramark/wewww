from flask import Flask, request, jsonify
import swisseph as swe
import datetime

app = Flask(__name__)

@app.route('/render-api', methods=['POST'])
def calculate_grahanila():
    data = request.json
    name = data['name']
    dob = data['dob']  # format: YYYY-MM-DD
    tob = data['tob']  # format: HH:MM
    location = data['location']  # (not used for now)

    dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60)

    planets = ['Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', 'Venus', 'Saturn']
    results = []

    for i, name in enumerate(planets):
        pos, _ = swe.calc_ut(jd, i)
        results.append(f"{name}: {round(pos[0], 2)}°")

    return jsonify({"grahanila": "<br>".join(results)})

if __name__ == '__main__':
    app.run(debug=True)
