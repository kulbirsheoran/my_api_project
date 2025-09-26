from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/categories')
def categories():
    return jsonify({
        "categories": [
            {"name": "फल", "icon": "🍎", "color": "#FF0000"},
            {"name": "जानवर", "icon": "🐶", "color": "#A52A2A"},
            {"name": "रंग", "icon": "🌈", "color": "#800080"},
            {"name": "सब्जी", "icon": "🥕", "color": "#008000"}
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
