from queue import PriorityQueue
import sys
import bisect


class Node:

    def __init__(self):
        self.character = ''
        self.frequency = 0
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_encoding(data):
    character_frequencies = get_character_frequencies(data)
    queue = create_asc_freq_queue(character_frequencies)
    root_node = build_huffman_tree(queue)

    huffman_dict = {}
    fill_huffman_dict(root_node, huffman_dict)

    encoded_str = ""

    for character in data:
        encoded_str += huffman_dict[character]

    return [encoded_str, root_node]


def build_huffman_tree(queue):
    while queue.qsize() > 1:
        new_node = Node()

        if (queue.qsize() <= 1):
            break

        _, left = queue.get()
        _, right = queue.get()

        new_node.left = left
        new_node.right = right
        new_node.frequency = left.frequency + right.frequency

        queue.put((new_node.frequency, new_node))
    _, root_node = queue.get()
    return root_node


def fill_huffman_dict(node, huffman_dict, code=""):
    if node.left is None and node.right is None:
        huffman_dict[node.character] = code
    else:
        fill_huffman_dict(node.left, huffman_dict, code + "0")
        fill_huffman_dict(node.right, huffman_dict, code + "1")


def create_asc_freq_queue(character_frequencies):
    queue = PriorityQueue()
    for character, frequency in character_frequencies.items():
        node = Node()
        node.character = character
        node.frequency = frequency
        queue.put((frequency, node))
    return queue


def get_character_frequencies(data):
    character_frequencies = {}
    for character in data:
        if character not in character_frequencies:
            character_frequencies[character] = 1
        else:
            character_frequencies[character] = character_frequencies[character] + 1
    return character_frequencies


def huffman_decoding(data, tree):
    decoded_str = ""

    curr_node = tree

    for bit in data:
        if curr_node.is_leaf():
            decoded_str += curr_node.character
            curr_node = tree

        if bit == "0":
            curr_node = curr_node.left

        if bit == "1":
            curr_node = curr_node.right

    decoded_str += curr_node.character

    return decoded_str


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
