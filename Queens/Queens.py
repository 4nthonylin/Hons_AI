from Tkinter import *
from ttk import *
from random import choice, randint
import time
import tkMessageBox

DEBUGGING = False
DELAY = 0
MODE = False
VERBOSE = False

class window(Frame):
    def __init__(self, parent):
        self.rows = boardSize
        self.columns = boardSize
        self.size = squareSize
        self.color1 = "white"
        self.color2 = "gray"
        self.queens = []        
        self.pic = PhotoImage(file ="queen.gif")

        canvas_width = self.columns * self.size
        canvas_height = self.rows * self.size

        Frame.__init__(self, parent)   

        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.parent = parent
        self.initUI()

        
    def initUI(self):
        self.parent.title("Queens %ix%i Genetic Algorithm" % (boardSize, boardSize))
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)
        
        quitButton = Button(self, text="QUIT", command=self.close)
        quitButton.pack(side=RIGHT, padx=10, pady=20)
        findButton = Button(self, text="FIND", command=self.query)
        findButton.pack(side=RIGHT, padx=10, pady=20)
        self.enterPopulation = Entry(self, width=5)
        self.enterPopulation.pack(side=RIGHT, padx=10)
        labelEntry = Label(self, text="Population")
        labelEntry.pack(side=RIGHT, padx=10)

        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=RIGHT)
        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)        
        self.label.pack(side=RIGHT, padx=5)
        scaleLabel = Label(self, text="Delay")
        scaleLabel.pack(side=RIGHT, padx=5)



        color = self.color2

        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2

    def place(self, xcoord, ycoord):
        x = (xcoord+1)*self.size
        x -= (self.size/2)
        y = (ycoord+1)*self.size
        y -= (self.size/2)
        self.queens.append(self.canvas.create_image(x, y, image = self.pic, anchor = CENTER))

    def query(self):
        if len(self.enterPopulation.get()) > 0:
            run(int(self.enterPopulation.get()))
        else:
            tkMessageBox.showerror(title="Warning", message="Incorrect Population Size")

    def delete(self):
        for queen in self.queens:
            self.canvas.delete(queen)
        self.queens = []

    def add(self, individual):
        self.delete()
        for x in range(boardSize):
            self.place(x, individual[x])


    def onScale(self, val):
        global DELAY
        DELAY = int(float(val))
        self.var.set(DELAY)

    def close(self):
        global stop
        stop = True
        self.quit()


def main():
    global boardSize
    global squareSize
    global app
    global stop
    stop = False
    squareSize = 64
    boardSize = int(raw_input("input n for NxN grid \n"))
    root = Tk()
    root.geometry("%ix%i+%i+%i" % (boardSize*squareSize, boardSize*squareSize+68, root.winfo_screenwidth()/2-boardSize*squareSize/2, root.winfo_screenheight()/2-(boardSize*squareSize+68)/2))
    app = window(root)
    root.mainloop()  
    root.destroy()




def genetic1(population, fitness):
    generations = 0
    solution = []
    start_time = time.clock()
    while(not check(population) and not stop):
        app.after(DELAY)
        population = selection(population, fitness, generations)
        temp = find(population, False)
        if VERBOSE: print temp[0]
        app.add(temp[0])
        app.update()

        generations += 1

    temp = find(population, False)
    solution = temp[0]
    app.add(solution)
    app.update()
    print "Generations: ", generations
    print "Time Elapsed: %2.2f seconds" % (time.clock() - start_time)

    return solution

def generate_population(size):
    population = []
    for i in range(size):
        individual = outsider()
        population.append(individual)
        if DEBUGGING: print individual
    return population

def outsider():
    individual = []
    options = range(boardSize)
    for i in range(boardSize):
        select = choice(options)
        individual.append(select)
        options.remove(select)

    return individual

def check(population):
    population = find(population, False)

    if FITNESS_FN(population[0]) == 0:
        if DEBUGGING:
            print "FOUND"
            print population[0]
        return True

def find(population, debug):
    temp = []
    fitness_vals = dict()
    index = 0
    for i in population:
        fitness_vals[index] = FITNESS_FN(i)
        index+=1
    fitness_vals_sorted = sorted(fitness_vals, key=fitness_vals.get, reverse = False)
    if DEBUGGING and debug: print fitness_vals_sorted

    for i in fitness_vals_sorted:
        temp.append(population[i])
        if DEBUGGING and debug: print population[i], fitness_vals[i]

    return temp

def FITNESS_FN(individual):
    fitness_val = 0
    for i in range(boardSize):
        if not individual.count(i) == 1:
            fitness_val += individual.count(i)
        for o in range(1, boardSize):
            if abs(individual[i] - individual[o]) == abs(i - o) and not abs(i - o) == 0:
                fitness_val += 1
    return fitness_val

def mutate(individual, trigger):
    individual[trigger] = randint(0, boardSize-1)
    return individual

def reproduce(individualA, individualB, trigger):
    combined = []
    for i in range(trigger): combined.append(individualA[i])
    for i in range(trigger, boardSize): combined.append(individualB[i])
    return combined

def selection(population, fitness, generations):
    temp = find(population, False)
    population = []

    for i in range(len(temp) - 2):
        reproduced = reproduce(temp[i], temp[i+1], randint(2, boardSize-3))
        mutated = mutate(reproduced, randint(0, boardSize-1))
        population.append(mutated)
    if MODE:
        for i in range(1):
            population.append(outsider())
        population.append(temp[0])
    else:
        for i in range(2):
            population.append(outsider()) 

    population = find(population, True)

    if VERBOSE: print "Generation: ", generations, "Smallest Fitness: ", FITNESS_FN(population[0])

    return population

def size(population_size):
    print "Population Size: ", population_size
    time.sleep(0.25)
    population = generate_population(population_size)
    solution = genetic1(population, FITNESS_FN)
    if not stop:
        print "Found: ", solution

def run(*args):
    size(args[0])


if __name__ == "__main__":
    main()
