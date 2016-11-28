from random import randrange
import MathFunctions as mfs


class Network:
    def run(self, input_matrix):
        hl_1_o = mfs.matrixMult(input_matrix.read(), self.hl_1.read())
        for index in range(len(hl_1_o[0])):
            return_sigma = mfs.sigma(hl_1_o[0][index])

        hl_2_o = mfs.matrixMult(hl_1_o, self.hl_2.read())
        for index in range(len(hl_2_o[0])):
            return_sigma = mfs.sigma(hl_2_o[0][index])
            if return_sigma >= .7:
                hl_2_o[0][index] = return_sigma
            else:
                hl_2_o[0][index] = 0

        ol_o = mfs.matrixMult(hl_2_o, self.ol.read())
        return ol_o[0][0]

    def __init__(self):

        self.hl_1 = mfs.Matrix(rows=2, columns=10)
        self.hl_2 = mfs.Matrix(rows=10, columns=10)
        self.ol = mfs.Matrix(rows=10, columns=1)

        self.hl_1.randomize(0, 1, decimal=100)
        self.hl_2.randomize(0, 1, decimal=100)
        self.ol.randomize(0, 1, decimal=100)


def mergeMatrices(matrix_one, matrix_two):
    return_matrix = [[0 for _ in range(len(matrix_one[0]))] for _ in range(len(matrix_one))]
    for r in range(len(matrix_one)):
        for c in range(len(matrix_one[0])):
            command = randrange(1, 101)
            if command <= 17:
                return_matrix[r][c] = matrix_one[r][c]
            elif command <= 34:
                return_matrix[r][c] = matrix_two[r][c]
            elif command <= 67:
                return_matrix[r][c] = (matrix_one[r][c] + matrix_two[r][c])/2
            elif command <= 100:
                return_matrix[r][c] = randrange(0, 200)/100
    return return_matrix


def breedNetworks(nets):
    original_nets = nets[:250]

    for index in range(0, 248, 2):
        append_net = Network()

        for _ in range(2):
            append_net.hl_1.totalAssign(mergeMatrices(
                original_nets[index].hl_1.read(),
                original_nets[index + 1].hl_1.read()
            ))
            append_net.hl_2.totalAssign(mergeMatrices(
                original_nets[index].hl_2.read(),
                original_nets[index + 1].hl_2.read()
            ))
            append_net.ol.totalAssign(mergeMatrices(
                original_nets[index].ol.read(),
                original_nets[index + 1].ol.read()
            ))
            original_nets.append(append_net)

    return original_nets


def sortNetworks(nets):
    outputs = []
    for net in nets:
        sum = 0
        for x in range(2):
            for y in range(2):
                il = mfs.Matrix(columns=2)
                il.assign(x, c=0)
                il.assign(y, c=1)

                if il.read()[0][0] == il.read()[0][1]:
                    target_value = 0
                else:
                    target_value = 1

                sum += abs(net.run(il) - target_value) ** 2
        '''
        for _ in range(100):
            il = mfs.Matrix(columns=2)
            il.randomize(0, 1)
            if il.read()[0][0] == il.read()[0][1]: target_value = 0
            else: target_value = 1

            sum += abs(net.run(il) - target_value)**2
            '''
        avg_e = sum / 4

        outputs.append(avg_e)

    output_zip = sorted(list(zip(outputs, range(len(nets)))))
    print('Lowest Error: ', output_zip[0][0])

    avg = 0
    for e, index in output_zip:
        avg += e
    avg /= len(output_zip)
    print('Average Error: ', avg)

    return [nets[i] for _, i in output_zip]

net_list = [Network() for _ in range(500)]

close = False
generation = 0
while not close:
    generations = int(input("How Many Generations: "))


    for g in range(generations):
        print('Generation: ', generation+g+1)
        net_list = sortNetworks(net_list)

        for x in range(2):
            for y in range(2):
                il = mfs.Matrix(columns=2)
                il.assign(x, c=0)
                il.assign(y, c=1)
                print(x, y, net_list[0].run(il))

        net_list = breedNetworks(net_list)

    generation += generations



    generation += generations
