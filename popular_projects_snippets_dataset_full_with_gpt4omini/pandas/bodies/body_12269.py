# Extracted from ./data/repos/pandas/pandas/tests/io/generate_legacy_storage_files.py
exit("_".join(
    [
        str(pandas.__version__),
        str(pl.machine()),
        str(pl.system().lower()),
        str(pl.python_version()),
    ]
))
