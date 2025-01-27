# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/module_test.py
# pylint: disable=pointless-statement
tf.summary.image
# If we use v2 API, check for create_file_writer,
# otherwise check for FileWriter.
if hasattr(tf, '_major_api_version') and tf._major_api_version == 2:
    tf.summary.create_file_writer
else:
    tf.compat.v1.summary.FileWriter
