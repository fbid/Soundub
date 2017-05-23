from os.path import join,dirname, abspath
from ConfigParser import ConfigParser

cp = ConfigParser()
cp.readfp(open(r'config.txt'))

cwd = dirname(abspath(__file__))
src_path = join(cwd,cp.get('Config', 'source_dir'))
out_path = join(cwd,cp.get('Config', 'output_dir'))

settings['NORMALIZE'] = cp.get('Config', 'normalize') == 'on'
settings['SILENCE'] = cp.get('Config', 'cut_silence') == 'on'
settings['REM_INDIVIDUAL_SAMPLES'] = cp.get('Config', 'remove_individual_samples') == 'on'
settings['CONCAT'] = _cp.get('Config', 'sample_chain') == 'on'
settings['PADDING'] = float(cp.get('Config', 'sample_padding')) * 1000
settings['PB_SPEED'] = float(cp.get('Config','playback_speed'))
settings['OUTPUT_FORMAT'] = cp.get('Config','output_format')
settings['OUTPUT_BITRATE'] = cp.get('Config','output_bitrate')
