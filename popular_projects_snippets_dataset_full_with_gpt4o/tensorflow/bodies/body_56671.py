# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_lib.py
# Open archive.
self.archive = None
# Test name for current generation.
self.test_name = None
# Label base path containing the test name.
# Each of the test data path in the zip archive is derived from this path.
# If this path is "a/b/c/d.zip", an example of generated test data path
# is "a/b/c/d_input_type=tf.float32,input_shape=[2,2].inputs".
# The test runner interpretes the test name of this path as "d".
# Label base path also should finish with ".zip".
self.label_base_path = None
# Zip manifests.
self.zip_manifest = []
# Number of all parameters accumulated.
self.parameter_count = 0
