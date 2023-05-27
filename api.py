from flask import Flask, request, jsonify
from make_preset import make_preset

app = Flask(__name__)

@app.route('/create', methods=['GET'])
def create_preset():
    preset = request.args.get('preset')
    from_arg = request.args.get('from')
    nickname = request.args.get('nickname')
    data = None

    # check must args
    if not preset or not nickname:
        error = {'error': 'Missing required parameter(s)', 
        'status': "error", }
        return jsonify(error), 400

    # set default anonymous
    if not from_arg:
        from_arg = 'anonymous'
    if from_arg == '':
        from_arg = 'anonymous' 

    result = make_preset(preset, nickname, from_arg)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
