# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if ragged_tensor.is_ragged(a) or ragged_tensor.is_ragged(b):
    exit(self._assertRaggedClose(a, b, rtol, atol, msg))
path = path or []
path_str = (("[" + "][".join(str(p) for p in path) + "]") if path else "")
msg = msg if msg else ""

# Check if a and/or b are namedtuples.
if hasattr(a, "_asdict"):
    a = a._asdict()
if hasattr(b, "_asdict"):
    b = b._asdict()
a_is_dict = isinstance(a, collections_abc.Mapping)
if a_is_dict != isinstance(b, collections_abc.Mapping):
    raise ValueError("Can't compare dict to non-dict, a%s vs b%s. %s" %
                     (path_str, path_str, msg))
if a_is_dict:
    self.assertItemsEqual(
        a.keys(),
        b.keys(),
        msg="mismatched keys: a%s has keys %s, but b%s has keys %s. %s" %
        (path_str, a.keys(), path_str, b.keys(), msg))
    for k in a:
        path.append(k)
        self._assertAllCloseRecursive(
            a[k], b[k], rtol=rtol, atol=atol, path=path, msg=msg)
        del path[-1]
elif isinstance(a, (list, tuple)):
    # Try to directly compare a, b as ndarrays; if not work, then traverse
    # through the sequence, which is more expensive.
    try:
        (a, b) = self.evaluate_if_both_tensors(a, b)
        a_as_ndarray = self._GetNdArray(a)
        b_as_ndarray = self._GetNdArray(b)
        self._assertArrayLikeAllClose(
            a_as_ndarray,
            b_as_ndarray,
            rtol=rtol,
            atol=atol,
            msg="Mismatched value: a%s is different from b%s. %s" %
            (path_str, path_str, msg))
    except (ValueError, TypeError, NotImplementedError) as e:
        if len(a) != len(b):
            raise ValueError(
                "Mismatched length: a%s has %d items, but b%s has %d items. %s" %
                (path_str, len(a), path_str, len(b), msg))
        for idx, (a_ele, b_ele) in enumerate(zip(a, b)):
            path.append(str(idx))
            self._assertAllCloseRecursive(
                a_ele, b_ele, rtol=rtol, atol=atol, path=path, msg=msg)
            del path[-1]
    # a and b are ndarray like objects
else:
    try:
        self._assertArrayLikeAllClose(
            a,
            b,
            rtol=rtol,
            atol=atol,
            msg=("Mismatched value: a%s is different from b%s. %s" %
                 (path_str, path_str, msg)))
    except TypeError as e:
        msg = ("Error: a%s has %s, but b%s has %s. %s" %
               (path_str, type(a), path_str, type(b), msg))
        e.args = ((e.args[0] + " : " + msg,) + e.args[1:])
        raise
