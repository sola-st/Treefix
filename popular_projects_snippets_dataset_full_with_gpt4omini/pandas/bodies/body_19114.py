# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
# set/unset to use numexpr
global USE_NUMEXPR
if NUMEXPR_INSTALLED:
    USE_NUMEXPR = v

# choose what we are going to do
global _evaluate, _where

_evaluate = _evaluate_numexpr if USE_NUMEXPR else _evaluate_standard
_where = _where_numexpr if USE_NUMEXPR else _where_standard
