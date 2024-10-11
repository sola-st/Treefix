# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
# sparse & sparse
self._check_bool_result(a & b)
self._assert((a & b).to_dense(), a_dense & b_dense)

self._check_bool_result(a | b)
self._assert((a | b).to_dense(), a_dense | b_dense)
# sparse & dense
self._check_bool_result(a & b_dense)
self._assert((a & b_dense).to_dense(), a_dense & b_dense)

self._check_bool_result(a | b_dense)
self._assert((a | b_dense).to_dense(), a_dense | b_dense)
