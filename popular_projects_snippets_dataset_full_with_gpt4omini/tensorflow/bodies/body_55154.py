# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
mt_spec = MaskedTensorV3.Spec(
    tensor_spec.TensorSpec(shape=[None, 1], dtype=dtypes.int32),
    tensor_spec.TensorSpec(shape=[None, 1], dtype=dtypes.bool),
)
model_input = input_layer.Input(type_spec=mt_spec)
model_output = array_ops.identity(model_input, name='output')
model = training.Model(inputs=model_input, outputs=model_output)
mt = MaskedTensorV3([[1], [2], [3]], [[True], [False], [True]])
self.assertEqual(model(mt), mt)
ds = dataset_ops.DatasetV2.from_tensors(mt)
self.assertEqual(model.predict(ds), mt)

with self.subTest('keras save'):
    path = self.create_tempdir().full_path
    model.save(path)
    loaded_model = keras_save.load_model(path)
    self.assertEqual(loaded_model.input.type_spec, mt_spec)
    self.assertEqual(loaded_model(mt), mt)

    loaded_fn = load.load(path)
    self.assertEqual(loaded_fn(mt), mt)
    with self.assertRaisesRegex(
        ValueError,
        'Could not find matching concrete function to call '
        'loaded from the SavedModel',
    ):
        loaded_fn(MaskedTensorV3([1, 2, 3], [True, False, True]))

    # The serving_fn use flatten signature
    serving_fn = loaded_fn.signatures['serving_default']
    self.assertEqual(
        serving_fn(args_0=mt.values, args_0_1=mt.mask)['tf.identity'], mt)
