from typing import Set # pragma: no cover
import token # pragma: no cover
import symtable as syms # pragma: no cover

class Feature: # pragma: no cover
    F_STRINGS = 'f-strings' # pragma: no cover
    DEBUG_F_STRINGS = 'self-documenting expressions in f-strings' # pragma: no cover
    NUMERIC_UNDERSCORES = 'underscores in numeric literals' # pragma: no cover
    POS_ONLY_ARGUMENTS = 'positional only arguments' # pragma: no cover
    ASSIGNMENT_EXPRESSIONS = 'assignment expressions' # pragma: no cover
    RELAXED_DECORATORS = 'relaxed decorator syntax' # pragma: no cover
    TRAILING_COMMA_IN_DEF = 'trailing comma in function definitions' # pragma: no cover
    TRAILING_COMMA_IN_CALL = 'trailing comma in function calls' # pragma: no cover
    UNPACKING_ON_FLOW = 'unpacking expressions in flow control statements' # pragma: no cover
    ANN_ASSIGN_EXTENDED_RHS = 'extended rhs in annotated assignments' # pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = 'parenthesized context managers' # pragma: no cover
    PATTERN_MATCHING = 'pattern matching with match statement' # pragma: no cover
    EXCEPT_STAR = 'except* clause' # pragma: no cover
    VARIADIC_GENERICS = 'variadic generics' # pragma: no cover
 # pragma: no cover
node = type('Mock', (object,), { # pragma: no cover
    'pre_order': lambda self: [], # pragma: no cover
    'value': '', # pragma: no cover
    'type': None, # pragma: no cover
    'parent': None, # pragma: no cover
    'children': [] # pragma: no cover
})() # pragma: no cover
def is_string_token(n): # pragma: no cover
    return hasattr(n, 'value') and isinstance(n.value, str) # pragma: no cover
def iter_fexpr_spans(value): # pragma: no cover
    return [(0, len(value))] # pragma: no cover
def is_number_token(n): # pragma: no cover
    return hasattr(n, 'value') and any(ch.isdigit() for ch in n.value) # pragma: no cover
def is_simple_decorator_expression(n): # pragma: no cover
    return isinstance(n, type('Mock', (object,), {})) # pragma: no cover
STARS = {token.STAR} # pragma: no cover
FUTURE_FLAG_TO_FEATURE = { # pragma: no cover
    'annotations': Feature.RELAXED_DECORATORS, # pragma: no cover
} # pragma: no cover
def set_syms_attribute(name): # pragma: no cover
    setattr(syms, name, type('Mock', (object,), {})) # pragma: no cover
for attribute in ['typedargslist', 'arglist', 'varargslist', 'decorator', 'argument', 'return_stmt', 'yield_expr', 'testlist_star_expr', 'star_expr', 'annassign', 'with_stmt', 'atom', 'testlist_gexp', 'match_stmt', 'except_clause', 'subscriptlist', 'trailer', 'tname_star']: # pragma: no cover
    set_syms_attribute(attribute) # pragma: no cover

from typing import Set # pragma: no cover
import token # pragma: no cover
import ast # pragma: no cover

class Feature: # pragma: no cover
    F_STRINGS = 'f-strings' # pragma: no cover
    DEBUG_F_STRINGS = 'self-documenting expressions in f-strings' # pragma: no cover
    NUMERIC_UNDERSCORES = 'underscores in numeric literals' # pragma: no cover
    POS_ONLY_ARGUMENTS = 'positional only arguments' # pragma: no cover
    ASSIGNMENT_EXPRESSIONS = 'assignment expressions' # pragma: no cover
    RELAXED_DECORATORS = 'relaxed decorator syntax' # pragma: no cover
    TRAILING_COMMA_IN_DEF = 'trailing comma in function definitions' # pragma: no cover
    TRAILING_COMMA_IN_CALL = 'trailing comma in function calls' # pragma: no cover
    UNPACKING_ON_FLOW = 'unpacking expressions in flow control statements' # pragma: no cover
    ANN_ASSIGN_EXTENDED_RHS = 'extended rhs in annotated assignments' # pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = 'parenthesized context managers' # pragma: no cover
    PATTERN_MATCHING = 'pattern matching with match statement' # pragma: no cover
    EXCEPT_STAR = 'except* clause' # pragma: no cover
    VARIADIC_GENERICS = 'variadic generics' # pragma: no cover
 # pragma: no cover
node = type('Mock', (object,), { # pragma: no cover
    'pre_order': lambda self: [], # pragma: no cover
    'value': '', # pragma: no cover
    'type': None, # pragma: no cover
    'parent': None, # pragma: no cover
    'children': [] # pragma: no cover
})() # pragma: no cover
def is_string_token(n): # pragma: no cover
    return hasattr(n, 'value') and isinstance(n.value, str) # pragma: no cover
def iter_fexpr_spans(value): # pragma: no cover
    return [(0, len(value))] # pragma: no cover
def is_number_token(n): # pragma: no cover
    return hasattr(n, 'value') and any(ch.isdigit() for ch in n.value) # pragma: no cover
def is_simple_decorator_expression(n): # pragma: no cover
    return isinstance(n, type('Mock', (object,), {})) # pragma: no cover
STARS = {token.STAR} # pragma: no cover
FUTURE_FLAG_TO_FEATURE = { # pragma: no cover
    'annotations': Feature.RELAXED_DECORATORS, # pragma: no cover
} # pragma: no cover
SYMS = type('SYMS', (object,), { # pragma: no cover
    'typedargslist': 'typedargslist', # pragma: no cover
    'arglist': 'arglist', # pragma: no cover
    'varargslist': 'varargslist', # pragma: no cover
    'decorator': 'decorator', # pragma: no cover
    'argument': 'argument', # pragma: no cover
    'return_stmt': 'return_stmt', # pragma: no cover
    'yield_expr': 'yield_expr', # pragma: no cover
    'testlist_star_expr': 'testlist_star_expr', # pragma: no cover
    'star_expr': 'star_expr', # pragma: no cover
    'annassign': 'annassign', # pragma: no cover
    'with_stmt': 'with_stmt', # pragma: no cover
    'atom': 'atom', # pragma: no cover
    'testlist_gexp': 'testlist_gexp', # pragma: no cover
    'match_stmt': 'match_stmt', # pragma: no cover
    'except_clause': 'except_clause', # pragma: no cover
    'subscriptlist': 'subscriptlist', # pragma: no cover
    'trailer': 'trailer', # pragma: no cover
    'tname_star': 'tname_star' # pragma: no cover
}) # pragma: no cover

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
