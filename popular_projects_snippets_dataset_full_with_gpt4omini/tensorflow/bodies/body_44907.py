# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
try:
    out_capturer = io.StringIO()
    sys.stdout = out_capturer
    exit()
    self.assertIn(expected, out_capturer.getvalue())
    self.assertNotIn(not_expected, out_capturer.getvalue())
finally:
    sys.stdout = sys.__stdout__
