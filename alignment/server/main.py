import json
import pathlib
from flask import Flask, make_response, jsonify

app = Flask(__name__)

def read():
    return json.loads(pathlib.Path('./result.json').read_text())

def write(result):
    return pathlib.Path('./result.json').write_text(
        json.dumps(result)
    )

@app.route('/up/<first_metric>/<second_metric>')
def up(first_metric, second_metric):
    if first_metric not in ['lawful', 'stupid', 'chaotic', 'true']:
        abort(400)
    if second_metric not in ['good', 'stupid', 'evil']:
        abort(400)
    if first_metric == 'stupid' and second_metric == 'stupid':
        # "Stupid Stupid" corresponds to "True Stupid"
        first_metric = 'true'

    so_far = read()
    so_far[f'{first_metric}_{second_metric}'] += 1
    write(so_far)

    return so_far

@app.route('/up/mystical')
def up_mystical():
    so_far = read()
    so_far['mystical'] += 1
    write(so_far)

    return so_far

@app.route('/get')
def get():
    response = make_response(read())
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8000'
    return response

@app.route('/reset')
def reset():
    base_result = {
      "chaotic_evil": 0,
      "chaotic_good": 0,
      "chaotic_stupid": 0,
      "lawful_evil": 0,
      "lawful_good": 0,
      "lawful_stupid": 0,
      "mystical": 0,
      "stupid_evil": 0,
      "stupid_good": 0,
      "true_stupid": 0,
    }
    write(base_result)

    return base_result

if __name__ == '__main__':
    reset()
    app.run()
