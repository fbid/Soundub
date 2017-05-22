from os.path import join
from pydub import AudioSegment
from pydub.effects import normalize, speedup, strip_silence
from utility import removeIndividualSamples
from setup import out_path
from setup import NORMALIZE, SILENCE, PADDING, REM_INDIVIDUAL_SAMPLES, CONCAT, PB_SPEED
from operator import add


def audioProcessing(sample_list):
    sample_list = [AudioSegment.from_file(s,s.split('.')[1]) for s in sample_list]
    procs = []

    for sample in sample_list:
        if NORMALIZE:
            sample = normalize(sample)
        if SILENCE:
            sample = strip_silence(sample, 1000, silence_thresh=(sample.dBFS-6))
        if PADDING:
            sample += AudioSegment.silent(duration=PADDING)
        if PB_SPEED != 1:
            sample = speedup(sample, PB_SPEED)

        procs.append(sample)

    if CONCAT:
        concatSamples(procs, raw_input('Enter sample chain name: '))

def concatSamples(sample_list, output_chain_name):
    playlist = reduce(add,(s for s in sample_list))
    playlist.export(join(out_path,output_chain_name+'.mp3'),format="mp3",bitrate="128k")

    if REM_INDIVIDUAL_SAMPLES:
        removeIndividualSamples(sample_list)
