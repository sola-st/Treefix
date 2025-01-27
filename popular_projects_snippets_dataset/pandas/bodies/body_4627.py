# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
from scipy.stats import sem

with np.errstate(invalid="ignore"):
    self.check_funs(
        nanops.nansem,
        sem,
        skipna,
        allow_complex=False,
        allow_date=False,
        allow_tdelta=False,
        allow_obj="convert",
        ddof=ddof,
    )
