from typing import Final # pragma: no cover
import token # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, type, parent, value, prev_sibling=None):# pragma: no cover
        self.type = type# pragma: no cover
        self.parent = parent# pragma: no cover
        self.value = value# pragma: no cover
        self.prev_sibling = prev_sibling# pragma: no cover
 # pragma: no cover
class MockParent:# pragma: no cover
    def __init__(self, type):# pragma: no cover
        self.type = type# pragma: no cover
ALWAYS_NO_SPACE = {token.NAME}# pragma: no cover
 # pragma: no cover
OPENING_BRACKETS = {token.LPAR}# pragma: no cover
 # pragma: no cover
VARARGS_SPECIALS = {token.STAR}# pragma: no cover
 # pragma: no cover
TYPED_NAMES = {token.NAME}# pragma: no cover
 # pragma: no cover
complex_subscript = False# pragma: no cover
 # pragma: no cover
def preceding_leaf(p): return MockLeaf(type=token.COMMA, parent=None, value='prev_value')# pragma: no cover
 # pragma: no cover
def parent_type(leaf): return syms.arglist# pragma: no cover
 # pragma: no cover
syms = type('syms', (), {})()# pragma: no cover
 # pragma: no cover
syms.parameters = 1# pragma: no cover
 # pragma: no cover
syms.arglist = 2# pragma: no cover
 # pragma: no cover
syms.typedargslist = 3# pragma: no cover
 # pragma: no cover
syms.subscript = 4# pragma: no cover
 # pragma: no cover
syms.sliceop = 5# pragma: no cover
 # pragma: no cover
syms.factor = 6# pragma: no cover
 # pragma: no cover
syms.star_expr = 7# pragma: no cover
 # pragma: no cover
