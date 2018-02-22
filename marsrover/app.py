from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/marsrover', methods=['GET', 'POST'])
def marsrover():
    date = request.form['date']
    r = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=' + date + '&api_key=G5y2M6Nxqx8ZO7E3Fr4sHOOzWTxmknVNYvOMJnZW')

    j_obj = r.json()
    image = j_obj['photos'][0]['img_src']
    earth_date = j_obj['photos'][0]['earth_date']
    launch_date = j_obj['photos']['rover']['launch_date']
    landing_date = j_obj['photos']['rover']['landing_date']
    camera = j_obj['photos'][0]['rover']['cameras']['full_name']
    status = j_obj['photos'][0]['rover']['status']
    rover = j_obj['photos'][0]['rover']['name']
    return render_template('marsrover.html', image=image, earth_date=earth_date, launch_date=launch_date, landing_date=landing_date, status=status, rover=rover)


if __name__ == '__main__':
    app.run(debug=True)
