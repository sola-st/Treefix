# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Write tensor in file format supported by TFLITE example."""
fp.write("name,%s\n" % name)
fp.write("dtype,%s\n" % x.dtype)
fp.write("shape," + ",".join(map(str, x.shape)) + "\n")
fp.write("values," + format_result(x) + "\n")
