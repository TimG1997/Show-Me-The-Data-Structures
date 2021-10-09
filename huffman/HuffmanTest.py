import unittest
from Huffman import huffman_encoding, huffman_decoding, Node


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

    def test_edge_case_encoding_string_is_empty_or_None(self):
        self.assertRaises(ValueError, huffman_encoding, '')
        self.assertRaises(ValueError, huffman_encoding, None)

    def test_edge_case_decoding_string_is_empty_or_None(self):
        tree = Node()

        self.assertRaises(ValueError, huffman_decoding, '', tree)
        self.assertRaises(ValueError, huffman_decoding, None, tree)

    def test_edge_case_decoding_tree_is_None(self):
        self.assertRaises(ValueError, huffman_decoding, "ABC", None)

    def test_edge_case_encoding_and_decoding_only_repeating_character(self):
        data_to_encode = 'AAA'
        encoded_data, tree = huffman_encoding(data_to_encode)

        self.assertEqual('000', encoded_data)
        decoded_data = huffman_decoding(encoded_data, tree)
        self.assertEqual(data_to_encode, decoded_data)