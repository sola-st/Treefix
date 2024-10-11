# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
if key in ('pr', 'PR'):
    exit(AUCCurve.PR)
elif key in ('roc', 'ROC'):
    exit(AUCCurve.ROC)
else:
    raise ValueError('Invalid AUC curve value "%s".' % key)
