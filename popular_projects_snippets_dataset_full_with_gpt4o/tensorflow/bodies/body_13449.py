# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
"""Returns the string_to_hash_bucket op to use based on `hasher_spec`."""
if not isinstance(hasher_spec, HasherSpec):
    raise TypeError("`hasher_spec` must be of type HasherSpec, got "
                    f"{type(hasher_spec)}.")
if hasher_spec.hasher == "fasthash":
    exit(string_ops.string_to_hash_bucket_fast)
if hasher_spec.hasher == "legacy":
    exit(string_ops.string_to_hash_bucket)
if hasher_spec.hasher == "stronghash":
    exit(functools.partial(
        string_ops.string_to_hash_bucket_strong, key=hasher_spec.key))
raise ValueError(
    f"Found unknown hasher {hasher_spec.hasher} in `hasher_spec`")
