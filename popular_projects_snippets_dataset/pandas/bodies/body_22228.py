# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
self.level = level
self._orig_grouper = grouper
self.grouping_vector = _convert_grouper(index, grouper)
self._all_grouper = None
self._orig_cats = None
self._index = index
self._sort = sort
self.obj = obj
self._observed = observed
self.in_axis = in_axis
self._dropna = dropna
self._uniques = uniques

self._passed_categorical = False

# we have a single grouper which may be a myriad of things,
# some of which are dependent on the passing in level

ilevel = self._ilevel
if ilevel is not None:
    # In extant tests, the new self.grouping_vector matches
    #  `index.get_level_values(ilevel)` whenever
    #  mapper is None and isinstance(index, MultiIndex)
    if isinstance(index, MultiIndex):
        index_level = index.get_level_values(ilevel)
    else:
        index_level = index

    if self.grouping_vector is None:
        self.grouping_vector = index_level
    else:
        mapper = self.grouping_vector
        self.grouping_vector = index_level.map(mapper)

        # a passed Grouper like, directly get the grouper in the same way
        # as single grouper groupby, use the group_info to get codes
elif isinstance(self.grouping_vector, Grouper):
    # get the new grouper; we already have disambiguated
    # what key/level refer to exactly, don't need to
    # check again as we have by this point converted these
    # to an actual value (rather than a pd.Grouper)
    assert self.obj is not None  # for mypy
    _, newgrouper, newobj = self.grouping_vector._get_grouper(
        self.obj, validate=False
    )
    self.obj = newobj

    ng = newgrouper._get_grouper()
    if isinstance(newgrouper, ops.BinGrouper):
        # in this case we have `ng is newgrouper`
        self.grouping_vector = ng
    else:
        # ops.BaseGrouper
        # use Index instead of ndarray so we can recover the name
        self.grouping_vector = Index(ng, name=newgrouper.result_index.name)

elif not isinstance(
    self.grouping_vector, (Series, Index, ExtensionArray, np.ndarray)
):
    # no level passed
    if getattr(self.grouping_vector, "ndim", 1) != 1:
        t = self.name or str(type(self.grouping_vector))
        raise ValueError(f"Grouper for '{t}' not 1-dimensional")

    self.grouping_vector = index.map(self.grouping_vector)

    if not (
        hasattr(self.grouping_vector, "__len__")
        and len(self.grouping_vector) == len(index)
    ):
        grper = pprint_thing(self.grouping_vector)
        errmsg = (
            "Grouper result violates len(labels) == "
            f"len(data)\nresult: {grper}"
        )
        self.grouping_vector = None  # Try for sanity
        raise AssertionError(errmsg)

if isinstance(self.grouping_vector, np.ndarray):
    if self.grouping_vector.dtype.kind in ["m", "M"]:
        # if we have a date/time-like grouper, make sure that we have
        # Timestamps like
        # TODO 2022-10-08 we only have one test that gets here and
        #  values are already in nanoseconds in that case.
        self.grouping_vector = Series(self.grouping_vector).to_numpy()
elif is_categorical_dtype(self.grouping_vector):
    # a passed Categorical
    self._passed_categorical = True

    self._orig_cats = self.grouping_vector.categories
    self.grouping_vector, self._all_grouper = recode_for_groupby(
        self.grouping_vector, sort, observed
    )
