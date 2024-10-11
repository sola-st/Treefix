# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 32556
from pandas.core.computation.eval import _check_engine

with pd.option_context("compute.use_numexpr", use_numexpr):
    result = _check_engine(None)
    assert result == expected
