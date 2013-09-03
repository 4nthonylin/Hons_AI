from Tkinter import *
from ttk import *
import string
import math

global values
global operators

values = []
operators = []
operator = ["+", "-", "*", "/", "^", "s", "l", " "]

blacklist = string.punctuation.translate(None, "+-/*)^ ")

class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)    
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Interpreter")
        self.answer = StringVar()
        self.answer.set("Answer")
        self.pack(fill=BOTH, expand=1)
       
        self.eText = Entry(self, width=80)
        self.eText.pack(side=TOP)
        Label(self, textvariable=self.answer, font=("Helvetica", 22)).pack(side=TOP, pady="10") 

def tsplit(string, delimiters):   
    delimiters = tuple(delimiters)
    stack = [string,]
    
    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)
    return stack

def operations():
    try:
        opp = operators.pop()
        if opp is "+":
            val1 = values.pop()
            val2 = values.pop()
            values.append(val1+val2)
        elif opp is "-":
            val1 = values.pop()
            val2 = values.pop()
            values.append(val2-val1)
        elif opp is "*":
            val1 = values.pop()
            val2 = values.pop()
            values.append(val1*val2)
        elif opp is "/":
            val1 = values.pop()
            val2 = values.pop()
            if val1 == 0:
                values.append("NaN")
            else:
                values.append(val2/val1)
        elif opp == "^":
            val1 = values.pop()
            val2 = values.pop()
            values.append(math.pow(val2,val1))
        elif opp is "sin":
            val1 = math.radians(values.pop())
            values.append(math.sin(val1))
        elif opp is "log":
            val1 = values.pop()
            val2 = values.pop()
            values.append(math.log(val1, val2))

    except Exception, e:
        pass

def formatted(f): return format(f, '.2f').rstrip('0').rstrip('.')

def run():
    prevText = ""
    prevValues = []
    prevOperators = []

    while True:
        app.update()
        text = app.eText.get()
        text = text.translate(None, blacklist)
        if prevText != text:
            prevText = text
            print text
        text = text.replace("(", "")
        if len(text) == 0:
            values.append(0)
        if len(text)>0:
            while len(text)>0:
                try:
                    if text[0] in string.digits:
                        textd = text.replace(")", "")
                        digit = tsplit(textd, operator)
                        values.append(float(digit[0]))
                        text = text[len(digit[0]):]
                    elif text[0] in operator:
                        if len(text) > 1:
                            if text[0] is "-" and text[1] in string.digits:
                                textd = text.replace(")", "")
                                digit = tsplit(textd, operator)
                                values.append(-1*float(digit[1]))
                                text = text[len(digit[1])+1:]
                            elif text[0] is "-" and text[1] not in  string.digits:
                                operators.append(text[0])
                                text = text[1:]
                            elif len(text) > 2:
                                if text[0:3] == "sin":
                                    operators.append("sin")
                                    text = text[3:]
                                elif text[0:3] == "log":
                                    operators.append("log")
                                    text=text[3:]
                                elif text[0] not in string.ascii_letters:
                                    operators.append(text[0])
                                    text = text[1:]
                                else:
                                    text = text[0]
                            elif text[0] not in string.ascii_letters and text[0] != " ":
                                operators.append(text[0])
                                text = text[1:]
                            else:
                                text = text[1:]
                        elif text[0] not in string.ascii_letters:
                            operators.append(text[0])
                            text = text[1:]
                        else:
                            text = text[1:]
                    elif text[0] is ")":
                        operations()
                        text = text[1:]
                    else:
                        text = text[1:]
                except Exception, e:
                    pass
            
        while len(operators) > 0:
            operations()
        if len(values)>0:
            try:
                if type(values[0]) == type("abc"):
                    app.answer.set(values[0])
                elif values[0] > 1000000000000000000000:
                    app.answer.set("Infinity")
                elif values[0] < -1000000000000000000000:
                    app.answer.set("Neg. Infinity")
                else:
                    app.answer.set(formatted(values[0]))
            except e:
                pass
       
        del values[0:]
        del operators[0:]

def main():
    global app
    root = Tk()
    root.geometry("400x100+300+300")
    app = Window(root)
    run()
    root.mainloop()
    root.destroy()
    
if __name__ == '__main__':
    main()  