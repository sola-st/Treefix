# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/converter_testing.py
try:
    out_capturer = io.StringIO()
    sys.stdout = out_capturer
    exit()
    self.assertEqual(out_capturer.getvalue(), expected_result)
finally:
    sys.stdout = sys.__stdout__
