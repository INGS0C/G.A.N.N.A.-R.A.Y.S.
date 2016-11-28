from random import randrange

hexdigits = '0123456789ABCDEF'

class NN:
    layer_one_node_list = []
    layer_two_node_list = []
    layer_three_node_list = []
    layer_output_node_list = []
    weight_values = ''

    def load_data(self):
        for node_index in range(50):
            current_node = []
            for weight_index in range(9):
                node_value = 0
                for digit in range(4):
                    value = (36*node_index) + (4*weight_index) + digit
                    node_value += hexdigits.index(self.weight_values[value]) * (16**(3-digit))
                current_node.append(node_value)
            self.layer_one_node_list.append(current_node)
        for node in range(50):
            for weight in range(9):
                self.layer_one_node_list[node][weight] /= (65535/2)
        print(len(self.layer_two_node_list))
        for node_index in range(100):
            current_node = []
            for weight_index in range(50):
                node_value = 0
                for digit in range(4):
                    value = (200*node_index) + (4*weight_index) + digit + 450*4
                    node_value += hexdigits.index(self.weight_values[value]) * (16**(3-digit))
                current_node.append(node_value)
            self.layer_two_node_list.append(current_node)
        for node in range(100):
            for weight in range(50):
                self.layer_two_node_list[node][weight] /= (65535/2)
        for node_index in range(50):
            current_node = []
            for weight_index in range(100):
                node_value = 0
                for digit in range(4):
                    value = (200*node_index) + (4*weight_index) + digit + 5450*4
                    node_value += hexdigits.index(self.weight_values[value]) * (16**(3-digit))
                current_node.append(node_value)
            self.layer_three_node_list.append(current_node)
        for node in range(50):
            for weight in range(100):
                self.layer_three_node_list[node][weight] /= (65535/2)
        for node_index in range(9):
            current_node = []
            for weight_index in range(50):
                node_value = 0
                for digit in range(4):
                    value = (200*node_index) + (4*weight_index) + digit + 10450*4
                    node_value += hexdigits.index(self.weight_values[value]) * (16**(3-digit))
                current_node.append(node_value)
            self.layer_output_node_list.append(current_node)
        for node in range(9):
            for weight in range(50):
                self.layer_output_node_list[node][weight] /= (65535/2)

    def __init__(self, network_index):
        read_file = open('NNData.txt', 'r')
        NN_contents = read_file.read()
        read_file.close()
        NN_raw_data_list = NN_contents.split()

        self.weight_values = NN_raw_data_list[network_index]

def generateNetworks():
    file_NN = open('NNData.txt', 'w')

    for line in range(500):
        print('Percent: ', line//5)
        random_NNValues = ''
        for index in range(43600):
            char = hexdigits[randrange(0, 15)]
            random_NNValues += char
        file_NN.write(random_NNValues + '\n')

    file_NN.close()

def buildNetwork(network_index):
    network_one = NN(network_index)
    network_one.load_data()
    print(network_one.layer_output_node_list)
