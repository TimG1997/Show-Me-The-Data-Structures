import hashlib
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data.encode('utf-8')
        hashlib.sha256().update(self.data)
        self.previous_hash = previous_hash


class Blockchain:

    def __init__(self):
        self.first_block = None
        self.last_block = None
        self.size = 0

    def append_block(self, data):
        if data is None:
            return

        new_block = Block(time.time(), data, None)

        if self.first_block is None:
            self.last_block = new_block
        else:
            previous_hash = self.last_block.data
            new_block.previous_hash = previous_hash
            self.last_block = new_block

        self.size += 1
