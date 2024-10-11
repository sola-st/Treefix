tag_class = type('TagClass', (object,), {'__init__': lambda self, serializer: setattr(self, 'key', 'example_key')}) # pragma: no cover
self = type('MockSerializer', (object,), {'tags': {}, 'order': []})() # pragma: no cover
force = False # pragma: no cover
index = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Register a new tag with this serializer.

        :param tag_class: tag class to register. Will be instantiated with this
            serializer instance.
        :param force: overwrite an existing tag. If false (default), a
            :exc:`KeyError` is raised.
        :param index: index to insert the new tag in the tag order. Useful when
            the new tag is a special case of an existing tag. If ``None``
            (default), the tag is appended to the end of the order.

        :raise KeyError: if the tag key is already registered and ``force`` is
            not true.
        """
tag = tag_class(self)
_l_(22967)
key = tag.key
_l_(22968)

if key is not None:
    _l_(22972)

    if not force and key in self.tags:
        _l_(22970)

        raise KeyError(f"Tag '{key}' is already registered.")
        _l_(22969)

    self.tags[key] = tag
    _l_(22971)

if index is None:
    _l_(22975)

    self.order.append(tag)
    _l_(22973)
else:
    self.order.insert(index, tag)
    _l_(22974)
