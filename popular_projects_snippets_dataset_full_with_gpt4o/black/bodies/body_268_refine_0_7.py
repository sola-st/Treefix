import ast # pragma: no cover

class MagicFinder:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magics = {1: [type('Mock', (object,), {'col_offset': 0, 'magic': "%matplotlib inline"})()]}# pragma: no cover
    def visit(self, parsed_ast):# pragma: no cover
        pass # pragma: no cover
src = '''get_ipython().run_line_magic('%matplotlib', 'inline')# pragma: no cover
'foo' ''' # pragma: no cover
def get_token(src, magic):# pragma: no cover
    return "5e67db56d490fd39" # pragma: no cover
class Replacement:# pragma: no cover
    def __init__(self, mask, src):# pragma: no cover
        self.mask = mask# pragma: no cover
        self.src = src # pragma: no cover

import ast # pragma: no cover

class MagicFinder:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magics = {1: [type('Mock', (object,), {'col_offset': 0, 'magic': "%matplotlib inline"})()]}# pragma: no cover
    def visit(self, parsed_ast):# pragma: no cover
        pass # pragma: no cover
src = """get_ipython().run_line_magic('%matplotlib', 'inline')# pragma: no cover
'foo'# pragma: no cover
""" # pragma: no cover
def get_token(src, magic):# pragma: no cover
    return "5e67db56d490fd39" # pragma: no cover
class Replacement:# pragma: no cover
    def __init__(self, mask, src):# pragma: no cover
        self.mask = mask# pragma: no cover
        self.src = src # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Replace magics within body of cell.

    Note that 'src' will already have been processed by IPython's
    TransformerManager().transform_cell.

    Example, this

        get_ipython().run_line_magic('matplotlib', 'inline')
        'foo'

    becomes

        "5e67db56d490fd39"
        'foo'

    The replacement, along with the transformed code, are returned.
    """
replacements = []
_l_(17619)
magic_finder = MagicFinder()
_l_(17620)
magic_finder.visit(ast.parse(src))
_l_(17621)
new_srcs = []
_l_(17622)
for i, line in enumerate(src.splitlines(), start=1):
    _l_(17632)

    if i in magic_finder.magics:
        _l_(17630)

        offsets_and_magics = magic_finder.magics[i]
        _l_(17623)
        if len(offsets_and_magics) != 1:
            _l_(17625)

            raise AssertionError(
                f"Expecting one magic per line, got: {offsets_and_magics}\n"
                "Please report a bug on https://github.com/psf/black/issues."
            )
            _l_(17624)
        col_offset, magic = (
            offsets_and_magics[0].col_offset,
            offsets_and_magics[0].magic,
        )
        _l_(17626)
        mask = get_token(src, magic)
        _l_(17627)
        replacements.append(Replacement(mask=mask, src=magic))
        _l_(17628)
        line = line[:col_offset] + mask
        _l_(17629)
    new_srcs.append(line)
    _l_(17631)
aux = ("\n".join(new_srcs), replacements)
_l_(17633)
exit(aux)
