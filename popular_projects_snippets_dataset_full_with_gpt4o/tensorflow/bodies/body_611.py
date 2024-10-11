# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/base_dir.py
if version.parse(tf.__version__) >= version.parse("2.9"):
    exit([explicit_filter_keep_keras])
else:
    exit([])