syms.argument = 8# pragma: no cover
 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return whitespace prefix if needed for the given `leaf`.

    `complex_subscript` signals whether the given leaf is part of a subscription
    which has non-trivial arguments, like arithmetic expressions or function calls.
    """
NO: Final = ""
_l_(8374)
SPACE: Final = " "
_l_(8375)
DOUBLESPACE: Final = "  "
_l_(8376)
t = leaf.type
_l_(8377)
p = leaf.parent
_l_(8378)
v = leaf.value
_l_(8379)
if t in ALWAYS_NO_SPACE:
    _l_(8381)

    aux = NO
    _l_(8380)
    exit(aux)

if t == token.COMMENT:
    _l_(8383)

    aux = DOUBLESPACE
    _l_(8382)
    exit(aux)

assert p is not None, f"INTERNAL ERROR: hand-made leaf without parent: {leaf!r}"
_l_(8384)
if t == token.COLON and p.type not in {
    syms.subscript,
    syms.subscriptlist,
    syms.sliceop,
}:
    _l_(8386)

    aux = NO
    _l_(8385)
    exit(aux)

prev = leaf.prev_sibling
_l_(8387)
if not prev:
    _l_(8417)

    prevp = preceding_leaf(p)
    _l_(8388)
    if not prevp or prevp.type in OPENING_BRACKETS:
        _l_(8390)

        aux = NO
        _l_(8389)
        exit(aux)

    if t == token.COLON:
        _l_(8396)

        if prevp.type == token.COLON:
            _l_(8394)

            aux = NO
            _l_(8391)
            exit(aux)

        elif prevp.type != token.COMMA and not complex_subscript:
            _l_(8393)

            aux = NO
            _l_(8392)
            exit(aux)
        aux = SPACE
        _l_(8395)

        exit(aux)

    if prevp.type == token.EQUAL:
        _l_(8414)

        if prevp.parent:
            _l_(8401)

            if prevp.parent.type in {
                syms.arglist,
                syms.argument,
                syms.parameters,
                syms.varargslist,
            }:
                _l_(8400)

                aux = NO
                _l_(8397)
                exit(aux)

            elif prevp.parent.type == syms.typedargslist:
                _l_(8399)

                aux = prevp.prefix
                _l_(8398)
                # A bit hacky: if the equal sign has whitespace, it means we
                # previously found it's a typed argument.  So, we're using
                # that, too.
                exit(aux)

    elif (
        prevp.type == token.STAR
        and parent_type(prevp) == syms.star_expr
        and parent_type(prevp.parent) == syms.subscriptlist
    ):
        _l_(8413)

        aux = NO
        _l_(8402)
        # No space between typevar tuples.
        exit(aux)

    elif prevp.type in VARARGS_SPECIALS:
        _l_(8412)

        if is_vararg(prevp, within=VARARGS_PARENTS | UNPACKING_PARENTS):
            _l_(8404)

            aux = NO
            _l_(8403)
            exit(aux)

    elif prevp.type == token.COLON:
        _l_(8411)

        if prevp.parent and prevp.parent.type in {syms.subscript, syms.sliceop}:
            _l_(8406)

            aux = SPACE if complex_subscript else NO
            _l_(8405)
            exit(aux)

    elif (
        prevp.parent
        and prevp.parent.type == syms.factor
        and prevp.type in MATH_OPERATORS
    ):
        _l_(8410)

        aux = NO
        _l_(8407)
        exit(aux)

    elif prevp.type == token.AT and p.parent and p.parent.type == syms.decorator:
        _l_(8409)

        aux = NO
        _l_(8408)
        # no space in decorators
        exit(aux)

elif prev.type in OPENING_BRACKETS:
    _l_(8416)

    aux = NO
    _l_(8415)
    exit(aux)

if p.type in {syms.parameters, syms.arglist}:
    _l_(8509)

    # untyped function signatures or calls
    if not prev or prev.type != token.COMMA:
        _l_(8419)

        aux = NO
        _l_(8418)
        exit(aux)

elif p.type == syms.varargslist:
    _l_(8508)

    # lambdas
    if prev and prev.type != token.COMMA:
        _l_(8421)

        aux = NO
        _l_(8420)
        exit(aux)

elif p.type == syms.typedargslist:
    _l_(8507)

    # typed function signatures
    if not prev:
        _l_(8423)

        aux = NO
        _l_(8422)
        exit(aux)

    if t == token.EQUAL:
        _l_(8430)

        if prev.type not in TYPED_NAMES:
            _l_(8425)

            aux = NO
            _l_(8424)
            exit(aux)

    elif prev.type == token.EQUAL:
        _l_(8429)

        aux = prev.prefix
        _l_(8426)
        # A bit hacky: if the equal sign has whitespace, it means we
        # previously found it's a typed argument.  So, we're using that, too.
        exit(aux)

    elif prev.type != token.COMMA:
        _l_(8428)

        aux = NO
        _l_(8427)
        exit(aux)

elif p.type in TYPED_NAMES:
    _l_(8506)

    # type names
    if not prev:
        _l_(8434)

        prevp = preceding_leaf(p)
        _l_(8431)
        if not prevp or prevp.type != token.COMMA:
            _l_(8433)

            aux = NO
            _l_(8432)
            exit(aux)

elif p.type == syms.trailer:
    _l_(8505)

    # attributes and calls
    if t == token.LPAR or t == token.RPAR:
        _l_(8436)

        aux = NO
        _l_(8435)
        exit(aux)

    if not prev:
        _l_(8441)

        if t == token.DOT or t == token.LSQB:
            _l_(8438)

            aux = NO
            _l_(8437)
            exit(aux)

    elif prev.type != token.COMMA:
        _l_(8440)

        aux = NO
        _l_(8439)
        exit(aux)

elif p.type == syms.argument:
    _l_(8504)

    # single argument
    if t == token.EQUAL:
        _l_(8443)

        aux = NO
        _l_(8442)
        exit(aux)

    if not prev:
        _l_(8449)

        prevp = preceding_leaf(p)
        _l_(8444)
        if not prevp or prevp.type == token.LPAR:
            _l_(8446)

            aux = NO
            _l_(8445)
            exit(aux)

    elif prev.type in {token.EQUAL} | VARARGS_SPECIALS:
        _l_(8448)

        aux = NO
        _l_(8447)
        exit(aux)

elif p.type == syms.decorator:
    _l_(8503)

    aux = NO
    _l_(8450)
    # decorators
    exit(aux)

elif p.type == syms.dotted_name:
    _l_(8502)

    if prev:
        _l_(8452)

        aux = NO
        _l_(8451)
        exit(aux)

    prevp = preceding_leaf(p)
    _l_(8453)
    if not prevp or prevp.type == token.AT or prevp.type == token.DOT:
        _l_(8455)

        aux = NO
        _l_(8454)
        exit(aux)

elif p.type == syms.classdef:
    _l_(8501)

    if t == token.LPAR:
        _l_(8457)

        aux = NO
        _l_(8456)
        exit(aux)

    if prev and prev.type == token.LPAR:
        _l_(8459)

        aux = NO
        _l_(8458)
        exit(aux)

elif p.type in {syms.subscript, syms.sliceop}:
    _l_(8500)

    # indexing
    if not prev:
        _l_(8466)

        assert p.parent is not None, "subscripts are always parented"
        _l_(8460)
        if p.parent.type == syms.subscriptlist:
            _l_(8462)

            aux = SPACE
            _l_(8461)
            exit(aux)
        aux = NO
        _l_(8463)

        exit(aux)

    elif not complex_subscript:
        _l_(8465)

        aux = NO
        _l_(8464)
        exit(aux)

elif p.type == syms.atom:
    _l_(8499)

    if prev and t == token.DOT:
        _l_(8468)

        aux = NO
        _l_(8467)
        # dots, but not the first one.
        exit(aux)

elif p.type == syms.dictsetmaker:
    _l_(8498)

    # dict unpacking
    if prev and prev.type == token.DOUBLESTAR:
        _l_(8470)

        aux = NO
        _l_(8469)
        exit(aux)

elif p.type in {syms.factor, syms.star_expr}:
    _l_(8497)

    # unary ops
    if not prev:
        _l_(8482)

        prevp = preceding_leaf(p)
        _l_(8471)
        if not prevp or prevp.type in OPENING_BRACKETS:
            _l_(8473)

            aux = NO
            _l_(8472)
            exit(aux)

        prevp_parent = prevp.parent
        _l_(8474)
        assert prevp_parent is not None
        _l_(8475)
        if prevp.type == token.COLON and prevp_parent.type in {
            syms.subscript,
            syms.sliceop,
        }:
            _l_(8479)

            aux = NO
            _l_(8476)
            exit(aux)

        elif prevp.type == token.EQUAL and prevp_parent.type == syms.argument:
            _l_(8478)

            aux = NO
            _l_(8477)
            exit(aux)

    elif t in {token.NAME, token.NUMBER, token.STRING}:
        _l_(8481)

        aux = NO
        _l_(8480)
        exit(aux)

elif p.type == syms.import_from:
    _l_(8496)

    if t == token.DOT:
        _l_(8490)

        if prev and prev.type == token.DOT:
            _l_(8484)

            aux = NO
            _l_(8483)
            exit(aux)

    elif t == token.NAME:
        _l_(8489)

        if v == "import":
            _l_(8486)

            aux = SPACE
            _l_(8485)
            exit(aux)

        if prev and prev.type == token.DOT:
            _l_(8488)

            aux = NO
            _l_(8487)
            exit(aux)

elif p.type == syms.sliceop:
    _l_(8495)

    aux = NO
    _l_(8491)
    exit(aux)

elif p.type == syms.except_clause:
    _l_(8494)

    if t == token.STAR:
        _l_(8493)

        aux = NO
        _l_(8492)
        exit(aux)
aux = SPACE
_l_(8510)

exit(aux)
