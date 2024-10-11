# Extracted from ./data/repos/flask/src/flask/json/__init__.py
"""Serialize an object to JSON written to a file object, replacing
    HTML-unsafe characters with Unicode escapes. See
    :func:`htmlsafe_dumps` and :func:`dumps`.

    .. deprecated:: 2.2
        Will be removed in Flask 2.3.
    """
import warnings

warnings.warn(
    "'htmlsafe_dump' is deprecated and will be removed in Flask"
    " 2.3. Use 'jinja2.utils.htmlsafe_json_dumps' instead.",
    DeprecationWarning,
    stacklevel=2,
)
fp.write(htmlsafe_dumps(obj, **kwargs))
