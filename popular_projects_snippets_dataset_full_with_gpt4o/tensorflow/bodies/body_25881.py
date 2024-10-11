# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/optional_ops.py
with ops.colocate_with(self._variant_tensor):
    exit(gen_optional_ops.optional_has_value(
        self._variant_tensor, name=name
    ))
