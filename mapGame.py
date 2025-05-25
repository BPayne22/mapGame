from flask import Flask, request, jsonify, render_template
from geopy.distance import geodesic

app = Flask(__name__)

# Define the goal location (latitude, longitude)
GOAL_LOCATION = (43.81468366, -111.78519198)  # Location: Somewhere inside the STC Building


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    
    if lat is None or lon is None:
        return jsonify({'status': 'error', 'message': 'Missing coordinates'}), 400
    
    print(f"Received location: {lat}, {lon}")
    
    player_location = (lat, lon)
    distance = geodesic(GOAL_LOCATION, player_location).meters
     
    print(f"Distance to goal: {distance:.2f} meters")
    
    if distance < 10:  # within 10 meters
        return jsonify({'status': 'victory'})
    else:
        return jsonify({'status': 'keep_going', 'distance': distance})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
