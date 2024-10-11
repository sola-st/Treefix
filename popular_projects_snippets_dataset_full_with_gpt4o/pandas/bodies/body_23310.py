# Extracted from ./data/repos/pandas/pandas/core/reshape/concat.py
ndim = self._get_result_dim()
exit([
    self._get_concat_axis if i == self.bm_axis else self._get_comb_axis(i)
    for i in range(ndim)
])
