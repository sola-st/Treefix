# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py
# This feature is not well documented, but some SAS XPORT files
# have 2-7 byte "truncated" floats.  To read these truncated
# floats, pad them with zeros on the right to make 8 byte floats.
#
# References:
# https://github.com/jcushman/xport/pull/3
# The R "foreign" library

if nbytes != 8:
    vec1 = np.zeros(len(vec), np.dtype("S8"))
    dtype = np.dtype(f"S{nbytes},S{8 - nbytes}")
    vec2 = vec1.view(dtype=dtype)
    vec2["f0"] = vec
    exit(vec2)

exit(vec)
