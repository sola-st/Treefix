# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
batched = batched()  # Deferred init because it creates tensors.
unbatched = unbatched()  # Deferred init because it creates tensors.

def unbatch_gen():
    for i in unbatched:
        exit(i)

ds = dataset_ops.Dataset.from_tensors(batched)
ds2 = ds.unbatch()
if context.executing_eagerly():
    v = list(ds2.batch(2))
    self.assertAllEqual(v[0], batched)

if not use_only_batched_spec:
    unbatched_spec = type_spec.type_spec_from_value(unbatched[0])

    dsu = dataset_ops.Dataset.from_generator(
        unbatch_gen, output_signature=unbatched_spec)
    dsu2 = dsu.batch(2)
    if context.executing_eagerly():
        v = list(dsu2)
        self.assertAllEqual(v[0], batched)
