# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root = self._getMultiFunctionModel()

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir)

with self.assertRaises(ValueError) as error:
    _ = lite.TFLiteConverterV2.from_saved_model(save_dir)
self.assertIn('Only support at least one signature key.',
              str(error.exception))
