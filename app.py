

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/get-image-url', methods=['GET'])
def redirect_to_image():
    image_url = "https://ezhil65.blob.core.windows.net/sample/graph.jpg?sp=racw&st=2025-06-17T07:37:36Z&se=2025-06-19T15:37:36Z&sv=2024-11-04&sr=b&sig=f07XhFpg9v0zNkr5NZ7w%2BMjfxdscJdZjnJ5WQDxofUM%3D"
    return redirect(image_url, code=302)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or default to 5000 locally
    app.run(host='0.0.0.0', port=port, debug=True)

