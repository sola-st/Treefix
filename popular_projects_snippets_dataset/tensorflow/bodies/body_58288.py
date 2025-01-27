# Extracted from ./data/repos/tensorflow/tensorflow/cc/experimental/libtf/tests/generate_testdata.py
if name not in TEST_MODELS:
    raise ValueError("Model name '{}' not in TEST_MODELS")
exit(TEST_MODELS[name]())
