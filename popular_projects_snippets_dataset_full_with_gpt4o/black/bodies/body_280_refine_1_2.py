from typing import Final # pragma: no cover

leaf = type('MockLeaf', (object,), {'type': 'MOCK_DEFAULT', 'parent': None, 'value': 'MOCK_DEFAULT', 'prev_sibling': None, 'prefix': ''})() # pragma: no cover
ALWAYS_NO_SPACE = {0} # pragma: no cover
token = type('MockToken', (object,), {'COMMENT': 'COMMENT', 'COLON': 'COLON', 'COMMA': 'COMMA', 'EQUAL': 'EQUAL', 'STAR': 'STAR', 'AT': 'AT', 'LPAR': 'LPAR', 'RPAR': 'RPAR', 'DOT': 'DOT', 'LSQB': 'LSQB', 'DOUBLESTAR': 'DOUBLESTAR', 'NAME': 'NAME', 'NUMBER': 'NUMBER', 'STRING': 'STRING'}) # pragma: no cover
preceding_leaf = lambda x: None # pragma: no cover
OPENING_BRACKETS = {token.LPAR, token.LSQB} # pragma: no cover
complex_subscript = False # pragma: no cover
parent_type = lambda x: 'MOCK_DEFAULT' # pragma: no cover
VARARGS_SPECIALS = {token.STAR} # pragma: no cover
is_vararg = lambda x, within: False # pragma: no cover
VARARGS_PARENTS = {'MOCK_PARENT'} # pragma: no cover
UNPACKING_PARENTS = {'MOCK_PARENT'} # pragma: no cover
MATH_OPERATORS = {'+', '-', '*', '/', '//', '=', '%'} # pragma: no cover
TYPED_NAMES = {'int', 'float', 'str', 'list', 'dict'} # pragma: no cover

from typing import Final # pragma: no cover

