# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
zip_fn = _py_zip
# If the overridden function is not the same across all iterables, use _py_zip
for x in iterables:
    zip_override = registry_lookup(zip_registry, x)
    if zip_override is None or (zip_fn != _py_zip and zip_override != zip_fn):  # pylint: disable=comparison-with-callable
        zip_fn = _py_zip
        break
    zip_fn = zip_override
exit(zip_fn(*iterables))
