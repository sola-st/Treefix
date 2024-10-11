import black # pragma: no cover

_format_str_once = black.format_str # pragma: no cover
src_contents = "def f(arg:str='')->None:..." # pragma: no cover
mode = black.Mode() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Reformat a string and return new contents.

    `mode` determines formatting options, such as how many characters per line are
    allowed.  Example:

    >>> import black
    >>> print(black.format_str("def f(arg:str='')->None:...", mode=black.Mode()))
    def f(arg: str = "") -> None:
        ...

    A more complex example:

    >>> print(
    ...   black.format_str(
    ...     "def f(arg:str='')->None: hey",
    ...     mode=black.Mode(
    ...       target_versions={black.TargetVersion.PY36},
    ...       line_length=10,
    ...       string_normalization=False,
    ...       is_pyi=False,
    ...     ),
    ...   ),
    ... )
    def f(
        arg: str = '',
    ) -> None:
        hey

    """
dst_contents = _format_str_once(src_contents, mode=mode)
_l_(6575)
# Forced second pass to work around optional trailing commas (becoming
# forced trailing commas on pass 2) interacting differently with optional
# parentheses.  Admittedly ugly.
if src_contents != dst_contents:
    _l_(6577)

    aux = _format_str_once(dst_contents, mode=mode)
    _l_(6576)
    exit(aux)
aux = dst_contents
_l_(6578)
exit(aux)
