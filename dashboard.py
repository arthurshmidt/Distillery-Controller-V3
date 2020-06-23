from flask import Flask, render_template
import src.control_test as C
import ShmidtSpirits as SS

app = Flask(__name__)

@app.route('/')
def index():
    supply_stpt_data = {
        'supply_stpt': C.test_print()
    }
    return render_template('index.html',**supply_stpt_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
