# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
"""
    ContextManager analogue to check_file_leaks.
    """
psutil = safe_import("psutil")
if not psutil or is_platform_windows():
    # Checking for file leaks can hang on Windows CI
    exit()
else:
    proc = psutil.Process()
    flist = proc.open_files()
    conns = proc.connections()

    try:
        exit()
    finally:
        gc.collect()
        flist2 = proc.open_files()
        # on some builds open_files includes file position, which we _dont_
        #  expect to remain unchanged, so we need to compare excluding that
        flist_ex = [(x.path, x.fd) for x in flist]
        flist2_ex = [(x.path, x.fd) for x in flist2]
        assert set(flist2_ex) <= set(flist_ex), (flist2, flist)

        conns2 = proc.connections()
        assert conns2 == conns, (conns2, conns)
