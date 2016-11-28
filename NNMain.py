import tkinter as Tk
import NNDataFunctions as DataTools
from NNButtonFunctions import *
from copy import deepcopy

class GlobalValues():
    close = False
    load_networks = False

master = Tk.Tk()
global_values = GlobalValues()

button_newnets = Tk.Button(
    master,
    text='Generate New Network Data File',
    #command=DataTools.generateNewNetworks,
    state='normal'
)
button_newtestnet = Tk.Button(
    master,
    text='Generate Test Network',
    command=lambda: DataTools.buildNetwork(0)
)
button_loadall = Tk.Button(
    master,
    text='Load All Networks',
    command=lambda: loadAllNetworks(global_values)
)
button_exit = Tk.Button(
    master,
    text='Exit',
    command=lambda: exitGUI(global_values)
)

button_newnets.grid(row=0, column=0)
button_newtestnet.grid(row=1, column=0)
button_loadall.grid(row=2, column=0)
button_exit.grid(row=3, column=0)


while not global_values.close:
    if global_values.load_networks:
        networks = [deepcopy(DataTools.NN(x)) for x in range(10)]
        for index in range(len(networks)):
            networks[index].load_data()
            print(networks[index].layer_one_node_list)
        global_values.load_networks = False
    master.update_idletasks()
    master.update()
