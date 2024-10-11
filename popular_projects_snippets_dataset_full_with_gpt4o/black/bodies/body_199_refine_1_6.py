from typing import Set # pragma: no cover
from collections import namedtuple # pragma: no cover
import token # pragma: no cover
import symtable as syms # pragma: no cover

Feature = namedtuple('Feature', ['F_STRINGS', 'DEBUG_F_STRINGS', 'NUMERIC_UNDERSCORES', 'POS_ONLY_ARGUMENTS', 'ASSIGNMENT_EXPRESSIONS', 'RELAXED_DECORATORS', 'TRAILING_COMMA_IN_DEF', 'TRAILING_COMMA_IN_CALL', 'UNPACKING_ON_FLOW', 'ANN_ASSIGN_EXTENDED_RHS', 'PARENTHESIZED_CONTEXT_MANAGERS', 'PATTERN_MATCHING', 'EXCEPT_STAR', 'VARIADIC_GENERICS'])(*range(14)) # pragma: no cover
node = type('MockNode', (object,), {'pre_order': lambda self: [], 'type': None, 'value': '', 'children': [], 'parent': None})() # pragma: no cover
is_string_token = lambda n: isinstance(n.value, str) # pragma: no cover
iter_fexpr_spans = lambda s: [(0, len(s))] # pragma: no cover
is_number_token = lambda n: n.value.isdigit() # pragma: no cover
is_simple_decorator_expression = lambda n: False # pragma: no cover
STARS = {token.STAR} # pragma: no cover
FUTURE_FLAG_TO_FEATURE = {'annotations': Feature.PATTERN_MATCHING} # pragma: no cover

from typing import Set # pragma: no cover
import token # pragma: no cover
import symtable as syms # pragma: no cover

class Feature:# pragma: no cover
    F_STRINGS = 'F_STRINGS'# pragma: no cover
    DEBUG_F_STRINGS = 'DEBUG_F_STRINGS'# pragma: no cover
    NUMERIC_UNDERSCORES = 'NUMERIC_UNDERSCORES'# pragma: no cover
    POS_ONLY_ARGUMENTS = 'POS_ONLY_ARGUMENTS'# pragma: no cover
    ASSIGNMENT_EXPRESSIONS = 'ASSIGNMENT_EXPRESSIONS'# pragma: no cover
    RELAXED_DECORATORS = 'RELAXED_DECORATORS'# pragma: no cover
    TRAILING_COMMA_IN_DEF = 'TRAILING_COMMA_IN_DEF'# pragma: no cover
    TRAILING_COMMA_IN_CALL = 'TRAILING_COMMA_IN_CALL'# pragma: no cover
    UNPACKING_ON_FLOW = 'UNPACKING_ON_FLOW'# pragma: no cover
    ANN_ASSIGN_EXTENDED_RHS = 'ANN_ASSIGN_EXTENDED_RHS'# pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = 'PARENTHESIZED_CONTEXT_MANAGERS'# pragma: no cover
    PATTERN_MATCHING = 'PATTERN_MATCHING'# pragma: no cover
    EXCEPT_STAR = 'EXCEPT_STAR'# pragma: no cover
    VARIADIC_GENERICS = 'VARIADIC_GENERICS' # pragma: no cover
node = type('MockNode', (object,), {'pre_order': lambda self: [], 'type': None, 'value': '', 'children': [], 'parent': None})() # pragma: no cover
is_string_token = lambda n: isinstance(n.value, str) # pragma: no cover
iter_fexpr_spans = lambda s: [(0, len(s))] # pragma: no cover
is_number_token = lambda n: n.value.isdigit() # pragma: no cover
is_simple_decorator_expression = lambda n: False # pragma: no cover
STARS = {token.STAR} # pragma: no cover
FUTURE_FLAG_TO_FEATURE = {'annotations': Feature.PARENTHESIZED_CONTEXT_MANAGERS} # pragma: no cover

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
