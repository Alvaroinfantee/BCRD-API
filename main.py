from flask import Flask, jsonify
import requests
from lxml import html

app = Flask(__name__)

BASE_URL = 'https://www.bancentral.gov.do/'

def fetch_data(xpath):
    response = requests.get(BASE_URL)
    tree = html.fromstring(response.content)
    data = tree.xpath(xpath)
    return data[0].text if data else 'N/A'

@app.route('/fecha')
def get_fecha():
    data = fetch_data('//*[@id="variables-economicas"]/div[1]/div/table[2]/thead/tr/th/a/small/span')
    return jsonify({'Fecha': data})

@app.route('/inflacion/interanual')
def get_inflacion_interanual():
    data = fetch_data('//*[@id="variables-economicas"]/div[1]/div/table[2]/tbody/tr[1]/td[2]').replace('%', '')
    return jsonify({'Inflacion Interanual': data})

@app.route('/inflacion/acumulada')
def get_inflacion_acumulada():
    data = fetch_data('//*[@id="variables-economicas"]/div[1]/div/table[2]/tbody/tr[2]/td[2]').replace('%', '')
    return jsonify({'Inflacion Acumulada': data})

@app.route('/inflacion/mensual')
def get_inflacion_mensual():
    data = fetch_data('//*[@id="variables-economicas"]/div[1]/div/table[2]/tbody/tr[3]/td[2]').replace('%', '')
    return jsonify({'Inflacion Mensual': data})

@app.route('/inflacion-subyacente/interanual')
def get_inflacion_subyacente_interanual():
    data = fetch_data('//*[@id="variables-economicas"]/div[1]/div/table[3]/tbody/tr[1]/td[2]').replace('%', '')
    return jsonify({'Inflacion Subyacente Interanual': data})

@app.route('/inflacion-subyacente/acumulada')
def get_inflacion_subyacente_acumulada():
    data = fetch_data('//*[@id="variables-economicas"]/div[1]/div/table[3]/tbody/tr[2]/td[2]').replace('%', '')
    return jsonify({'Inflacion Subyacente Acumulada': data})

@app.route('/inflacion-subyacente/mensual')
def get_inflacion_subyacente_mensual():
    data = fetch_data('//*[@id="variables-economicas"]/div[1]/div/table[3]/tbody/tr[3]/td[2]').replace('%', '')
    return jsonify({'Inflacion Subyacente Mensual': data})

@app.route('/tpm')
def get_tpm():
    data = fetch_data('//*[@id="variables-economicas"]/div[2]/div/table[1]/tbody/tr/td/h5')
    return jsonify({'TPM': data})

@app.route('/tasa-interes-promedio-ponderado/interbancario')
def get_tasa_interes_promedio_ponderado_interbancario():
    data = fetch_data('//*[@id="variables-economicas"]/div[2]/div/table[2]/tbody/tr[1]/td[2]')
    return jsonify({'Tasa Interes Promedio Ponderado Interbancario': data})

@app.route('/tasa-interes-promedio-ponderado/activa-bm')
def get_tasa_interes_promedio_ponderado_activa_bm():
    data = fetch_data('//*[@id="variables-economicas"]/div[2]/div/table[2]/tbody/tr[2]/td[2]')
    return jsonify({'Tasa Interes Promedio Ponderado Activa B.M.': data})

@app.route('/tasa-interes-promedio-ponderado/pasiva-bm')
def get_tasa_interes_promedio_ponderado_pasiva_bm():
    data = fetch_data('//*[@id="variables-economicas"]/div[2]/div/table[2]/tbody/tr[3]/td[2]')
    return jsonify({'Tasa Interes Promedio Ponderado Pasiva B.M.': data})

@app.route('/prestamos-privados/variacion-porcentual-interanual-mon-nacional')
def get_prestamos_privados_variacion_porcentual_interanual_mon_nacional():
    data = fetch_data('//*[@id="variables-economicas"]/div[2]/div/table[3]/tbody/tr[1]/td[2]').replace('%', '')
    return jsonify({'Prestamos Privados Variacion % Interanual Mon. Nacional': data})

@app.route('/prestamos-privados/variacion-porcentual-interanual-total')
def get_prestamos_privados_variacion_porcentual_interanual_total():
    data = fetch_data('//*[@id="variables-economicas"]/div[2]/div/table[3]/tbody/tr[2]/td[2]').replace('%', '')
    return jsonify({'Prestamos Privados Variacion % Interanual Total': data})

@app.route('/sector-externo/tasa-cambio-compra')
def get_tasa_cambio_compra():
    data = fetch_data('//*[@id="variables-economicas"]/div[4]/div/table[1]/tbody/tr/td[1]/h5')
    return jsonify({'Tasa Cambio Compra': data})

@app.route('/sector-externo/tasa-cambio-venta')
def get_tasa_cambio_venta():
    data = fetch_data('//*[@id="variables-economicas"]/div[4]/div/table[1]/tbody/tr/td[2]/h5')
    return jsonify({'Tasa Cambio Venta': data})

if __name__ == '__main__':
    app.run(debug=True) 
