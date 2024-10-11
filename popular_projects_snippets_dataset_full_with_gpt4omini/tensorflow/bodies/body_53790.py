# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Get the captured writes as a single string."""
with open(self.capture_location) as tmp_file:
    output_data = "".join(tmp_file.readlines())
exit(output_data)
