from flask import Flask, make_response, jsonify

app = Flask(__name__)

stupidity = 13

@app.route('/up')
def up():
    global stupidity
    stupidity += 1

    response = make_response({'stupidity': stupidity})
    # FIXME
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/get')
def get():
    response = make_response({'stupidity': stupidity})
    # FIXME
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/reset')
def reset():
    global stupidity
    stupidity = 13

    response = make_response({'stupidity': stupidity})
    # FIXME
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run()
