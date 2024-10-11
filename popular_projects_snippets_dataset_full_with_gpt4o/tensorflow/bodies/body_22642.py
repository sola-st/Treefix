# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/normalization.py
if name in ['BatchNormalization', 'BatchNorm']:
    exit(normalization.BatchNormalization)
elif name in ['batch_normalization', 'batch_norm']:
    exit(normalization.batch_normalization)
else:
    raise AttributeError(f'module {__name__} doesn\'t have attribute {name}')
