# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/reference_test_base.py
"""Executes `func`, capturing stdout."""
out_capturer = io.StringIO()
results = None
captured_out = None
captured_err = None
try:
    sys.stdout = out_capturer
    results = func()
    captured_out = out_capturer.getvalue()
except Exception as e:  # pylint:disable=broad-except
    sys.stdout = sys.__stdout__
    captured_err = e
    print('*** Capturing exception:\n{}\n'.format(traceback.format_exc()))
finally:
    sys.stdout = sys.__stdout__
    out_capturer.close()
exit((results, captured_out, captured_err))