MockParent = type('MockParent', (object,), {'type': 'MOCK_PARENT_TYPE'}) # pragma: no cover
MockLeaf = type('MockLeaf', (object,), {'type': 'MOCK_DEFAULT', 'parent': MockParent(), 'value': 'MOCK_DEFAULT', 'prev_sibling': None, 'prefix': ''}) # pragma: no cover
leaf = MockLeaf() # pragma: no cover
ALWAYS_NO_SPACE = {0} # pragma: no cover
token = type('MockToken', (object,), {'COMMENT': 'COMMENT', 'COLON': 'COLON', 'COMMA': 'COMMA', 'EQUAL': 'EQUAL', 'STAR': 'STAR', 'AT': 'AT', 'LPAR': 'LPAR', 'RPAR': 'RPAR', 'DOT': 'DOT', 'LSQB': 'LSQB', 'DOUBLESTAR': 'DOUBLESTAR', 'NAME': 'NAME', 'NUMBER': 'NUMBER', 'STRING': 'STRING'}) # pragma: no cover
preceding_leaf = lambda x: None # pragma: no cover
OPENING_BRACKETS = {token.LPAR, token.LSQB} # pragma: no cover
complex_subscript = False # pragma: no cover
parent_type = lambda x: 'MOCK_DEFAULT' # pragma: no cover
VARARGS_SPECIALS = {token.STAR} # pragma: no cover
is_vararg = lambda x, within: False # pragma: no cover
VARARGS_PARENTS = {'MOCK_PARENT'} # pragma: no cover
UNPACKING_PARENTS = {'MOCK_PARENT'} # pragma: no cover
MATH_OPERATORS = {'+', '-', '*', '/', '//', '=', '%'} # pragma: no cover
TYPED_NAMES = {'int', 'float', 'str', 'list', 'dict'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return whitespace prefix if needed for the given `leaf`.

    `complex_subscript` signals whether the given leaf is part of a subscription
    which has non-trivial arguments, like arithmetic expressions or function calls.
    """
NO: Final = ""
_l_(19840)
SPACE: Final = " "
_l_(19841)
DOUBLESPACE: Final = "  "
_l_(19842)
t = leaf.type
_l_(19843)
p = leaf.parent
_l_(19844)
v = leaf.value
_l_(19845)
if t in ALWAYS_NO_SPACE:
    _l_(19847)

    aux = NO
    _l_(19846)
    exit(aux)

if t == token.COMMENT:
    _l_(19849)

    aux = DOUBLESPACE
    _l_(19848)
    exit(aux)

assert p is not None, f"INTERNAL ERROR: hand-made leaf without parent: {leaf!r}"
_l_(19850)
if t == token.COLON and p.type not in {
    syms.subscript,
    syms.subscriptlist,
    syms.sliceop,
}:
    _l_(19852)

    aux = NO
    _l_(19851)
    exit(aux)

prev = leaf.prev_sibling
_l_(19853)
if not prev:
    _l_(19883)

    prevp = preceding_leaf(p)
    _l_(19854)
    if not prevp or prevp.type in OPENING_BRACKETS:
        _l_(19856)

        aux = NO
        _l_(19855)
        exit(aux)

    if t == token.COLON:
        _l_(19862)

        if prevp.type == token.COLON:
            _l_(19860)

            aux = NO
            _l_(19857)
            exit(aux)

        elif prevp.type != token.COMMA and not complex_subscript:
            _l_(19859)

            aux = NO
            _l_(19858)
            exit(aux)
        aux = SPACE
        _l_(19861)

        exit(aux)

    if prevp.type == token.EQUAL:
        _l_(19880)

        if prevp.parent:
            _l_(19867)

            if prevp.parent.type in {
                syms.arglist,
                syms.argument,
                syms.parameters,
                syms.varargslist,
            }:
                _l_(19866)

                aux = NO
                _l_(19863)
                exit(aux)

            elif prevp.parent.type == syms.typedargslist:
                _l_(19865)

                aux = prevp.prefix
                _l_(19864)
                # A bit hacky: if the equal sign has whitespace, it means we
                # previously found it's a typed argument.  So, we're using
                # that, too.
                exit(aux)

    elif (
        prevp.type == token.STAR
        and parent_type(prevp) == syms.star_expr
        and parent_type(prevp.parent) == syms.subscriptlist
    ):
        _l_(19879)

        aux = NO
        _l_(19868)
        # No space between typevar tuples.
        exit(aux)

    elif prevp.type in VARARGS_SPECIALS:
        _l_(19878)

        if is_vararg(prevp, within=VARARGS_PARENTS | UNPACKING_PARENTS):
            _l_(19870)

            aux = NO
            _l_(19869)
            exit(aux)

    elif prevp.type == token.COLON:
        _l_(19877)

        if prevp.parent and prevp.parent.type in {syms.subscript, syms.sliceop}:
            _l_(19872)

            aux = SPACE if complex_subscript else NO
            _l_(19871)
            exit(aux)

    elif (
        prevp.parent
        and prevp.parent.type == syms.factor
        and prevp.type in MATH_OPERATORS
    ):
        _l_(19876)

        aux = NO
        _l_(19873)
        exit(aux)

    elif prevp.type == token.AT and p.parent and p.parent.type == syms.decorator:
        _l_(19875)

        aux = NO
        _l_(19874)
        # no space in decorators
        exit(aux)

elif prev.type in OPENING_BRACKETS:
    _l_(19882)

    aux = NO
    _l_(19881)
    exit(aux)

if p.type in {syms.parameters, syms.arglist}:
    _l_(19975)

    # untyped function signatures or calls
    if not prev or prev.type != token.COMMA:
        _l_(19885)

        aux = NO
        _l_(19884)
        exit(aux)

elif p.type == syms.varargslist:
    _l_(19974)

    # lambdas
    if prev and prev.type != token.COMMA:
        _l_(19887)

        aux = NO
        _l_(19886)
        exit(aux)

elif p.type == syms.typedargslist:
    _l_(19973)

    # typed function signatures
    if not prev:
        _l_(19889)

        aux = NO
        _l_(19888)
        exit(aux)

    if t == token.EQUAL:
        _l_(19896)

        if prev.type not in TYPED_NAMES:
            _l_(19891)

            aux = NO
            _l_(19890)
            exit(aux)

    elif prev.type == token.EQUAL:
        _l_(19895)

        aux = prev.prefix
        _l_(19892)
        # A bit hacky: if the equal sign has whitespace, it means we
        # previously found it's a typed argument.  So, we're using that, too.
        exit(aux)

    elif prev.type != token.COMMA:
        _l_(19894)

        aux = NO
        _l_(19893)
        exit(aux)

elif p.type in TYPED_NAMES:
    _l_(19972)

    # type names
    if not prev:
        _l_(19900)

        prevp = preceding_leaf(p)
        _l_(19897)
        if not prevp or prevp.type != token.COMMA:
            _l_(19899)

            aux = NO
            _l_(19898)
            exit(aux)

elif p.type == syms.trailer:
    _l_(19971)

    # attributes and calls
    if t == token.LPAR or t == token.RPAR:
        _l_(19902)

        aux = NO
        _l_(19901)
        exit(aux)

    if not prev:
        _l_(19907)

        if t == token.DOT or t == token.LSQB:
            _l_(19904)

            aux = NO
            _l_(19903)
            exit(aux)

    elif prev.type != token.COMMA:
        _l_(19906)

        aux = NO
        _l_(19905)
        exit(aux)

elif p.type == syms.argument:
    _l_(19970)

    # single argument
    if t == token.EQUAL:
        _l_(19909)

        aux = NO
        _l_(19908)
        exit(aux)

    if not prev:
        _l_(19915)

        prevp = preceding_leaf(p)
        _l_(19910)
        if not prevp or prevp.type == token.LPAR:
            _l_(19912)

            aux = NO
            _l_(19911)
            exit(aux)

    elif prev.type in {token.EQUAL} | VARARGS_SPECIALS:
        _l_(19914)

        aux = NO
        _l_(19913)
        exit(aux)

elif p.type == syms.decorator:
    _l_(19969)

    aux = NO
    _l_(19916)
    # decorators
    exit(aux)

elif p.type == syms.dotted_name:
    _l_(19968)

    if prev:
        _l_(19918)

        aux = NO
        _l_(19917)
        exit(aux)

    prevp = preceding_leaf(p)
    _l_(19919)
    if not prevp or prevp.type == token.AT or prevp.type == token.DOT:
        _l_(19921)

        aux = NO
        _l_(19920)
        exit(aux)

elif p.type == syms.classdef:
    _l_(19967)

    if t == token.LPAR:
        _l_(19923)

        aux = NO
        _l_(19922)
        exit(aux)

    if prev and prev.type == token.LPAR:
        _l_(19925)

        aux = NO
        _l_(19924)
        exit(aux)

elif p.type in {syms.subscript, syms.sliceop}:
    _l_(19966)

    # indexing
    if not prev:
        _l_(19932)

        assert p.parent is not None, "subscripts are always parented"
        _l_(19926)
        if p.parent.type == syms.subscriptlist:
            _l_(19928)

            aux = SPACE
            _l_(19927)
            exit(aux)
        aux = NO
        _l_(19929)

        exit(aux)

    elif not complex_subscript:
        _l_(19931)

        aux = NO
        _l_(19930)
        exit(aux)

elif p.type == syms.atom:
    _l_(19965)

    if prev and t == token.DOT:
        _l_(19934)

        aux = NO
        _l_(19933)
        # dots, but not the first one.
        exit(aux)

elif p.type == syms.dictsetmaker:
    _l_(19964)

    # dict unpacking
    if prev and prev.type == token.DOUBLESTAR:
        _l_(19936)

        aux = NO
        _l_(19935)
        exit(aux)

elif p.type in {syms.factor, syms.star_expr}:
    _l_(19963)

    # unary ops
    if not prev:
        _l_(19948)

        prevp = preceding_leaf(p)
        _l_(19937)
        if not prevp or prevp.type in OPENING_BRACKETS:
            _l_(19939)

            aux = NO
            _l_(19938)
            exit(aux)

        prevp_parent = prevp.parent
        _l_(19940)
        assert prevp_parent is not None
        _l_(19941)
        if prevp.type == token.COLON and prevp_parent.type in {
            syms.subscript,
            syms.sliceop,
        }:
            _l_(19945)

            aux = NO
            _l_(19942)
            exit(aux)

        elif prevp.type == token.EQUAL and prevp_parent.type == syms.argument:
            _l_(19944)

            aux = NO
            _l_(19943)
            exit(aux)

    elif t in {token.NAME, token.NUMBER, token.STRING}:
        _l_(19947)

        aux = NO
        _l_(19946)
        exit(aux)

elif p.type == syms.import_from:
    _l_(19962)

    if t == token.DOT:
        _l_(19956)

        if prev and prev.type == token.DOT:
            _l_(19950)

            aux = NO
            _l_(19949)
            exit(aux)

    elif t == token.NAME:
        _l_(19955)

        if v == "import":
            _l_(19952)

            aux = SPACE
            _l_(19951)
            exit(aux)

        if prev and prev.type == token.DOT:
            _l_(19954)

            aux = NO
            _l_(19953)
            exit(aux)

elif p.type == syms.sliceop:
    _l_(19961)

    aux = NO
    _l_(19957)
    exit(aux)

elif p.type == syms.except_clause:
    _l_(19960)

    if t == token.STAR:
        _l_(19959)

        aux = NO
        _l_(19958)
        exit(aux)
aux = SPACE
_l_(19976)

exit(aux)
