from flask import Flask,jsonify
from block import Block

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_FIRST'] = True

block1 = Block()

@app.route('/',methods=['GET'])

def route():

    return 'Blockchain Application'

@app.route('/mine',methods=['GET'])

def mine():
    previous_block = block1.prev_block()
    previous_proof = previous_block['proof']
    proof = block1.proof_of_work(previous_proof)
    previous_hash = block1.hash(previous_block)
    blocks = block1.block_creation(proof,previous_hash)

    response = {
        'alert!' : 'A BLOCK IS MINED',
        'index' : blocks['index'],
        'timestamp' : blocks['timestamp'],
        'proof' : blocks['proof'],
        'previous hash' : blocks['previous_hash']   
    }

    return jsonify(response), 200

@app.route('/valid',methods = ['GET'])

def valid():
    valid = block1.valid_chain(block1.chain_block)
    if(valid):
        response = {'alert!' : 'THE BLOCKCHAIN IS VALID'}
    else:
        response = {'alert!' : 'THE BLOCKCHAIN IS INVALID'}
    return jsonify(response), 200

@app.route('/get_chain',methods = ['GET'])

def display_chain():
    response = {
        'chain' : block1.chain_block,
        'length' : len(block1.chain_block),
    }
    return jsonify(response), 200

app.run(host = '127.0.0.1',port = 5000)