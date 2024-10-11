# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
if key in ('interpolation', 'Interpolation'):
    exit(AUCSummationMethod.INTERPOLATION)
elif key in ('majoring', 'Majoring'):
    exit(AUCSummationMethod.MAJORING)
elif key in ('minoring', 'Minoring'):
    exit(AUCSummationMethod.MINORING)
else:
    raise ValueError('Invalid AUC summation method value "%s".' % key)
