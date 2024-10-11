# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# Expect different error messages from get_engine(engine="auto")
# if engines aren't installed vs. are installed but bad version
from pandas.compat._optional import VERSIONS

# Do we have engines installed, but a bad version of them?
pa_min_ver = VERSIONS.get("pyarrow")
fp_min_ver = VERSIONS.get("fastparquet")
have_pa_bad_version = (
    False
    if not _HAVE_PYARROW
    else Version(pyarrow.__version__) < Version(pa_min_ver)
)
have_fp_bad_version = (
    False
    if not _HAVE_FASTPARQUET
    else Version(fastparquet.__version__) < Version(fp_min_ver)
)
# Do we have usable engines installed?
have_usable_pa = _HAVE_PYARROW and not have_pa_bad_version
have_usable_fp = _HAVE_FASTPARQUET and not have_fp_bad_version

if not have_usable_pa and not have_usable_fp:
    # No usable engines found.
    if have_pa_bad_version:
        match = f"Pandas requires version .{pa_min_ver}. or newer of .pyarrow."
        with pytest.raises(ImportError, match=match):
            get_engine("auto")
    else:
        match = "Missing optional dependency .pyarrow."
        with pytest.raises(ImportError, match=match):
            get_engine("auto")

    if have_fp_bad_version:
        match = f"Pandas requires version .{fp_min_ver}. or newer of .fastparquet."
        with pytest.raises(ImportError, match=match):
            get_engine("auto")
    else:
        match = "Missing optional dependency .fastparquet."
        with pytest.raises(ImportError, match=match):
            get_engine("auto")
