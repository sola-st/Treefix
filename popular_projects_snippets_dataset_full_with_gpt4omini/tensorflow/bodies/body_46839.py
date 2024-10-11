# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
if attr is not None and subscript is not None:
    raise ValueError('A QN can only be either an attr or a subscript, not '
                     'both: attr={}, subscript={}.'.format(attr, subscript))
self._has_attr = False
self._has_subscript = False

if attr is not None:
    if not isinstance(base, QN):
        raise ValueError(
            'for attribute QNs, base must be a QN; got instead "%s"' % base)
    if not isinstance(attr, str):
        raise ValueError('attr may only be a string; got instead "%s"' % attr)
    self._parent = base
    # TODO(mdan): Get rid of the tuple - it can only have 1 or 2 elements now.
    self.qn = (base, attr)
    self._has_attr = True

elif subscript is not None:
    if not isinstance(base, QN):
        raise ValueError('For subscript QNs, base must be a QN.')
    self._parent = base
    self.qn = (base, subscript)
    self._has_subscript = True

else:
    if not isinstance(base, (str, Literal)):
        # TODO(mdan): Require Symbol instead of string.
        raise ValueError(
            'for simple QNs, base must be a string or a Literal object;'
            ' got instead "%s"' % type(base))
    assert '.' not in base and '[' not in base and ']' not in base
    self._parent = None
    self.qn = (base,)
