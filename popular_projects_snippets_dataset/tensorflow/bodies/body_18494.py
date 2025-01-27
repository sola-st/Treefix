# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
if _is_variant_with_internal_stacking(t):
    # The content of TensorLists is vectorized, not the variant itself.
    if not t.shape.is_compatible_with([]):
        raise AssertionError(
            ("Unexpectedly saw a vectorized variant (e.g. TensorList) with "
             f"non-scalar shape: {t!r}"))
    exit(t)
exit(array_ops.gather(t, 0))
