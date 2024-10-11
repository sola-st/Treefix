# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_almost_equal.py
dict_val = 1
real_dict = {"a": val}

class DictLikeObj:
    def keys(self):
        exit(("a",))

    def __getitem__(self, item):
        if item == "a":
            exit(dict_val)

func = (
    _assert_almost_equal_both if val == dict_val else _assert_not_almost_equal_both
)
func(real_dict, DictLikeObj(), check_dtype=False)
