import os
from os.path import join as pjoin

EGS_DIR = '/scail/group/deeplearning/speech/zxie/kaldi-stanford/kaldi-trunk/egs'

DATASET = 'swbd'

SCAIL_DATA_DIR = '/scail/data/group/deeplearning/u/zxie'

# CTC Parameters

if DATASET == 'wsj':
    DATA_SUBSET = 'test_eval92'
    DATA_DIR = pjoin(EGS_DIR, 'wsj/s6/exp/%s_ctc/' % DATA_SUBSET)
    #DATA_DIR = pjoin(EGS_DIR, 'wsj/s6/exp/train_si284_ctc/')
    INPUT_DIM = 21*23
    RAW_DIM = 41*23
    OUTPUT_DIM = 32  # FIXME
    MAX_UTT_LEN = 2000
    LAYER_SIZE = 1824
elif DATASET == 'swbd':
    DATA_SUBSET = 'eval2000'
    DATA_DIR = pjoin(EGS_DIR, 'swbd/s5b/exp/%s_ctc/' % DATA_SUBSET)
    INPUT_DIM = 41*15
    RAW_DIM = 41*15
    OUTPUT_DIM = 35
    MAX_UTT_LEN = 5000
    LAYER_SIZE = 1824
    SWBD_SUBSET = 'callhome'
    assert SWBD_SUBSET in ['callhome', 'swbd', 'all']

# LM Parameters

LM_SOURCE = '/afs/cs.stanford.edu/u/zxie/py-arpa-lm/lm.py'

if DATASET == 'wsj':
    SPACE = '<SPACE>'
    SPECIALS_LIST = frozenset(['<SPACE>', '<NOISE>'])
    CHARMAP_PATH = pjoin(EGS_DIR, 'wsj/s6/ctc-utils/')
elif DATASET == 'swbd':
    SPACE = '[space]'
    SPECIALS_LIST = frozenset(['[vocalized-noise]', '[laughter]', '[space]', '[noise]'])
    CHARMAP_PATH = pjoin(EGS_DIR, 'swbd/s5b/ctc-utils/')

LM_ARPA_FILE = '/scail/data/group/deeplearning/u/zxie/biglm/lms/biglm.5g.1.arpa'

# Model parameters

NUM_LAYERS = 5
ANNEAL = 1.2 if DATASET == 'wsj' else 1.3
TEMPORAL_LAYER = 3

#MODEL_DIR = '/afs/cs.stanford.edu/u/zxie/kaldi-stanford/stanford-nnet/ctc_fast/models'
MODEL_DIR = '/scail/group/deeplearning/speech/zxie/ctc_models'

def get_brnn_model_file():
    # TODO Figure out what "new_layers" means in wsj model
    model_file = pjoin(MODEL_DIR, '%s_%d_%d_bitemporal_%d_step_1e-5_mom_.95_anneal_%.1f.bin' % (DATASET, NUM_LAYERS, LAYER_SIZE, TEMPORAL_LAYER, ANNEAL))
    assert os.path.exists(model_file)
    return model_file