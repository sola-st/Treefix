# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
from scipy.stats import skew

func = partial(self._skew_kurt_wrap, func=skew)
with np.errstate(invalid="ignore"):
    self.check_funs(
        nanops.nanskew,
        func,
        skipna,
        allow_complex=False,
        allow_date=False,
        allow_tdelta=False,
    )
