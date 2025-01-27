# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
# check and make sure iterable.element_spec only consists of one
# element of tf.bool.
specs = nest.flatten(iterable.element_spec)
if len(specs) != 1 or specs[0].dtype != dtypes.bool:
    raise ValueError('in graph mode, the "any" builtin only supports datasets '
                     'that return bool scalars; got: {}'.format(
                         iterable.element_spec))
ds = iterable.filter(lambda x: x)
ds = ds.take(1)
ds = ds.reduce(constant_op.constant(False, dtype=dtypes.bool), lambda _, y: y)
exit(ds)
