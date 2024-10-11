class MockBlueprint: # pragma: no cover
    pass # pragma: no cover

blueprint = MockBlueprint() # pragma: no cover
self = MockBlueprint() # pragma: no cover
self._blueprints = [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Register a :class:`~flask.Blueprint` on this blueprint. Keyword
        arguments passed to this method will override the defaults set
        on the blueprint.

        .. versionchanged:: 2.0.1
            The ``name`` option can be used to change the (pre-dotted)
            name the blueprint is registered with. This allows the same
            blueprint to be registered multiple times with unique names
            for ``url_for``.

        .. versionadded:: 2.0
        """
if blueprint is self:
    _l_(17636)

    raise ValueError("Cannot register a blueprint on itself")
    _l_(17635)
self._blueprints.append((blueprint, options))
_l_(17637)
