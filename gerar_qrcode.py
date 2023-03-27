from io import BytesIO
import qrcode
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

def wifi_qrcode_data(ssid, password):
    return f"WIFI:T:WPA;S:{ssid};P:{password};;"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qrcode', methods=['POST'])
def gerar_qrcode():
    ssid = request.form['ssid']
    password = request.form['password']

    wifi_data = wifi_qrcode_data(ssid, password)

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_buffer = BytesIO()
    img.save(img_buffer, 'PNG')
    img_buffer.seek(0)

    response = make_response(img_buffer.getvalue())
    response.headers['Content-Type'] = 'image/png'

    return response

if __name__ == '__main__':
    app.run()
