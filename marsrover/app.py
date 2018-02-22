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
    return render_template('marsrover.html', image=image, date=date, earth_date=earth_date)


if __name__ == '__main__':
    app.run(debug=True)
