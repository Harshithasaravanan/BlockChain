import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self):
        self.chain_block = []
        self.block_creation(proof=1, prev_hash='0')

    def block_creation(self,proof,prev_hash):
        block = {
            'index' : len(self.chain_block) + 1,
            'timestamp' : str(datetime.now()),
            'proof' : proof,
            'previous_hash' : prev_hash
        }
        self.chain_block.append(block)
        return block
    
    def prev_block(self):
        return self.chain_block[-1]

    def proof_of_work(self,prev_proof):
        new_proof = 1
        chk_proof = False

        while chk_proof is False:
            hash_op = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()

            if(hash_op[:5]=='00000'):
                chk_proof = True
            else:
                new_proof+=1
        return new_proof
    
    def hash(self,block):
        enc_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(enc_block).hexdigest()
    
    def valid_chain(self,chain_block):
        prev_block = chain_block[0]
        block_index = 1

        while(block_index < len(chain_block)):

            block = chain_block[block_index]
            if(block['prev_block'] != self.hash(prev_block)):
                return False
            
            prev_proof = prev_block['proof']
            proof = block['proof']
            hash_op = hashlib.sha256(str(proof**2 - prev_proof**2).encode()).hexdigest()

            if(hash_op[:5] != '00000'):
                return False
            prev_block = block
            block_index += 1
        return True