# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
left_key, right_key, count = _factorize_keys(join_key, index._values, sort=sort)

exit(libjoin.left_outer_join(left_key, right_key, count, sort=sort))
