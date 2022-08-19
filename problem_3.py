import sys

encode_val = {}


# A Huffman Tree Node
class Node:
    def __init__(self, freq, letter, left=None, right=None):
        self.freq = freq
        self.letter = letter
        self.left = left
        self.right = right
        self.direction = ''


def print_nodes(node, val=''):
    global encode_val
    # huffman code for current node
    new_val = val + str(node.direction)
    # if node is not an edge node
    # then traverse inside it
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)
    # if node is edge node then display its huffman code
    if not node.left and not node.right:
        print(f"{node.letter} -> {new_val}")
        encode_val[node.letter] = new_val


def frequency_calc(data):
    if data is None or data == "" or type(data) is not str:
        return None
    data = "".join(data.split())
    freq_holder_dict = {}
    for char in data:
        if char in freq_holder_dict:
            freq_holder_dict[char] += 1
        else:
            freq_holder_dict[char] = 1
    ordered_dict = dict(sorted(freq_holder_dict.items(), key=lambda v: v[1]))
    print(ordered_dict)
    return ordered_dict


def huffman_tree_nodes_builder(letter_freq_dict):
    nodes = []
    for key in letter_freq_dict:
        nodes.append(Node(letter_freq_dict[key], key))
    return nodes


def huffman_tree_nodes(nodes):
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        # pick two smallest nodes from the nodes
        left_node = nodes[0]
        right_node = nodes[1]

        # assign direction of 0 to left node and direction of 1 to right node
        left_node.direction = 0
        right_node.direction = 1

        # combine the nodes
        combined_node = Node(
            left_node.freq + right_node.freq, left_node.letter + right_node.letter, left_node, right_node)
        #   remove the combined node
        nodes.remove(left_node)
        nodes.remove(right_node)
        nodes.append(combined_node)
    return nodes[0]


def get_encoded_record(data):
    global encode_val
    if data is None or data == "" or type(data) is not str:
        return None
    data = "".join(data.split())
    encoded_string = ""
    for char in data:
        encoded_string += encode_val[char]
    return encoded_string


def huffman_encoding(data):
    if type(data) is not str or data is None or data == "":
        return "Invalid Entry", ""
    frequency_ordered_dict = frequency_calc(data)
    if frequency_ordered_dict is None:
        return "Invalid Entry"
    nodes = huffman_tree_nodes_builder(frequency_ordered_dict)
    huffman_getter = huffman_tree_nodes(nodes)
    print_nodes(huffman_getter)
    return get_encoded_record(data), huffman_getter


def huffman_decoding(data, tree):
    huffman_tree = tree
    decoded_output = []
    for char in data:
        if char == "0":
            tree = tree.left
        elif char == "1":
            tree = tree.right
        try:
            if tree.left.letter is None and tree.right.letter is None:
                pass
        except AttributeError:
            decoded_output.append(tree.letter)
            tree = huffman_tree
    string = ''.join([str(item) for item in decoded_output])
    return string


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
    print("The content of the encoded data is: {}\n".format(decoded_data))


test1_text_code, test1_text_code_tree = huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")

print(test1_text_code)   #return 1010101010101000100100111111111111111000000010101010101

decoded_text1 = huffman_decoding(test1_text_code, test1_text_code_tree)

print(decoded_text1) #return AAAAAAABBBCCCCCCCDDEEEEEE

test2_text_code, test2_text_code_tree = huffman_encoding("")

print(test2_text_code) #return Invalid Entry

test3_text_code, test3_text_code_tree = huffman_encoding("JJJJJJJJGGGGG")

print(test3_text_code) #return 1111111100000

decoded_text3 = huffman_decoding(test3_text_code, test3_text_code_tree)

print(decoded_text3) #return JJJJJJJJGGGGG