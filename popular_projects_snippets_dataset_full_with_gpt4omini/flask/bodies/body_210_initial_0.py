import json # pragma: no cover
from markupsafe import Markup # pragma: no cover

_jinja_htmlsafe_dumps = lambda obj, dumps, **kwargs: Markup(json.dumps(obj, **kwargs)) # pragma: no cover
obj = {'key': 'value', 'html': '<div>Example</div>'} # pragma: no cover
dumps = json.dumps # pragma: no cover
kwargs = {'ensure_ascii': False} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/__init__.py
from l3.Runtime import _l_
"""Serialize an object to a string of JSON with :func:`dumps`, then
    replace HTML-unsafe characters with Unicode escapes and mark the
    result safe with :class:`~markupsafe.Markup`.

    This is available in templates as the ``|tojson`` filter.

    The returned string is safe to render in HTML documents and
    ``<script>`` tags. The exception is in HTML attributes that are
    double quoted; either use single quotes or the ``|forceescape``
    filter.

    .. deprecated:: 2.2
        Will be removed in Flask 2.3. This is built-in to Jinja now.

    .. versionchanged:: 2.0
        Uses :func:`jinja2.utils.htmlsafe_json_dumps`. The returned
        value is marked safe by wrapping in :class:`~markupsafe.Markup`.

    .. versionchanged:: 0.10
        Single quotes are escaped, making this safe to use in HTML,
        ``<script>`` tags, and single-quoted attributes without further
        escaping.
    """
try:
    import warnings
    _l_(6858)

except ImportError:
    pass

warnings.warn(
    "'htmlsafe_dumps' is deprecated and will be removed in Flask"
    " 2.3. Use 'jinja2.utils.htmlsafe_json_dumps' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(6859)
aux = _jinja_htmlsafe_dumps(obj, dumps=dumps, **kwargs)
_l_(6860)
exit(aux)
