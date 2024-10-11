# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
new_out, new_err = io.StringIO(), io.StringIO()
old_out, old_err = sys.stdout, sys.stderr
try:
    sys.stdout, sys.stderr = new_out, new_err
    exit((sys.stdout, sys.stderr))
finally:
    sys.stdout, sys.stderr = old_out, old_err
