from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            static_folder='.',
            template_folder='.')

# Ruta principal - servir index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Servir archivos CSS
@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory('css', filename)

# Servir archivos JS (si los hay)
@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory('js', filename)

# Servir imágenes (si las hay)
@app.route('/img/<path:filename>')
def img(filename):
    return send_from_directory('img', filename)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

# API endpoints de ejemplo para futuras funcionalidades
@app.route('/api/health')
def health():
    return {'status': 'ok', 'message': 'MiAdelanto API funcionando correctamente'}

if __name__ == '__main__':
    # En desarrollo, usar debug=True
    # En producción, cambiar a debug=False
    app.run(debug=True, host='0.0.0.0', port=5000)
