# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test if the warning message when using TOCO is logged."""
log = io.StringIO()
handler = logging.StreamHandler(log)
logging.root.addHandler(handler)
warning_message = 'please use optimizations=[Optimize.DEFAULT] instead.'
lite.QuantizationMode([optimization], lite.TargetSpec(), None, None)
self.assertIn(warning_message, log.getvalue())
logging.root.removeHandler(handler)
