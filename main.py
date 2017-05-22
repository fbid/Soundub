from mapping import filesMapping as mapSamples
from setup import src_path, out_path
from audioProcessing import audioProcessing as procSamples
from os.path import exists
from os import makedirs

if __name__ == '__main__':
    samples = mapSamples(src_path,['*.wav', '*.aiff', '*.mp3'])
    if not exists(out_path):
        makedirs(out_path)
    procSamples(samples)
