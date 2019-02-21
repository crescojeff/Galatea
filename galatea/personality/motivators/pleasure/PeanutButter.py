__author__ = 'CresCoJeff'

'''
pseudocode for relevant verbs
Munch{
Def := to consume vigorously
Connotation := good food and good times
Usage := "The dog was overjoyed by his treat, munching happily."
}
Inhale{
Def := to eat without chewing
Connotation := hunger more driving than the need to breathe
Usage := "He inhaled the delicious peanut butter treat, pausing a moment to cough but smiling all the while."
}
'''

class PeanutButter:
    #TODO: figure out how to get these values on ratio scale

    # defines when savory threshold is reached
    iSavoryThreshold = 100
    # defines when sweetness threshold is reached
    iSweetnessThreshold = 100

    # boolean value that defines whether or not PB is chunky
    bChunky = False
    # integer value that defines the proliferation of chunks in the lovely PB, in terms of
    # number of chunks per cubic millimeter (assuming uniform chunk volume
    # and density, as per The Ancient and Most Official Peanut Butter Standard)
    iChunkProliferation = 0

    #float value that defines the degree to which we savor savory
    fSavoryProclivity = 55.5

    #float that defines the degree to which sweetness is appreciated
    fSweetProclivity = 55.5

    def __init__(self):
        print("Savory threshold is reached at %i and re: chunkiness: %s" % (self.iSavoryThreshold, ("moar crunch!" if self.bChunky else "no crunch in my munch!")))

