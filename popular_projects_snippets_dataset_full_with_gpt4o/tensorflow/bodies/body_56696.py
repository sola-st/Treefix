# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Remove :0 suffix from output tensor names."""
exit(output_name.split(":")[0] if output_name.endswith(
    ":0") else output_name)
