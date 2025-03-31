from flask import Flask, jsonify, request, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

# Homepage with an epic space mission dashboard
@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>🌌 Flask DevOps Mission Control 🚀</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background: #000;
                overflow: hidden;
                font-family: 'Orbitron', sans-serif;
            }

            @keyframes moveStars {
                from { transform: translateY(0); }
                to { transform: translateY(-100%); }
            }

            /* Starfield Effect */
            .starfield {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle, #000, #111);
                overflow: hidden;
                z-index: -1;
            }

            .star {
                position: absolute;
                background: #ffffff;
                border-radius: 50%;
                opacity: 0.8;
                animation: moveStars 50s linear infinite;
            }

            @keyframes blink {
                0%, 100% { opacity: 0.8; }
                50% { opacity: 1; }
            }

            /* Rocket Animation */
            .rocket {
                width: 60px;
                animation: rocketLaunch 2s infinite;
                transition: transform 0.5s ease;
            }

            @keyframes rocketLaunch {
                0% { transform: translateY(0); }
                50% { transform: translateY(-20px); }
                100% { transform: translateY(0); }
            }

            .rocket:hover {
                transform: translateY(-50px) scale(1.2);
            }

            /* Dashboard Styling */
            .container {
                text-align: center;
                padding: 50px;
                color: #fff;
            }

            h1 {
                font-size: 60px;
                color: #00bcd4;
                text-shadow: 0 0 30px #00bcd4, 0 0 50px #00bcd4, 0 0 70px #00bcd4;
            }

            .button {
                background: #00bcd4;
                padding: 15px 30px;
                border-radius: 12px;
                color: white;
                font-size: 20px;
                text-decoration: none;
                transition: background 0.3s, transform 0.3s;
            }

            .button:hover {
                background: #ff4081;
                transform: scale(1.1);
            }

            .status {
                font-size: 24px;
                margin: 20px 0;
                color: #ffeb3b;
            }

            .gauge {
                width: 200px;
                height: 200px;
                background: conic-gradient(#00ffcc 0%, #ff0000 100%);
                border-radius: 50%;
                margin: 20px auto;
                transition: background 1s ease;
            }

        </style>
    </head>
    <body>
        <div class="starfield">
            {% for i in range(150) %}
                <div class="star" style="top: {{ random.randint(0, 100) }}%; left: {{ random.randint(0, 100) }}%; width: {{ random.randint(2, 5) }}px; height: {{ random.randint(2, 5) }}px; animation-delay: {{ random.randint(0, 10) }}s;"></div>
            {% endfor %}
        </div>

        <div class="container">
            <h1>🚀 Flask DevOps Mission Control 🌍</h1>
            <a href="/api/status" class="button">🛰️ Check Server Status</a>
            <br><br>
            <a href="/api/greet?name=Commander" class="button">👨‍🚀 Send Greetings!</a>

            <div class="status" id="statusMessage">Awaiting Launch...</div>
            <div class="gauge" id="gauge"></div>
        </div>

        <script>
            document.querySelector('.button').addEventListener('click', function() {
                const statusElement = document.getElementById('statusMessage');
                const gauge = document.getElementById('gauge');
                statusElement.textContent = "🚀 Launching... Hold Tight!";
                gauge.style.background = "conic-gradient(#00ffcc 0%, #ff0000 0%)";

                setTimeout(() => {
                    statusElement.textContent = "✅ All Systems Go!";
                    gauge.style.background = "conic-gradient(#00ffcc 75%, #ff0000 25%)";
                }, 3000);
            });
        </script>
    </body>
    </html>
    """, random=random)  # ✅ Pass 'random' to the template

# Dynamic status API with real-time load gauge
@app.route('/api/status', methods=['GET'])
def status():
    server_load = random.randint(0, 100)  # Simulating server load
    return jsonify({
        "status": "active",
        "server_load": f"{server_load}%",
        "message": "Flask app is operational in orbit! 🚀",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# Greet API with space-themed personalization
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Explorer')
    return jsonify({
        "message": f"👋 Greetings, {name}! Welcome to the Interstellar Flask API!",
        "time": datetime.now().strftime("%H:%M:%S")
    })

# Custom 404 error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "⚠️ Error 404: This part of the galaxy doesn't exist!"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
