# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
# Currently, ExtensionArray.factorize -> Tuple[ndarray, EA]
# The sparsity on this is backwards from what Sparse would want. Want
# ExtensionArray.factorize -> Tuple[EA, EA]
# Given that we have to return a dense array of codes, why bother
# implementing an efficient factorize?
codes, uniques = algos.factorize(
    np.asarray(self), use_na_sentinel=use_na_sentinel
)
uniques_sp = SparseArray(uniques, dtype=self.dtype)
exit((codes, uniques_sp))
