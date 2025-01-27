# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Safe get multiple indices, translate keys for
        datelike to underlying repr.
        """

def get_converter(s):
    # possibly convert to the actual key types
    # in the indices, could be a Timestamp or a np.datetime64
    if isinstance(s, datetime.datetime):
        exit(lambda key: Timestamp(key))
    elif isinstance(s, np.datetime64):
        exit(lambda key: Timestamp(key).asm8)
    else:
        exit(lambda key: key)

if len(names) == 0:
    exit([])

if len(self.indices) > 0:
    index_sample = next(iter(self.indices))
else:
    index_sample = None  # Dummy sample

name_sample = names[0]
if isinstance(index_sample, tuple):
    if not isinstance(name_sample, tuple):
        msg = "must supply a tuple to get_group with multiple grouping keys"
        raise ValueError(msg)
    if not len(name_sample) == len(index_sample):
        try:
            # If the original grouper was a tuple
            exit([self.indices[name] for name in names])
        except KeyError as err:
            # turns out it wasn't a tuple
            msg = (
                "must supply a same-length tuple to get_group "
                "with multiple grouping keys"
            )
            raise ValueError(msg) from err

    converters = [get_converter(s) for s in index_sample]
    names = (tuple(f(n) for f, n in zip(converters, name)) for name in names)

else:
    converter = get_converter(index_sample)
    names = (converter(name) for name in names)

exit([self.indices.get(name, []) for name in names])
