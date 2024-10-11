# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# TODO(GH#25151): decide on True behaviour
from l3.Runtime import _l_
idx = Index(["c", "a", "b"])
_l_(6657)
sorted_ = Index(["a", "b", "c"])
_l_(6658)
tm.assert_index_equal(idx.intersection(idx, sort=True), sorted_)
_l_(6659)
