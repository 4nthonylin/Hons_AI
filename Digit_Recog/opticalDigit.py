from Tkinter import *
from neuron import *
from ttk import *
import random
import copy

class digitGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.neuron = [Neuron() for x in range(10)]
        self.rows = 7
        self.columns = 5
        self.size = 32
        self.zero =  ([[0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]])
        self.one = ([[0,1,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [1,1,1,1,1]])
        self.two = ([[0,1,1,1,0],
            [1,0,0,0,1],
            [0,0,0,1,0],
            [0,0,1,0,0],
            [0,1,0,0,0],
            [1,0,0,0,0],
            [1,1,1,1,1]])
        self.three = ([[0,1,1,1,0],
            [1,0,0,0,1],
            [0,0,0,0,1],
            [0,0,1,1,0],
            [0,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]])
        self.four = ([[0,0,1,1,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [1,0,0,1,0],
            [1,1,1,1,1],
            [0,0,0,1,0],
            [0,0,0,1,0]])
        self.five = ([[1,1,1,1,1],
            [1,0,0,0,0],
            [1,1,1,1,0],
            [0,0,0,0,1],
            [0,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]])
        self.six = ([[0,0,1,1,1],
            [0,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]])
        self.seven = ([[1,1,1,1,1],
            [0,0,0,0,1],
            [0,0,0,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0]])
        self.eight = ([[0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,0]])
        self.nine = ([[0,1,1,1,0],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [0,1,1,1,1],
            [0,0,0,0,1],
            [0,0,0,1,0],
            [0,1,1,0,0]])
        self.error = ([[0,1,1,1,1],
           [1,0,0,0,0],
           [1,0,0,0,0],
           [0,1,1,1,0],
           [1,0,0,0,0],
           [1,0,0,0,0],
           [0,1,1,1,1]])
        self.numbers = (self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine)
        self.inputNumber = ([[255,255,255,255,255],
            [255,255,255,255,255],
            [255,255,255,255,255],
            [255,255,255,255,255],
            [255,255,255,255,255],
            [255,255,255,255,255],
            [255,255,255,255,255]])
        self.initUI()
        self.drawIn(self.inputNumber)
        self.drawOut(self.inputNumber)
        
    def initUI(self):
        self.parent.title("Digit Recog")
        self.pack(fill=BOTH, expand=1)

        frame = Frame(self)
        frame.grid(row=0, column=1)

        digitHolder = Frame(self)
        digitHolder.grid(row=1, columnspan=3)

        
        self.inWindow = Canvas(self, width=self.columns * self.size + 10, height=self.rows * self.size + 10, borderwidth=2)
        self.inWindow.grid(row=0, column=0)
        

        self.outWindow = Canvas(self, width=self.columns * self.size + 10, height=self.rows * self.size + 10, borderwidth=2)
        self.outWindow.grid(row=0, column=2)

        self.identifyBtn = Button(frame, text="IDENTIFY", command=self.identify).pack(side="top")
        self.trainBtn = Button(frame, text="TRAIN", command=self.train).pack(side="top")
        self.addNoise = Button(frame, text="ADD NOISE", command=self.Noise).pack(side="top")

        self.btnZero = Button(digitHolder, text="ZERO", width=6, command=self.zeroFunc).pack(side="left")
        self.btnOne = Button(digitHolder, text="ONE", width=6, command=self.oneFunc).pack(side="left")
        self.btnTwo = Button(digitHolder, text="TWO", width=6, command=self.twoFunc).pack(side="left")
        self.btnThree = Button(digitHolder, text="THREE", width=6, command=self.threeFunc).pack(side="left")
        self.btnFour = Button(digitHolder, text="FOUR", width=6, command=self.fourFunc).pack(side="left")
        self.btnFive = Button(digitHolder, text="FIVE", width=6, command=self.fiveFunc).pack(side="left")
        self.btnSix = Button(digitHolder, text="SIX", width=6, command=self.sixFunc).pack(side="left")
        self.btnSeven = Button(digitHolder, text="SEVEN", width=6, command=self.sevenFunc).pack(side="left")
        self.btnEight = Button(digitHolder, text="EIGHT", width=6, command=self.eightFunc).pack(side="left")
        self.btnNine = Button(digitHolder, text="NINE", width=6, command=self.nineFunc).pack(side="left")

    def train(self):
        holder = copy.deepcopy(self.inputNumber)
        for x in range(10):
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
            del options[x]
            training_data = []
            temp = self.splitArray(self.parse(self.numbers[x]))
            temp.append(1)
            training_data.append(temp)
            for i in range(30):
                self.inputNumber = self.parse(self.numbers[x])
                self.Noise1()
                temp1 = self.splitArray(self.inputNumber)
                temp1.append(1)
                training_data.append(temp1)

            for i in options:
                for y in range(30):
                    self.inputNumber= self.parse(self.numbers[i])
                    self.Noise1()
                    temp2 = self.splitArray(self.inputNumber)
                    temp2.append(0)
                    training_data.append(temp2)
            self.neuron[x].loadTrainingData(training_data)
            self.neuron[x].train_error_correction()
            print "Trained: %i" % (x)
        print "-----------------------------"
        print "Completed Training Process"
        print "-----------------------------"
        self.inputNumber = copy.deepcopy(holder)


    def parse(self, temp):
        array = copy.deepcopy(temp)
        for x in range(7):
            for y in range(5):
                array[x][y] = 0 if temp[x][y] is 1 else 255
        return array
    def splitArray(self, array):
        output = []
        for x in range(7):
            for y in range(5):
                output.append(array[x][y])
        return output

    def convertcolour(self, grayscale):
        temp = hex(grayscale)
        temp2 = temp[2:]
        colourcode = "#%s" % (temp2*3)
        return colourcode

    def identify(self):
        identification = self.splitArray(self.inputNumber)
        identification.insert(0, 1.0)
        outputs = []
        for x in range(10):
            self.neuron[x].setInputs(identification)
            self.neuron[x].activate()
            outputs.append(self.neuron[x].getOutput())
            print "NEURON %i: %.2f" % (x, outputs[x])

        for x in range(10):
            if outputs[x] == 1:
                self.drawOut(self.parse(self.numbers[x]))
                break
            else:
                self.drawOut(self.parse(self.error))
        print "--------------------------------"

    def zeroFunc(self):
        self.inputNumber = self.parse(self.zero)
        self.drawIn(self.inputNumber)
    def oneFunc(self):
        self.inputNumber = self.parse(self.one)
        self.drawIn(self.inputNumber)
    def twoFunc(self):
        self.inputNumber = self.parse(self.two)
        self.drawIn(self.inputNumber)
    def threeFunc(self):
        self.inputNumber = self.parse(self.three)
        self.drawIn(self.inputNumber)
    def fourFunc(self):
        self.inputNumber = self.parse(self.four)
        self.drawIn(self.inputNumber)
    def fiveFunc(self):
        self.inputNumber = self.parse(self.five)
        self.drawIn(self.inputNumber)
    def sixFunc(self):
        self.inputNumber = self.parse(self.six)
        self.drawIn(self.inputNumber)
    def sevenFunc(self):
        self.inputNumber = self.parse(self.seven)
        self.drawIn(self.inputNumber)
    def eightFunc(self):
        self.inputNumber = self.parse(self.eight)
        self.drawIn(self.inputNumber)
    def nineFunc(self):
        self.inputNumber = self.parse(self.nine)
        self.drawIn(self.inputNumber)    

    def Noise(self):
        rate = 0.2
        for x in range(5):
            for y in range(7):
                if random.random() < rate:
                    if self.inputNumber[y][x] == 0:
                        self.inputNumber[y][x] += random.randrange(0, 200)
                    else: 
                        self.inputNumber[y][x] -= int(self.inputNumber[y][x] * random.uniform(0.5, 1))

        self.drawIn(self.inputNumber)

    def Noise1(self):
        rate = 0.3
        for x in range(5):
            for y in range(7):
                if random.random() < rate:
                    if self.inputNumber[y][x] == 0:
                        self.inputNumber[y][x] += random.randrange(0, 200)
                    else: 
                        self.inputNumber[y][x] -= int(self.inputNumber[y][x] * random.uniform(0.5, 1))

    def drawIn(self, array):
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.inWindow.create_rectangle(x1+5, y1+5, x2+5, y2+5, outline="gray", fill=self.convertcolour(array[row][col]), tags="square")
    def drawOut(self, array):
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.outWindow.create_rectangle(x1+5, y1+5, x2+5, y2+5, outline="gray", fill=self.convertcolour(array[row][col]), tags="square")

if __name__ == "__main__":
    root = Tk()
    app = digitGUI(root)
    root.mainloop()
