import string
import pickle

class Node():
	Parent = None
	Data = None
	Left = None
	Right = None

	def __init__(self, iParent, iData, iLeft, iRight):
		self.Parent = iParent
		self.Data = iData
		self.Left = iLeft
		self.Right = iRight

	def isLeaf(self):
		return (self.Left == None) & (self.Right == None)

def query(prompt):
	answer = raw_input(prompt + "[Y or N]: ")	
	answer = string.lower(answer)
	while answer[0] != 'y' and answer[0]!= 'n':
		answer = raw_input("Invalid response. Please type Y or N: ")
		answer = string.lower(answer)
	return answer[0] == 'y'

def learn(current):
	guessWord = current.Data
	difference = raw_input("What makes them different?: ")
	correctWord = raw_input("What were you thinking?: ")

	current.Data = difference
	current.Left = Node(current, guessWord, None, None)
	current.Right = Node(current, correctWord, None, None)

def startTree():
	if not query("Load from text file? "):
		start = Node(None, "Is it an animal?", None, None)
		t = Node(None, "Is it an animal?", Node(start, "Bamboo", None, None), Node(start, "Tiger", None, None))
		return t

	else:
		path = raw_input("Enter File Path: ")
		t = pickle.load(open(path, "r+"))
		return t

def play(current):
	while not current.isLeaf():
		if query(current.Data): current = current.Right
		else: current = current.Left
	temp = 	current.Data
	if temp[0] == 'a' or temp[0] == 'i' or temp[0] == 'o' or temp[0] == 'u' or temp[0] == 'e':
		preposition = "an"
	else:
		preposition = "a"
	if not query("Is it " + preposition + " " + temp + "?"):
		learn(current)
	else:
		print "I knew it!"

def main():
	root = startTree()

	while True:
		play(root)
		if query("Save to text file? "):
			path = raw_input("Path: ")
			pickle.dump(root, open(path, "w+"))

		if not query("Play Again? "):
			break;

if __name__ == '__main__':
    main()  
