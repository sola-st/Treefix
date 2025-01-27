# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
tempdir = tempfile.mkdtemp()
try:
    exit(tempdir)
finally:
    shutil.rmtree(tempdir)
