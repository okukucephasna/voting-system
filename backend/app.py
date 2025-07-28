from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

# Serve React frontend
@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

# Optional: Handle client-side routing (React Router)
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

# Example API route
@app.route("/api/hello")
def hello():
    return {"message": "Hello from Flask!"}

if __name__ == "__main__":
    app.run(debug=True)
