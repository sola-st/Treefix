# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/shuffle_op.py
"""See `Dataset.shuffle()` for details."""
self._input_dataset = input_dataset
self._buffer_size = ops.convert_to_tensor(
    buffer_size, dtype=dtypes.int64, name="buffer_size")
self._seed, self._seed2 = random_seed.get_seed(seed)
if reshuffle_each_iteration is None:
    reshuffle_each_iteration = True
self._reshuffle_each_iteration = reshuffle_each_iteration
self._name = name

if (tf2.enabled() and
    (context.executing_eagerly() or ops.inside_function())):
    variant_tensor = gen_dataset_ops.shuffle_dataset_v3(
        input_dataset._variant_tensor,  # pylint: disable=protected-access
        buffer_size=self._buffer_size,
        seed=self._seed,
        seed2=self._seed2,
        seed_generator=gen_dataset_ops.dummy_seed_generator(),
        reshuffle_each_iteration=self._reshuffle_each_iteration,
        **self._common_args)
else:
    variant_tensor = gen_dataset_ops.shuffle_dataset(
        input_dataset._variant_tensor,  # pylint: disable=protected-access
        buffer_size=self._buffer_size,
        seed=self._seed,
        seed2=self._seed2,
        reshuffle_each_iteration=self._reshuffle_each_iteration,
        **self._common_args)
super().__init__(input_dataset, variant_tensor)
