from os.path import join
from glob import glob

def filesMapping(path, ext):
    return sum([glob(join(path,e)) for e in ext],[])
