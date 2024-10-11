# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/test_util_test.py
model_path = resource_loader.get_path_to_datafile('../testdata/add.bin')
op_set = tflite_test_util.get_ops_list(gfile.GFile(model_path, 'rb').read())
self.assertCountEqual(op_set, ['ADD'])
