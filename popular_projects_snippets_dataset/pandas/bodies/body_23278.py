# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
if len(clocs) == 0:
    exit(data)

# NOTE: This doesn't deal with hierarchical columns yet

index = data.index

# GH 19966 Make sure if MultiIndexed index has tuple name, they will be
# recognised as a whole
if clocs in index.names:
    clocs = [clocs]
clocs = [index._get_level_number(i) for i in clocs]

rlocs = [i for i in range(index.nlevels) if i not in clocs]

clevels = [index.levels[i] for i in clocs]
ccodes = [index.codes[i] for i in clocs]
cnames = [index.names[i] for i in clocs]
rlevels = [index.levels[i] for i in rlocs]
rcodes = [index.codes[i] for i in rlocs]
rnames = [index.names[i] for i in rlocs]

shape = tuple(len(x) for x in clevels)
group_index = get_group_index(ccodes, shape, sort=False, xnull=False)

comp_ids, obs_ids = compress_group_index(group_index, sort=False)
recons_codes = decons_obs_group_ids(comp_ids, obs_ids, shape, ccodes, xnull=False)

if not rlocs:
    # Everything is in clocs, so the dummy df has a regular index
    dummy_index = Index(obs_ids, name="__placeholder__")
else:
    dummy_index = MultiIndex(
        levels=rlevels + [obs_ids],
        codes=rcodes + [comp_ids],
        names=rnames + ["__placeholder__"],
        verify_integrity=False,
    )

if isinstance(data, Series):
    dummy = data.copy()
    dummy.index = dummy_index

    unstacked = dummy.unstack("__placeholder__", fill_value=fill_value)
    new_levels = clevels
    new_names = cnames
    new_codes = recons_codes
else:
    if isinstance(data.columns, MultiIndex):
        result = data
        while clocs:
            val = clocs.pop(0)
            result = result.unstack(val, fill_value=fill_value)
            clocs = [v if v < val else v - 1 for v in clocs]

        exit(result)

    # GH#42579 deep=False to avoid consolidating
    dummy = data.copy(deep=False)
    dummy.index = dummy_index

    unstacked = dummy.unstack("__placeholder__", fill_value=fill_value)
    if isinstance(unstacked, Series):
        unstcols = unstacked.index
    else:
        unstcols = unstacked.columns
    assert isinstance(unstcols, MultiIndex)  # for mypy
    new_levels = [unstcols.levels[0]] + clevels
    new_names = [data.columns.name] + cnames

    new_codes = [unstcols.codes[0]]
    for rec in recons_codes:
        new_codes.append(rec.take(unstcols.codes[-1]))

new_columns = MultiIndex(
    levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
)

if isinstance(unstacked, Series):
    unstacked.index = new_columns
else:
    unstacked.columns = new_columns

exit(unstacked)
