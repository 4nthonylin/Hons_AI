from math import *

class Neuron():
    m_weights = []
    m_inputs = []
    m_numinputs = 0
    m_threshold = 0.00
    m_output = 0.00
    m_trainingInputs = [[]]
    m_trainingOutputs = []
    m_numVectors = 0
    m_numTrainInputs = 0
    m_maxIterations = 1000
    m_errorThreshold = 0.1
    m_learningRate = 0.1
    m_sTrainingFile = ""

    def __init__(self, rhs):
        for x in range(rhs+1):
            self.m_weights.append(0.0)
            self.m_inputs.append(0.0)
        self.m_numinputs = rhs + 1
        self.m_threshold = 1.0
        self.m_output = 0.0

    def __init__(self):
        self.m_threshold = 1.0
        self.m_output = 0.0

    def loadTrainingData(self, rhs):
        try:
            self.m_numTrainInputs = len(rhs[0])
            self.m_numinputs = self.m_numTrainInputs
            self.m_numVectors = len(rhs)

            if self.m_numinputs <= 0 or self.m_numVectors <= 0:
                return

            self.m_trainingInputs = [[0.0 for x in range(self.m_numinputs)] for x in range(self.m_numVectors)] 
            self.m_weights = [0.0 for x in range(self.m_numinputs)]
            self.m_inputs = [0.0 for x in range(self.m_numinputs)]
            self.m_threshold = 1.0
            self.m_weights[0] = -self.m_threshold
            self.m_inputs[0] = 1.0
            self.m_trainingOutputs = [0.0 for x in range(self.m_numVectors)]

            for i in range(self.m_numVectors):
                self.m_trainingInputs[i][0] = 1.0
                for j in range(1, self.m_numinputs):
                    self.m_trainingInputs[i][j] = float(rhs[i][j-1])
                self.m_trainingOutputs[i] = float(rhs[i][-1])
        except EOFError:
            print "FILE ERROR"

    def train_error_correction(self):
        self.iNumCycles = 0
        fDesired = 0.0
        self.m_trainedWeights = []
        self.m_trainedWeights = [0.0 for x in range(self.m_numinputs)]

        while True:
            fError = 0.0
            for i in range(self.m_numVectors):
                fDesired = self.m_trainingOutputs[i]
                self.setInputs(self.m_trainingInputs[i])
                self.activate()
                fError += fDesired - self.getOutput()
                for j in range(self.m_numinputs):
                    self.m_weights[j] += self.m_learningRate * (fDesired - self.getOutput()) * self.m_trainingInputs[i][j]
            self.iNumCycles += 1
            if self.iNumCycles>self.m_maxIterations or fError<self.m_errorThreshold:
                if self.iNumCycles > 50:
                    self.m_trainingInputs = []
                    self.m_trainingOutputs = []
                    self.m_numTrainInputs = []
                    print "TRAINED"
                    print "Weights: "
                    print self.m_weights
                    print "Threshold: "
                    print self.m_threshold
                    print "Cycles: "
                    print self.iNumCycles
                    print "Error: "
                    print fError
                    print "PURGED"
                    break

    def setLearningRate (self, rhs):
        self.m_learningRate = rhs;
    
    def setMaxIterations (self, rhs):
        self.m_maxIterations = rhs;
    
    def setErrorThreshold (self, rhs):
        self.m_errorThreshold = rhs;
    
    def setWeight(self, rhs, w):
        if rhs >= self.m_inputs:
            return
        self.m_weights[rhs] = w

    def setWeights (self, rhs):
        self.m_weights = rhs;

    def setInput(self, rhs, w):
        if rhs >= self.m_numinputs:
            return
        self.m_inputs[rhs] = w

    def setInputs (self, rhs):
        self.m_inputs = rhs;

    def setThreshold (self, rhs):
        try:
            self.m_threshold = float(rhs)
        except ValueError:
            print "Please input a float"

    def getOutput(self):
        return self.m_output

    def activate(self):
        fSum = 0.0
        for i in range(self.m_numinputs):
            fSum += self.m_weights[i] * self.m_inputs[i]
        self.m_output = 1.0 if fSum > self.m_threshold else 0.0