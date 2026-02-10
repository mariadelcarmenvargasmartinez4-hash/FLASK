from flask import Flask, render_template, request
import requests

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)

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

        headers = {
            'User-Agent': 'FlaskAppEducativo'
        }

        respuesta = requests.get(url, params=parametros, headers=headers)
        datos = respuesta.json()

        if datos:
            lat = datos[0]['lat']
            lon = datos[0]['lon']
            nombre = datos[0]['display_name']
            return render_template('map.html', lat=lat, lon=lon, nombre=nombre)
        else:
            return render_template('index.html', error="Lugar no encontrado")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
