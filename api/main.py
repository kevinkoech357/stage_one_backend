#!/usr/bin/env python3

from flask import Flask, request, jsonify
from datetime import datetime

# initializing app
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    github_file_url = 
    github_repo_url =


if __name__ == '__main__':
    app.run(debug=True)
