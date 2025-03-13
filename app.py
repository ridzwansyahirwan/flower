from flask import Flask, render_template

app = Flask(__name__)


# Route to serve the index.html
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html file


if __name__ == '__main__':
    app.run(debug=True)  # Start the development server
