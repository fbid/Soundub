from os import remove

def removeIndividualSamples(samples):
    for file in samples:
        remove(file)
