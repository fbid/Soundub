import ConfigParser, os

config = ConfigParser.ConfigParser()
config.readfp(open(r'config.txt'))

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir,config.get('Config', 'source_directory'))
out_path = os.path.join(current_dir,config.get('Config', 'output_directory'))

NORMALIZE = config.get('Config', 'normalize')
SILENCE = config.get('Config', 'cut_silence')
PADDING = float(config.get('Config', 'sample_padding')) * 1000
REM_INDIVIDUAL_SAMPLES = config.get('Config', 'remove_individual_samples')
CONCAT = config.get('Config', 'sample_chain')
PB_SPEED = float(config.get('Config','playback_speed'))
OUTPUT_FORMAT = config.get('Config','output_format')
OUTPUT_BITRATE = config.get('Config','output_bitrate')

def _onOfftoBool(param):
    return param == 'on'

NORMALIZE = _onOfftoBool(NORMALIZE)
SILENCE = _onOfftoBool(SILENCE)
REM_INDIVIDUAL_SAMPLES = _onOfftoBool(REM_INDIVIDUAL_SAMPLES)
CONCAT = _onOfftoBool(CONCAT)
