# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_lib.py
if not os.path.isdir(x):
    os.mkdir(x)
    if not os.path.isdir(x):
        raise RuntimeError("Failed to create dir %r" % x)
