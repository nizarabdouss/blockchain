import datetime as d
import hashlib as h
import time as t

last_index: int
class Block:
    def __init__(self, index, timestamp, data, prevhash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.hash = self.hashblock()
    
    def hashblock (self):
        block_encryption=h.sha256() 
        data = str(self.index)+str(self.timestamp)+str(self.data)+str(self.prevhash)
        block_encryption.update(data.encode())
        return block_encryption.hexdigest()

    @staticmethod
    def genesisblock():
        return Block(0,d.datetime.now(),"genesis block transaction"," ")

    @staticmethod
    def newblock(lastblock):
        index = lastblock.index+1
        timestamp = d.datetime.now()
        hashblock = lastblock.hash
        data = "Transaction " +str(index)
        return Block(index,timestamp,data,hashblock)

blockchain = [Block.genesisblock()]
prevblock = blockchain[0]

timer = t.time()
for i in range (0,7):
    addblock = Block.newblock(prevblock)
    blockchain.append(addblock)
    prevblock =addblock

    print("Block ID #"+str(addblock.index))
    print("Timestamp: "+str(addblock.timestamp))
    print("Hash of the block: "+str(addblock.hash))
    print("Previous Block Hash: "+str(addblock.prevhash))
    last_index = addblock.index
    print("Data: "+str(addblock.data)+"\n")

end = t.time()
print(str(end - timer)+"\n")