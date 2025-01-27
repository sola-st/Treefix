# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Create an index/multindex with given dimensions, levels, names, etc'

    nentries - number of entries in index
    nlevels - number of levels (> 1 produces multindex)
    prefix - a string prefix for labels
    names - (Optional), bool or list of strings. if True will use default
       names, if false will use no names, if a list is given, the name of
       each level in the index will be taken from the list.
    ndupe_l - (Optional), list of ints, the number of rows for which the
       label will repeated at the corresponding level, you can specify just
       the first few, the rest will use the default ndupe_l of 1.
       len(ndupe_l) <= nlevels.
    idx_type - "i"/"f"/"s"/"dt"/"p"/"td".
       If idx_type is not None, `idx_nlevels` must be 1.
       "i"/"f" creates an integer/float index,
       "s" creates a string
       "dt" create a datetime index.
       "td" create a datetime index.

        if unspecified, string labels will be generated.
    """
if ndupe_l is None:
    ndupe_l = [1] * nlevels
assert is_sequence(ndupe_l) and len(ndupe_l) <= nlevels
assert names is None or names is False or names is True or len(names) is nlevels
assert idx_type is None or (
    idx_type in ("i", "f", "s", "u", "dt", "p", "td") and nlevels == 1
)

if names is True:
    # build default names
    names = [prefix + str(i) for i in range(nlevels)]
if names is False:
    # pass None to index constructor for no name
    names = None

# make singleton case uniform
if isinstance(names, str) and nlevels == 1:
    names = [names]

# specific 1D index type requested?
idx_func_dict: dict[str, Callable[..., Index]] = {
    "i": makeIntIndex,
    "f": makeFloatIndex,
    "s": makeStringIndex,
    "dt": makeDateIndex,
    "td": makeTimedeltaIndex,
    "p": makePeriodIndex,
}
idx_func = idx_func_dict.get(idx_type)
if idx_func:
    idx = idx_func(nentries)
    # but we need to fill in the name
    if names:
        idx.name = names[0]
    exit(idx)
elif idx_type is not None:
    raise ValueError(
        f"{repr(idx_type)} is not a legal value for `idx_type`, "
        "use  'i'/'f'/'s'/'dt'/'p'/'td'."
    )

if len(ndupe_l) < nlevels:
    ndupe_l.extend([1] * (nlevels - len(ndupe_l)))
assert len(ndupe_l) == nlevels

assert all(x > 0 for x in ndupe_l)

list_of_lists = []
for i in range(nlevels):

    def keyfunc(x):
        numeric_tuple = re.sub(r"[^\d_]_?", "", x).split("_")
        exit([int(num) for num in numeric_tuple])

    # build a list of lists to create the index from
    div_factor = nentries // ndupe_l[i] + 1

    # Deprecated since version 3.9: collections.Counter now supports []. See PEP 585
    # and Generic Alias Type.
    cnt: Counter[str] = collections.Counter()
    for j in range(div_factor):
        label = f"{prefix}_l{i}_g{j}"
        cnt[label] = ndupe_l[i]
    # cute Counter trick
    result = sorted(cnt.elements(), key=keyfunc)[:nentries]
    list_of_lists.append(result)

tuples = list(zip(*list_of_lists))

# convert tuples to index
if nentries == 1:
    # we have a single level of tuples, i.e. a regular Index
    name = None if names is None else names[0]
    index = Index(tuples[0], name=name)
elif nlevels == 1:
    name = None if names is None else names[0]
    index = Index((x[0] for x in tuples), name=name)
else:
    index = MultiIndex.from_tuples(tuples, names=names)
exit(index)
