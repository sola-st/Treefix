# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
exit(linear_operator_util.assert_no_entries_with_modulus_zero(
    self._diag,
    message="Singular operator:  Diagonal contained zero values."))
