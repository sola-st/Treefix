# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Create a DataFrame using supplied parameters.

    Parameters
    ----------
    nrows,  ncols - number of data rows/cols
    c_idx_names, r_idx_names  - False/True/list of strings,  yields No names ,
            default names or uses the provided names for the levels of the
            corresponding index. You can provide a single string when
            c_idx_nlevels ==1.
    c_idx_nlevels - number of levels in columns index. > 1 will yield MultiIndex
    r_idx_nlevels - number of levels in rows index. > 1 will yield MultiIndex
    data_gen_f - a function f(row,col) which return the data value
            at that position, the default generator used yields values of the form
            "RxCy" based on position.
    c_ndupe_l, r_ndupe_l - list of integers, determines the number
            of duplicates for each label at a given level of the corresponding
            index. The default `None` value produces a multiplicity of 1 across
            all levels, i.e. a unique index. Will accept a partial list of length
            N < idx_nlevels, for just the first N levels. If ndupe doesn't divide
            nrows/ncol, the last label might have lower multiplicity.
    dtype - passed to the DataFrame constructor as is, in case you wish to
            have more control in conjunction with a custom `data_gen_f`
    r_idx_type, c_idx_type -  "i"/"f"/"s"/"dt"/"td".
        If idx_type is not None, `idx_nlevels` must be 1.
        "i"/"f" creates an integer/float index,
        "s" creates a string index
        "dt" create a datetime index.
        "td" create a timedelta index.

            if unspecified, string labels will be generated.

    Examples
    --------
    # 5 row, 3 columns, default names on both, single index on both axis
    >> makeCustomDataframe(5,3)

    # make the data a random int between 1 and 100
    >> mkdf(5,3,data_gen_f=lambda r,c:randint(1,100))

    # 2-level multiindex on rows with each label duplicated
    # twice on first level, default names on both axis, single
    # index on both axis
    >> a=makeCustomDataframe(5,3,r_idx_nlevels=2,r_ndupe_l=[2])

    # DatetimeIndex on row, index with unicode labels on columns
    # no names on either axis
    >> a=makeCustomDataframe(5,3,c_idx_names=False,r_idx_names=False,
                             r_idx_type="dt",c_idx_type="u")

    # 4-level multindex on rows with names provided, 2-level multindex
    # on columns with default labels and default names.
    >> a=makeCustomDataframe(5,3,r_idx_nlevels=4,
                             r_idx_names=["FEE","FIH","FOH","FUM"],
                             c_idx_nlevels=2)

    >> a=mkdf(5,3,r_idx_nlevels=2,c_idx_nlevels=4)
    """
assert c_idx_nlevels > 0
assert r_idx_nlevels > 0
assert r_idx_type is None or (
    r_idx_type in ("i", "f", "s", "dt", "p", "td") and r_idx_nlevels == 1
)
assert c_idx_type is None or (
    c_idx_type in ("i", "f", "s", "dt", "p", "td") and c_idx_nlevels == 1
)

columns = makeCustomIndex(
    ncols,
    nlevels=c_idx_nlevels,
    prefix="C",
    names=c_idx_names,
    ndupe_l=c_ndupe_l,
    idx_type=c_idx_type,
)
index = makeCustomIndex(
    nrows,
    nlevels=r_idx_nlevels,
    prefix="R",
    names=r_idx_names,
    ndupe_l=r_ndupe_l,
    idx_type=r_idx_type,
)

# by default, generate data based on location
if data_gen_f is None:
    data_gen_f = lambda r, c: f"R{r}C{c}"

data = [[data_gen_f(r, c) for c in range(ncols)] for r in range(nrows)]

exit(DataFrame(data, index, columns, dtype=dtype))
