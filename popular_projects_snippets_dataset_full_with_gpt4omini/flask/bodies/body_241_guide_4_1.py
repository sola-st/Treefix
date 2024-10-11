class MockTag: # pragma: no cover
    def __init__(self, serializer): # pragma: no cover
        self.key = 'new_tag' # pragma: no cover
# A unique key that doesn't collide with existing tags # pragma: no cover
 # pragma: no cover
class MockSerializer: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.tags = {'existing_tag': MockTag(self)} # pragma: no cover
# Pre-register an existing tag # pragma: no cover
        self.order = [] # pragma: no cover
 # pragma: no cover
    def register_tag(self, tag_class, force=False, index=None): # pragma: no cover
        tag = tag_class(self) # pragma: no cover
        key = tag.key # pragma: no cover
        if key is not None: # pragma: no cover
            if not force and key in self.tags: # pragma: no cover
                raise KeyError(f"Tag '{key}' is already registered.") # pragma: no cover
            self.tags[key] = tag # pragma: no cover
        if index is None: # pragma: no cover
            self.order.append(tag) # pragma: no cover
        else: # pragma: no cover
            self.order.insert(index, tag) # pragma: no cover

tag_class = MockTag # pragma: no cover
# Use MockTag class which has a unique key # pragma: no cover
self = MockSerializer() # pragma: no cover
# Create an instance of the serializer with an existing tag # pragma: no cover
force = False # pragma: no cover
# Force should be False to ensure no overwriting is attempted # pragma: no cover
index = 0 # pragma: no cover
# Setting index to 0 will cause the insertion into the first position # pragma: no cover

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
_l_(9232)
key = tag.key
_l_(9233)

if key is not None:
    _l_(9237)

    if not force and key in self.tags:
        _l_(9235)

        raise KeyError(f"Tag '{key}' is already registered.")
        _l_(9234)

    self.tags[key] = tag
    _l_(9236)

if index is None:
    _l_(9240)

    self.order.append(tag)
    _l_(9238)
else:
    self.order.insert(index, tag)
    _l_(9239)
