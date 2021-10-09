import unittest

from Blockchain import Blockchain

class BlockchainTest(unittest.TestCase):

    def test_append_block(self):

        blockchain = Blockchain()

        blockchain.append_block("first block")
        blockchain.append_block("second block")
        blockchain.append_block("third block")

        self.assertEqual(3, blockchain.size)