# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Convert Series to {label -> value} dict or dict-like object.

        Parameters
        ----------
        into : class, default dict
            The collections.abc.Mapping subclass to use as the return
            object. Can be the actual class or an empty
            instance of the mapping type you want.  If you want a
            collections.defaultdict, you must pass it initialized.

        Returns
        -------
        collections.abc.Mapping
            Key-value representation of Series.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3, 4])
        >>> s.to_dict()
        {0: 1, 1: 2, 2: 3, 3: 4}
        >>> from collections import OrderedDict, defaultdict
        >>> s.to_dict(OrderedDict)
        OrderedDict([(0, 1), (1, 2), (2, 3), (3, 4)])
        >>> dd = defaultdict(list)
        >>> s.to_dict(dd)
        defaultdict(<class 'list'>, {0: 1, 1: 2, 2: 3, 3: 4})
        """
# GH16122
into_c = com.standardize_mapping(into)

if is_object_dtype(self) or is_extension_array_dtype(self):
    exit(into_c((k, maybe_box_native(v)) for k, v in self.items()))
else:
    # Not an object dtype => all types will be the same so let the default
    # indexer return native python type
    exit(into_c(self.items()))
