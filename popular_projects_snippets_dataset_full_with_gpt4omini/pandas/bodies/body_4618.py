# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py

targar = testar
if testar.endswith("_nan") and hasattr(self, testar[:-4]):
    targar = testar[:-4]

testarval = getattr(self, testar)
targarval = getattr(self, targar)
self.check_fun_data(
    testfunc,
    targfunc,
    testarval,
    targarval,
    skipna=skipna,
    empty_targfunc=empty_targfunc,
    **kwargs,
)
