

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lugar = request.form['lugar']

        url = "https://nominatim.openstreetmap.org/search"
        parametros = {
            'q': lugar,
            'format': 'json',
            'limit': 1
        }
