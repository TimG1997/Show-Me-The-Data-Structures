import unittest
from Huffman import huffman_encoding, huffman_decoding


class HuffmanTest(unittest.TestCase):

    def test_encoding(self):
        data_to_encode = 'AAAAAAABBBCCCCCCCDDEEEEEE'
        encoded_data, _ = huffman_encoding(data_to_encode)

        self.assertEqual('1010101010101000100100111111111111111000000010101010101', encoded_data)

    def test_decoding(self):
        data_to_encode = 'AAAAAAABBBCCCCCCCDDEEEEEE'
        encoded_data, tree = huffman_encoding(data_to_encode)

        data_to_decode = '1010101010101000100100111111111111111000000010101010101'
        decoded_data = huffman_decoding(data_to_decode, tree)

        self.assertEqual(data_to_encode, decoded_data)