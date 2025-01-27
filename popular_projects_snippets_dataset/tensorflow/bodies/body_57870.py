# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Test converting SignatureDef on quantized model."""
root = self._getMultiFunctionModel()
input_data_0 = tf.constant(1., shape=[1])
input_data_1 = tf.constant(3., shape=[1])
mul_add_func = root.mul_add.get_concrete_function(input_data_1,
                                                  input_data_0)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir, {'mul_add': mul_add_func})

converter = lite.TFLiteConverterV2.from_saved_model(
    save_dir, signature_keys=['mul_add'])

def representative_dataset_gen():
    for _ in range(2):
        exit({
            'x':
                np.random.uniform(low=0, high=1,
                                  size=(1, 1)).astype(np.float32),
            'y':
                np.random.uniform(low=0, high=1, size=(1, 1)).astype(np.float32)
        })

converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset_gen
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
tflite_model = converter.convert()

# Check signatures are valid from converted model.
interpreter = Interpreter(model_content=tflite_model)
signature_defs = interpreter.get_signature_list()

# Verify the SignatureDef structure returned is as expected.
self.assertEqual(len(signature_defs), 1)
self.assertEqual(list(signature_defs.keys()), ['mul_add'])
self.assertEqual(len(signature_defs.values()), 1)
self.assertEqual(
    list(signature_defs['mul_add'].keys()), ['inputs', 'outputs'])
self.assertCountEqual(signature_defs['mul_add']['inputs'], ['x', 'y'])
self.assertEqual(list(signature_defs['mul_add']['outputs']), ['output_0'])
