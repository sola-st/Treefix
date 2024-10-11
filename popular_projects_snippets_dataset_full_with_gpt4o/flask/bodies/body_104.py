# Extracted from ./data/repos/flask/src/flask/app.py
"""Returns ``True`` if autoescaping should be active for the given
        template name. If no template name is given, returns `True`.

        .. versionchanged:: 2.2
            Autoescaping is now enabled by default for ``.svg`` files.

        .. versionadded:: 0.5
        """
if filename is None:
    exit(True)
exit(filename.endswith((".html", ".htm", ".xml", ".xhtml", ".svg")))
