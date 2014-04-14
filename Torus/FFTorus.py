from Tkinter import *
import tkMessageBox
import tkFileDialog
import math
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from random import uniform,shuffle

class torusGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        print "Initialising NeuralNetwork"
        self.parent = parent      
        self.net = buildNetwork(2, 12, 1, hiddenclass=TanhLayer, bias=True)
        self.ds = SupervisedDataSet(2, 1)
        self.trainer = BackpropTrainer(self.net, self.ds)  

        self.initUI()
        
    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        self.parent.title("TORUS")

        self.buttonTrain = Button(self, text="TRAIN", command=self.train)
        self.buttonTrain.pack(side="top")
        
        self.buttonPlot = Button(self, text="PLOT", command=self.plot)
        self.buttonPlot.pack(side="top")

        self.buttonGen = Button(self, text="GEN TEST", command=self.generatetest)
        self.buttonGen.pack(side="top")

        self.buttonGenD = Button(self, text="GEN TRAIN", command=self.generatetrain)
        self.buttonGenD.pack(side="top")

    def train(self):
        coord = list()
        path = tkFileDialog.askopenfilename()
        f = open(path, 'r')
        tar = []
        for line in f:
            x = line.split()
            coord.append([float(x[0]), float(x[1])])
            tar.append(float(x[2]))
        # coord = np.asarray(coord)
        # inp = coord.reshape(len(coord), 2)
        # tar = np.asarray(tar)
        # tar = tar.reshape(len(coord), 1)
        # net = nl.net.newff([[-11.0, 20.0], [-7.0, 11.0]],[5, 1])
        # error = net.train(inp, tar, epochs=10000, show=1, goal=3)
        # out = net.sim(inp)
        # print out
        # pl.subplot(211)
        # pl.plot(error)
        # pl.xlabel('Epoch number')
        # pl.ylabel('error (default SSE)')

        # x2 = np.linspace(-6.0,6.0,150)
        # y2 = net.sim(x2.reshape(x2.size,1)).reshape(x2.size)

        # y3 = out.reshape(size)

        # pl.subplot(212)
        # pl.plot(x2, y2, '-',x , y, '.', x, y3, 'p')
        # pl.legend(['train target', 'net output'])
        # pl.show()

        print "Initialising TrainingSet"
        print coord[0][0], coord[0][1], tar[0]
        print len(coord)
        for x in range(len(coord)):
            self.ds.addSample([coord[x][0], coord[x][1]], [tar[x]])
        print self.ds
        print "Training"
        x = 1
        while x > 0.005:
            x = self.trainer.train()
            print x
        print "Trained"


    def plot(self):
        coord = list()
        x1 = []
        x2 = []
        x3 = []
        y1 = []
        y2 = []
        y3 = []
        path = tkFileDialog.askopenfilename()
        f = open(path, 'r')
        for line in f:
            x = line.split()
            coord.append([float(x[0]), float(x[1])])

        for x in range(len(coord)):
            if self.net.activate([coord[x][0], coord[x][1]]) > 0.5:
                x1.append(coord[x][0])
                y1.append(coord[x][1])
            else:
                x2.append(coord[x][0])
                y2.append(coord[x][1])

        linex = -15
        while linex < 25:
            linex += 0.5
            liney = -15
            while liney < 25:
                liney+=0.2
                if self.net.activate([linex,liney]) > 0.47 and self.net.activate([linex,liney]) < 0.53:
                    x3.append(linex)
                    y3.append(liney)


        plt.plot(x1, y1, 'ro')
        plt.plot(x2, y2, 'bo')
        plt.plot(x3, y3, 'go')
        plt.autoscale(enable=True, tight=False)
        plt.show()

    def generatetest(self):
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        text = []
        r = 8
        R = 10
        while len(x1) < 1000:
            theta = uniform(0, math.pi)
            Radius = uniform(r, R)
            center = (0, 0)
            x1.append(center[0] + Radius*math.cos(theta))
            y1.append(center[1] + Radius*math.sin(theta))
        try:
            y = float(raw_input("Input d: "))
        except ValueError:
            y = 0
        while len(x2) < 1000:
            theta = uniform(0, -math.pi)
            Radius = uniform(r, R)
            center = ((r+R)/2, y)
            x2.append(center[0] + Radius*math.cos(theta))
            y2.append(center[1] + Radius*math.sin(theta))

        path = tkFileDialog.askopenfilename()
        f = open(path, 'w')
        for x in range(len(x1)):
            text.append('%f %f\n' % (x1[x], y1[x]))
        for x in range(len(x2)):
            text.append('%f %f\n' % (x2[x], y2[x]))
        shuffle(text)
        for x in text:
            f.write(x)
        f.close()
        plt.plot(x1, y1, 'ro')
        plt.plot(x2, y2, 'bo')
        plt.axis([-15, 25, -15, 15])
        plt.show()

    def generatetrain(self):
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        text = []
        r = 8
        R = 10
        while len(x1) < 1000:
            theta = uniform(0, math.pi)
            Radius = uniform(r, R)
            center = (0, 0)
            x1.append(center[0] + Radius*math.cos(theta))
            y1.append(center[1] + Radius*math.sin(theta))
        try:
            y = float(raw_input("Input d: "))
        except ValueError:
            y = 0
        while len(x2) < 1000:
            theta = uniform(0, -math.pi)
            Radius = uniform(r, R)
            center = ((r+R)/2, y)
            x2.append(center[0] + Radius*math.cos(theta))
            y2.append(center[1] + Radius*math.sin(theta))

        path = tkFileDialog.askopenfilename()
        f = open(path, 'w')
        for x in range(len(x1)):
            text.append('%f %f 1\n' % (x1[x], y1[x]))
        for x in range(len(x2)):
            text.append('%f %f 0\n' % (x2[x], y2[x]))
        shuffle(text)

        f.write("3\n")
        f.write("2000\n")
        for x in text:
            f.write(x)
        f.close()
        plt.plot(x1, y1, 'ro')
        plt.plot(x2, y2, 'bo')
        plt.axis([-15, 25, -15, 15])
        plt.show()


if __name__ == "__main__":
    root = Tk()
    app = torusGUI(root)
    root.mainloop()
