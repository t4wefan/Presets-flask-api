from flask import Flask, request, jsonify
from make_preset import make_preset
from read_preset import read_preset
import time

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

    returned_preset = make_preset(preset, nickname, from_arg)
    second_pass = returned_preset
    #read_time = time.strftime("%Y-%m-%d %H:%M:%S")
    status = 'created'
    second_pass['status'] = status

    result = second_pass


    return jsonify(result)

@app.route('/read', methods=['GET'])
def read_from_exists():
    id = request.args.get('id')

    # check must args
    if not id:
        error = {'error': 'Missing required parameter(s)', 
        'status': "error", }
        return jsonify(error), 400


    returned_preset = read_preset(id)
    second_pass = returned_preset
    read_time = time.strftime("%Y-%m-%d %H:%M:%S")
    second_pass['last_read_time'] = read_time

    result = second_pass


    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
