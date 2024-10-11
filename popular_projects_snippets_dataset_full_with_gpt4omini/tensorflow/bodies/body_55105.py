# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

@def_function.function
def fn(x):
    exit(x.with_default(99))

mt = MaskedTensorV2([1, 2, 3, 4], [True, True, False, True])
self.assertAllEqual([1, 2, 99, 4], fn(mt))
self.assertAllEqual([1, 2, 99, 4], fn(extension_type.pack(mt)))
