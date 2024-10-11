from typing import Set # pragma: no cover
import token # pragma: no cover
from enum import Enum, auto # pragma: no cover

class Feature(Enum): # pragma: no cover
    F_STRINGS = auto() # pragma: no cover
    DEBUG_F_STRINGS = auto() # pragma: no cover
    NUMERIC_UNDERSCORES = auto() # pragma: no cover
    POS_ONLY_ARGUMENTS = auto() # pragma: no cover
    ASSIGNMENT_EXPRESSIONS = auto() # pragma: no cover
    RELAXED_DECORATORS = auto() # pragma: no cover
    TRAILING_COMMA_IN_DEF = auto() # pragma: no cover
    TRAILING_COMMA_IN_CALL = auto() # pragma: no cover
    UNPACKING_ON_FLOW = auto() # pragma: no cover
    ANN_ASSIGN_EXTENDED_RHS = auto() # pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = auto() # pragma: no cover
    PATTERN_MATCHING = auto() # pragma: no cover
    EXCEPT_STAR = auto() # pragma: no cover
    VARIADIC_GENERICS = auto() # pragma: no cover
FUTURE_FLAG_TO_FEATURE = { # pragma: no cover
    'annotations': Feature.RELAXED_DECORATORS # pragma: no cover
} # pragma: no cover
def is_string_token(n): # pragma: no cover
    return n.type == token.STRING # pragma: no cover
def is_number_token(n): # pragma: no cover
    return n.type == token.NUMBER # pragma: no cover
def iter_fexpr_spans(value): # pragma: no cover
    yield (0, len(value)) # pragma: no cover
def is_simple_decorator_expression(n): # pragma: no cover
    return False # pragma: no cover
