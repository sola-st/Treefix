# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v1_12.py
cls._tf_api_version = 1 if hasattr(tf, 'contrib') else 2
