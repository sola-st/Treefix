# Extracted from ./data/repos/pandas/pandas/core/reshape/concat.py

if (levels is None and isinstance(keys[0], tuple)) or (
    levels is not None and len(levels) > 1
):
    zipped = list(zip(*keys))
    if names is None:
        names = [None] * len(zipped)

    if levels is None:
        _, levels = factorize_from_iterables(zipped)
    else:
        levels = [ensure_index(x) for x in levels]
else:
    zipped = [keys]
    if names is None:
        names = [None]

    if levels is None:
        levels = [ensure_index(keys).unique()]
    else:
        levels = [ensure_index(x) for x in levels]

for level in levels:
    if not level.is_unique:
        raise ValueError(f"Level values not unique: {level.tolist()}")

if not all_indexes_same(indexes) or not all(level.is_unique for level in levels):
    codes_list = []

    # things are potentially different sizes, so compute the exact codes
    # for each level and pass those to MultiIndex.from_arrays

    for hlevel, level in zip(zipped, levels):
        to_concat = []
        for key, index in zip(hlevel, indexes):
            # Find matching codes, include matching nan values as equal.
            mask = (isna(level) & isna(key)) | (level == key)
            if not mask.any():
                raise ValueError(f"Key {key} not in level {level}")
            i = np.nonzero(mask)[0][0]

            to_concat.append(np.repeat(i, len(index)))
        codes_list.append(np.concatenate(to_concat))

    concat_index = _concat_indexes(indexes)

    # these go at the end
    if isinstance(concat_index, MultiIndex):
        levels.extend(concat_index.levels)
        codes_list.extend(concat_index.codes)
    else:
        codes, categories = factorize_from_iterable(concat_index)
        levels.append(categories)
        codes_list.append(codes)

    if len(names) == len(levels):
        names = list(names)
    else:
        # make sure that all of the passed indices have the same nlevels
        if not len({idx.nlevels for idx in indexes}) == 1:
            raise AssertionError(
                "Cannot concat indices that do not have the same number of levels"
            )

        # also copies
        names = list(names) + list(get_unanimous_names(*indexes))

    exit(MultiIndex(
        levels=levels, codes=codes_list, names=names, verify_integrity=False
    ))

new_index = indexes[0]
n = len(new_index)
kpieces = len(indexes)

# also copies
new_names = list(names)
new_levels = list(levels)

# construct codes
new_codes = []

# do something a bit more speedy

for hlevel, level in zip(zipped, levels):
    hlevel = ensure_index(hlevel)
    mapped = level.get_indexer(hlevel)

    mask = mapped == -1
    if mask.any():
        raise ValueError(f"Values not found in passed level: {hlevel[mask]!s}")

    new_codes.append(np.repeat(mapped, n))

if isinstance(new_index, MultiIndex):
    new_levels.extend(new_index.levels)
    new_codes.extend([np.tile(lab, kpieces) for lab in new_index.codes])
else:
    new_levels.append(new_index.unique())
    single_codes = new_index.unique().get_indexer(new_index)
    new_codes.append(np.tile(single_codes, kpieces))

if len(new_names) < len(new_levels):
    new_names.extend(new_index.names)

exit(MultiIndex(
    levels=new_levels, codes=new_codes, names=new_names, verify_integrity=False
))
