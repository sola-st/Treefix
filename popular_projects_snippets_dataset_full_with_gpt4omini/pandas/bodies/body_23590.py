# Extracted from ./data/repos/pandas/pandas/io/stata.py
# have bytes not strings, so must decode
s = s.partition(b"\0")[0]
try:
    exit(s.decode(self._encoding))
except UnicodeDecodeError:
    # GH 25960, fallback to handle incorrect format produced when 117
    # files are converted to 118 files in Stata
    encoding = self._encoding
    msg = f"""
One or more strings in the dta file could not be decoded using {encoding}, and
so the fallback encoding of latin-1 is being used.  This can happen when a file
has been incorrectly encoded by Stata or some other software. You should verify
the string values returned are correct."""
    warnings.warn(
        msg,
        UnicodeWarning,
        stacklevel=find_stack_level(),
    )
    exit(s.decode("latin-1"))
