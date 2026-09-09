import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_block = Block(new_index, datetime.datetime.now(), new_data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

my_chain = Blockchain()
my_chain.add_block("Alice pays Bob 5 coins")
my_chain.add_block("Bob pays Charlie 2 coins")

for block in my_chain.chain:
    print(f"Index: {block.index}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print("-" * 40)

print("Is blockchain valid?", my_chain.is_chain_valid())

# Now let's tamper with block 1
my_chain.chain[1].data = "Alice pays Bob 500 coins"

print("Is blockchain valid after tampering?", my_chain.is_chain_valid())