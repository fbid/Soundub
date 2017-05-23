from os import remove

def removeIndividualSamples(samples):
    map(remove,(f for f in samples))
