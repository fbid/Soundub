from os.path import join,dirname, abspath
from ConfigParser import ConfigParser

cp = ConfigParser()
cp.readfp(open(r'config.txt'))

cwd = dirname(abspath(__file__))
src_path = join(cwd,cp.get('Config', 'source_dir'))
out_path = join(cwd,cp.get('Config', 'output_dir'))

settings = {
    'NORMALIZE': cp.get('Config', 'normalize') == 'on',
    'SILENCE': cp.get('Config', 'cut_silence') == 'on',
    'REM_INDIVIDUAL_SAMPLES': cp.get('Config', 'remove_individual_samples') == 'on',
    'CONCAT': cp.get('Config', 'sample_chain') == 'on',
    'PADDING': float(cp.get('Config', 'sample_padding')) * 1000,
    'PB_SPEED': float(cp.get('Config','playback_speed')),
    'OUTPUT_FORMAT': cp.get('Config','output_format'),
    'OUTPUT_BITRATE': cp.get('Config','output_bitrate')
}
