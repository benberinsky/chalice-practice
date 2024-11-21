from chalice import Chalice

app = Chalice(app_name='sample-api')


@app.route('/')
def index():
    return {'Name': 'Ben Berinsky'}
