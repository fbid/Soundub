from os.path import join
from pydub import AudioSegment
from pydub.effects import normalize, speedup, strip_silence
from utility import removeIndividualSamples
from setup import out_path
from setup import settings
from operator import add

def audioProcessing(sample_list):
    procs = []
    for s in sample_list:
        sample = AudioSegment.from_file(s,s.split('.')[1])
        if settings['NORMALIZE']:
            sample = normalize(sample)
        if settings['SILENCE']:
            sample = strip_silence(sample, 1000, silence_thresh=(sample.dBFS-6))
        if settings['PADDING']:
            sample += AudioSegment.silent(duration=settings['PADDING'])
        if settings['PB_SPEED'] != 1:
            sample = speedup(sample, settings['PB_SPEED'])
        if not settings['CONCAT']:
            # Exporting indivudial samples
            sample_name = s.split('/')[-1].split('.')[0]
            export(sample, sample_name, settings['OUTPUT_FORMAT'], settings['OUTPUT_BITRATE'])
        else:
            procs.append(sample)

    if settings['CONCAT']:
        # Exporting sample chain
        concatSamples(procs, raw_input('Enter sample chain name: '))

    if settings['REM_INDIVIDUAL_SAMPLES']:
        removeIndividualSamples(sample_list)

def concatSamples(sample_list, output_chain_name):
    playlist = reduce(add,(s for s in sample_list))
    export(playlist, output_chain_name, settings['OUTPUT_FORMAT'], settings['OUTPUT_BITRATE'])

def export(sample, sample_name, frmt, bitrate):
    if frmt == 'mp3':
        sample.export(join(out_path,sample_name+'.'+frmt),format=frmt,bitrate=bitrate)
    else:
        sample.export(join(out_path,sample_name+'.'+frmt),format=frmt)
