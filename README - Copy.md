# Mini Blockchain (Python)

A minimal blockchain implementation built from scratch in Python to understand the core fundamentals of how blockchains work — blocks, hashing, and chain integrity — without any external libraries or frameworks.

## What it demonstrates

- **Block structure**: each block stores an index, timestamp, data, and a reference to the previous block's hash
- **Hashing (SHA-256)**: each block's hash is calculated from its own contents, so any change to the data changes the hash completely
- **Chain linking**: each block stores the hash of the block before it, creating a tamper-evident chain
- **Tamper detection**: a validity check walks the chain and confirms every block's hash is correct and every link to the previous block is intact

## How it works

​```
Block 0 (Genesis) → Block 1 → Block 2
   hash: abc...        hash: def...   hash: ghi...
                previous_hash: abc... previous_hash: def...
​```

## Example output

​```
Is blockchain valid? True

# after manually changing Block 1's data
Is blockchain valid after tampering? False
​```

## Run it

```bash
python block.py
```

## Why I built this

Alongside my Solidity/smart contract projects, I wanted to implement blockchain fundamentals from first principles — not just read about hashing and chain integrity, but write the code and watch tamper detection actually work. This was built purely as a learning exercise, not a production system.

## Possible next steps

- Add Proof-of-Work (mining with a difficulty target)
- Add a Merkle tree for multiple transactions per block