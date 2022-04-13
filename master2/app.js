
const crypto = require("crypto"), SHA256 = message => crypto.createHash('sha256').update(message).digest('hex');

class Block{
    constructor(timestamp='', data = []) {
        this.timestamp = timestamp;
        this.data = data;
        this.hash = this.getHash();
        this.prevHash = '';
        this.nonce = 0;
    }

    getHash() {
        return SHA256(this.prevHash + this.timestamp + JSON.stringify(this.data));
    }

    mineDifficulty(difficulty) {
        while(!this.hash.startsWith(Array(difficulty + 1).join("0"))) {
            is.nonce++;
            is.hash = this.getHash();
        }
    }
}

class Blockchain{
    constructor() {
        this.chain = [new Block(Date.now().toString())];
        this.difficulty = 1
    }

    getLastBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock() {
        block.prevHash = this.getLastBlock().hash;

        block.hash = block.getHash;
        block.mine(this.difficulty);
        this.chain.push(Object.freeze(block));

    }

    isValid(blockchain = this) {
        // Iterate over the chain, we need to set i to 1 because there are nothing before the genesis block, so we start at the second block.
        for (let i = 1; i < blockchain.chain.length; i++) {
            const currentBlock = blockchain.chain[i];
            const prevBlock = blockchain.chain[i-1];

            // Check validation
            if (currentBlock.hash !== currentBlock.getHash() || prevBlock.hash !== currentBlock.prevHash) {
                return false;
            }
        }

        return true;
    }
}

module.exports = {Block, Blockchain};