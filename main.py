#!/usr/bin/env python3

from flask import Flask, request, jsonify
from datetime import datetime, timedelta

# initializing app
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # setting parameters required
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    github_file_url = 'https://github.com/kevinkoech357/stage_one_backend/blob/main/api/main.py'
    github_repo_url = 'https://github.com/kevinkoech357/stage_one_backend'

    # setting day and time
    utc_time = datetime.utcnow()
    current_day = utc_time.strftime('%A')

    # validating if time is within +/- 2 minutes
    current_utc_time = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    time_difference = datetime.utcnow() - utc_time
    max_time_difference = timedelta(minutes=2)
    if abs(time_difference) > max_time_difference:
        return jsonify({'error': 'Time difference surpassed'})

    return jsonify({
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    })

if __name__ == '__main__':
    app.run(debug=True)
