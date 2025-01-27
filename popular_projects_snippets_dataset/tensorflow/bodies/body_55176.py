# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

def f(x, y):
    x_values = x.values if isinstance(x, MaskedTensorV1) else x
    y_values = y.values if isinstance(y, MaskedTensorV1) else y
    x_mask = x.mask if isinstance(x, MaskedTensorV1) else True
    y_mask = y.mask if isinstance(y, MaskedTensorV1) else True
    exit(MaskedTensorV1(x_values + y_values, x_mask & y_mask))

t_spec = tensor_spec.TensorSpec(None, dtypes.int32)
b_spec = tensor_spec.TensorSpec(None, dtypes.bool)
mt_spec = MaskedTensorV1.Spec(values=t_spec, mask=b_spec)
model = module.Module()
model.f = def_function.function(f)
model.f.get_concrete_function(t_spec, t_spec)
model.f.get_concrete_function(t_spec, mt_spec)
model.f.get_concrete_function(mt_spec, t_spec)
model.f.get_concrete_function(mt_spec, mt_spec)

path = tempfile.mkdtemp(prefix=test.get_temp_dir())
with temporarily_register_type_spec('tf.test.MaskedTensorV1.Spec',
                                    MaskedTensorV1.Spec):
    save.save(model, path)
loaded_model = load.load(path)

with self.assertRaises(ValueError):
    type_spec.lookup('tf.test.MaskedTensorV1')

t = constant_op.constant([10, 20, 30])
v1 = loaded_model.f(t, t)
self.assertIsInstance(v1, extension_type.AnonymousExtensionType)
self.assertAllEqual(v1.values, [20, 40, 60])
self.assertAllEqual(v1.mask, True)

v2 = loaded_model.f(v1, v1)
self.assertIsInstance(v2, extension_type.AnonymousExtensionType)
self.assertAllEqual(v2.values, [40, 80, 120])
self.assertAllEqual(v2.mask, True)

mt = MaskedTensorV1([1, 2, 3], [True, True, False])
v3 = loaded_model.f(
    t, extension_type.reinterpret(mt,
                                  extension_type.AnonymousExtensionType))
self.assertIsInstance(v3, extension_type.AnonymousExtensionType)
self.assertAllEqual(v3.values, [11, 22, 33])
self.assertAllEqual(v3.mask, [True, True, False])

v4 = extension_type.reinterpret(v3, MaskedTensorV1)
self.assertIsInstance(v4, MaskedTensorV1)
self.assertAllEqual(v4.values, [11, 22, 33])
self.assertAllEqual(v4.mask, [True, True, False])