syms = type('syms', (object,), { # pragma: no cover
    'typedargslist': 1, # pragma: no cover
    'arglist': 2, # pragma: no cover
    'varargslist': 3, # pragma: no cover
    'decorator': 4, # pragma: no cover
    'return_stmt': 5, # pragma: no cover
    'yield_expr': 6, # pragma: no cover
    'testlist_star_expr': 7, # pragma: no cover
    'star_expr': 8, # pragma: no cover
    'annassign': 9, # pragma: no cover
    'with_stmt': 10, # pragma: no cover
    'atom': 11, # pragma: no cover
    'testlist_gexp': 12, # pragma: no cover
    'match_stmt': 13, # pragma: no cover
    'except_clause': 14, # pragma: no cover
    'subscriptlist': 15, # pragma: no cover
    'trailer': 16, # pragma: no cover
    'tname_star': 17, # pragma: no cover
    'argument': 18 # pragma: no cover
}) # pragma: no cover
STARS = {token.STAR, token.DOUBLESTAR} # pragma: no cover
class MockNode: # pragma: no cover
    def __init__(self, typ=None, value='', children=None, parent=None): # pragma: no cover
        self.type = typ # pragma: no cover
        self.value = value # pragma: no cover
        self.children = children if children else [] # pragma: no cover
        self.parent = parent # pragma: no cover
    def pre_order(self): # pragma: no cover
        return [self] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Return a set of (relatively) new Python features used in this file.

    Currently looking for:
    - f-strings;
    - self-documenting expressions in f-strings (f"{x=}");
    - underscores in numeric literals;
    - trailing commas after * or ** in function signatures and calls;
    - positional only arguments in function signatures and lambdas;
    - assignment expression;
    - relaxed decorator syntax;
    - usage of __future__ flags (annotations);
    - print / exec statements;
    - parenthesized context managers;
    - match statements;
    - except* clause;
    - variadic generics;
    """
features: Set[Feature] = set()
_l_(19065)
if future_imports:
    _l_(19067)

    features |= {
        FUTURE_FLAG_TO_FEATURE[future_import]
        for future_import in future_imports
        if future_import in FUTURE_FLAG_TO_FEATURE
    }
    _l_(19066)

for n in node.pre_order():
    _l_(19115)

    if is_string_token(n):
        _l_(19114)

        value_head = n.value[:2]
        _l_(19068)
        if value_head in {'f"', 'F"', "f'", "F'", "rf", "fr", "RF", "FR"}:
            _l_(19075)

            features.add(Feature.F_STRINGS)
            _l_(19069)
            if Feature.DEBUG_F_STRINGS not in features:
                _l_(19074)

                for span_beg, span_end in iter_fexpr_spans(n.value):
                    _l_(19073)

                    if n.value[span_beg : span_end - 1].rstrip().endswith("="):
                        _l_(19072)

                        features.add(Feature.DEBUG_F_STRINGS)
                        _l_(19070)
                        break
                        _l_(19071)

    elif is_number_token(n):
        _l_(19113)

        if "_" in n.value:
            _l_(19077)

            features.add(Feature.NUMERIC_UNDERSCORES)
            _l_(19076)

    elif n.type == token.SLASH:
        _l_(19112)

        if n.parent and n.parent.type in {
            syms.typedargslist,
            syms.arglist,
            syms.varargslist,
        }:
            _l_(19079)

            features.add(Feature.POS_ONLY_ARGUMENTS)
            _l_(19078)

    elif n.type == token.COLONEQUAL:
        _l_(19111)

        features.add(Feature.ASSIGNMENT_EXPRESSIONS)
        _l_(19080)

    elif n.type == syms.decorator:
        _l_(19110)

        if len(n.children) > 1 and not is_simple_decorator_expression(
            n.children[1]
        ):
            _l_(19082)

            features.add(Feature.RELAXED_DECORATORS)
            _l_(19081)

    elif (
        n.type in {syms.typedargslist, syms.arglist}
        and n.children
        and n.children[-1].type == token.COMMA
    ):
        _l_(19109)

        if n.type == syms.typedargslist:
            _l_(19085)

            feature = Feature.TRAILING_COMMA_IN_DEF
            _l_(19083)
        else:
            feature = Feature.TRAILING_COMMA_IN_CALL
            _l_(19084)

        for ch in n.children:
            _l_(19092)

            if ch.type in STARS:
                _l_(19087)

                features.add(feature)
                _l_(19086)

            if ch.type == syms.argument:
                _l_(19091)

                for argch in ch.children:
                    _l_(19090)

                    if argch.type in STARS:
                        _l_(19089)

                        features.add(feature)
                        _l_(19088)

    elif (
        n.type in {syms.return_stmt, syms.yield_expr}
        and len(n.children) >= 2
        and n.children[1].type == syms.testlist_star_expr
        and any(child.type == syms.star_expr for child in n.children[1].children)
    ):
        _l_(19108)

        features.add(Feature.UNPACKING_ON_FLOW)
        _l_(19093)

    elif (
        n.type == syms.annassign
        and len(n.children) >= 4
        and n.children[3].type == syms.testlist_star_expr
    ):
        _l_(19107)

        features.add(Feature.ANN_ASSIGN_EXTENDED_RHS)
        _l_(19094)

    elif (
        n.type == syms.with_stmt
        and len(n.children) > 2
        and n.children[1].type == syms.atom
    ):
        _l_(19106)

        atom_children = n.children[1].children
        _l_(19095)
        if (
            len(atom_children) == 3
            and atom_children[0].type == token.LPAR
            and atom_children[1].type == syms.testlist_gexp
            and atom_children[2].type == token.RPAR
        ):
            _l_(19097)

            features.add(Feature.PARENTHESIZED_CONTEXT_MANAGERS)
            _l_(19096)

    elif n.type == syms.match_stmt:
        _l_(19105)

        features.add(Feature.PATTERN_MATCHING)
        _l_(19098)

    elif (
        n.type == syms.except_clause
        and len(n.children) >= 2
        and n.children[1].type == token.STAR
    ):
        _l_(19104)

        features.add(Feature.EXCEPT_STAR)
        _l_(19099)

    elif n.type in {syms.subscriptlist, syms.trailer} and any(
        child.type == syms.star_expr for child in n.children
    ):
        _l_(19103)

        features.add(Feature.VARIADIC_GENERICS)
        _l_(19100)

    elif (
        n.type == syms.tname_star
        and len(n.children) == 3
        and n.children[2].type == syms.star_expr
    ):
        _l_(19102)

        features.add(Feature.VARIADIC_GENERICS)
        _l_(19101)
aux = features
_l_(19116)

exit(aux)
