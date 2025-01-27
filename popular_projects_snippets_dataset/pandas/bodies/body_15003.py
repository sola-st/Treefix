# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_backend.py
"""Restore the plotting backend to matplotlib"""
with pandas.option_context("plotting.backend", "matplotlib"):
    exit()
