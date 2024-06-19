from flask import Flask, request, render_template
from reconcile import reconcile
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'csv_file' not in request.files or 'excel_file' not in request.files:
        return "No file part", 400

    csv_file = request.files['csv_file']
    excel_file = request.files['excel_file']

    discrepancies = reconcile(csv_file, excel_file)

    return render_template('results.html', tables=[discrepancies.to_html(classes='data', header="true")])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
