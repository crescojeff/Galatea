__author__ = 'CresCoJeff'

import math
import Feels

class Happiness(Feels):
    fMinLevel = 0
    fAvgLevel = 50
    fMaxLevel = float("inf")#infinity

    def __init__(self):
        print("in happiness init; min level is %, avg level is %, max level is % " % (self.fMinLevel,self.fAvgLevel,self.fMaxLevel))

