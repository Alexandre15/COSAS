from flask import Flask, send_file
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get-csv')
def get_csv():
    # Altere o caminho para o seu arquivo CSV
    csv_file_path = os.path.join(os.getcwd(), './data.csv')
    return send_file(csv_file_path, mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)