import hashlib
import json

class BlockData:
    def __init__(self, amount):
        self.amount = amount

class Block:
    def __init__(self, index, timestamp, data, previousHash = ''):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha224(str(self.index) + self.previousHash + self.timestamp + json.dumps(self.data.__dict__)).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "12/01/2017", BlockData(0))

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, newBlock):
        newBlock.previousHash = self.get_latest_block().hash
        newBlock.hash = newBlock.calculate_hash()
        self.chain.append(newBlock)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previousHash != previous_block.hash:
                return False

        return True

pyCoin = BlockChain()
pyCoin.add_block(Block(1, "12/06/2017", BlockData(4)))
pyCoin.add_block(Block(2, "12/12/2017", BlockData(8)))

# print pyCoin.get_latest_block().data.__dict__
print 'Is Chain Valid?? ' + str(pyCoin.is_chain_valid())

print 'Changing a block...'
pyCoin.chain[1].data = BlockData(100)

print 'Is Chain Valid?? ' + str(pyCoin.is_chain_valid())
