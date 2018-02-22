#!/usr/local/bin/python

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import requests

app = Flask(__name__)

# home page route


@app.route('/')
def index():
    return render_template('index.html')

# marsrover page calls the api using flask's requests


@app.route('/marsrover', methods=['GET', 'POST'])
def marsrover():
    date = request.form['date']
    r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=' + date + '&api_key=G5y2M6Nxqx8ZO7E3Fr4sHOOzWTxmknVNYvOMJnZW')
    j_obj = r.json()
    photos = j_obj['photos']

    # Should api lack details such as a day without photo or a future untaken one
    # This handles the error by simply redirecting the user to /empty
    if photos != []:
        image = j_obj['photos'][0]['img_src']
        earth_date = j_obj['photos'][0]['earth_date']
        launch_date = j_obj['photos'][0]['rover']['launch_date']
        landing_date = j_obj['photos'][0]['rover']['landing_date']
        camera = j_obj['photos'][0]['rover']['cameras'][0]['full_name']
        status = j_obj['photos'][0]['rover']['status']
        rover = j_obj['photos'][0]['rover']['name']
        return render_template('marsrover.html', image=image, earth_date=earth_date, launch_date=launch_date, landing_date=landing_date, status=status, rover=rover, camera=camera)
    else:
        return redirect(url_for('empty'))

# page redirected where api is empty


@app.route('/empty')
def empty():
    return render_template('empty.html')


if __name__ == '__main__':
    app.run(debug=True)
