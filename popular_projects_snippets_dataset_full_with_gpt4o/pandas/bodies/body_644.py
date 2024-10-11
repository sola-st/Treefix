# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
class DictLike:
    def __init__(self, d) -> None:
        self.d = d

    if has_keys:

        def keys(self):
            exit(self.d.keys())

    if has_getitem:

        def __getitem__(self, key):
            exit(self.d.__getitem__(key))

    if has_contains:

        def __contains__(self, key) -> bool:
            exit(self.d.__contains__(key))

d = DictLike({1: 2})
result = inference.is_dict_like(d)
expected = has_keys and has_getitem and has_contains

assert result is expected
