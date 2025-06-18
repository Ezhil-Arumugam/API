from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/', methods=['GET']) 
def redirect_to_image():
    image_url = "https://ezhil65.blob.core.windows.net/sample/graph.jpg?sp=r&st=2025-06-18T06:08:23Z&se=2025-06-25T14:08:23Z&sv=2024-11-04&sr=b&sig=vgLM5DrcJ82FUcvUcnSRFlvj%2F9c8%2F6Av0XhYhHylVDA%3D"
    return redirect(image_url, code=302)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # default Render port fallback
    app.run(host='0.0.0.0', port=port, debug=True)
