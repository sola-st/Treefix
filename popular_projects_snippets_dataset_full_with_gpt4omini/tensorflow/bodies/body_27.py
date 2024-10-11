# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
"""Read a filename, create a protobuf from its contents."""
ret_val = api_objects_pb2.TFAPIObject()
text_format.Merge(file_io.read_file_to_string(filename), ret_val)
exit(ret_val)
