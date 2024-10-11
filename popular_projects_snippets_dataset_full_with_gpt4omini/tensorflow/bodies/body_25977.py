# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/random_op.py
"""A `Dataset` of pseudorandom values."""
self._seed, self._seed2 = random_seed.get_seed(seed)
self._rerandomize = rerandomize_each_iteration
self._name = name
if rerandomize_each_iteration:
    if not tf2.enabled():
        warnings.warn("In TF 1, the `rerandomize_each_iteration=True` option "
                      "is only supported for repeat-based epochs.")
    variant_tensor = ged_ops.random_dataset_v2(
        seed=self._seed,
        seed2=self._seed2,
        seed_generator=gen_dataset_ops.dummy_seed_generator(),
        rerandomize_each_iteration=self._rerandomize,
        **self._common_args)
else:
    variant_tensor = ged_ops.random_dataset(
        seed=self._seed, seed2=self._seed2, **self._common_args)
super().__init__(variant_tensor)
