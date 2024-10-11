# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
output_signature = tensor_spec.TensorSpec((), dtypes.int64)
dataset = from_generator_op._GeneratorDataset(1, init_fn, next_fn,
                                              finalize_fn,
                                              output_signature)
iterator = iter(dataset)
next(iterator)
