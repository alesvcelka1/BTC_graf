from flask import Flask, render_template_string
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Get Bitcoin data from Yahoo Finance
    btc_data = si.get_data("BTC-USD")

    # Plot the closing prices
    plt.figure(figsize=(10, 5))
    plt.plot(btc_data.index, btc_data['close'], label='BTC-USD')
    plt.title('Bitcoin Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.legend()
    plt.grid(True)

    # Save the plot to a PNG image in memory
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Render the plot in an HTML template
    return render_template_string('''
        <h1>Bitcoin Closing Prices</h1>
        <img src="data:image/png;base64,{{ plot_url }}">
    ''', plot_url=plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)