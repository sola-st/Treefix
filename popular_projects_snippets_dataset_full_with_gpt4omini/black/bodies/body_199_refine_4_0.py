from typing import Set, Dict, Any # pragma: no cover
import token # pragma: no cover
import grammar as syms # pragma: no cover

Feature = type('Feature', (), { 'F_STRINGS': 'f_strings', 'DEBUG_F_STRINGS': 'debug_f_strings', 'NUMERIC_UNDERSCORES': 'numeric_underscores', 'POS_ONLY_ARGUMENTS': 'pos_only_arguments', 'ASSIGNMENT_EXPRESSIONS': 'assignment_expressions', 'RELAXED_DECORATORS': 'relaxed_decorators', 'TRAILING_COMMA_IN_DEF': 'trailing_comma_in_def', 'TRAILING_COMMA_IN_CALL': 'trailing_comma_in_call', 'UNPACKING_ON_FLOW': 'unpacking_on_flow', 'ANN_ASSIGN_EXTENDED_RHS': 'ann_assign_extended_rhs', 'PARENTHESIZED_CONTEXT_MANAGERS': 'parenthesized_context_managers', 'PATTERN_MATCHING': 'pattern_matching', 'EXCEPT_STAR': 'except_star', 'VARIADIC_GENERICS': 'variadic_generics' }) # pragma: no cover
node = type('MockNode', (), { 'pre_order': lambda self: [] })() # pragma: no cover
is_string_token = lambda n: isinstance(n, str) # pragma: no cover
iter_fexpr_spans = lambda value: [(0, len(value))] # pragma: no cover
is_number_token = lambda n: isinstance(n, (int, float)) # pragma: no cover
STARS = {token.STAR} # pragma: no cover
FUTURE_FLAG_TO_FEATURE = {} # pragma: no cover

from typing import Set, Dict, Any # pragma: no cover
import token # pragma: no cover
import sys # pragma: no cover

class Feature:# pragma: no cover
    F_STRINGS = 'f_strings'# pragma: no cover
    DEBUG_F_STRINGS = 'debug_f_strings'# pragma: no cover
    NUMERIC_UNDERSCORES = 'numeric_underscores'# pragma: no cover
    POS_ONLY_ARGUMENTS = 'pos_only_arguments'# pragma: no cover
    ASSIGNMENT_EXPRESSIONS = 'assignment_expressions'# pragma: no cover
    RELAXED_DECORATORS = 'relaxed_decorators'# pragma: no cover
    TRAILING_COMMA_IN_DEF = 'trailing_comma_in_def'# pragma: no cover
    TRAILING_COMMA_IN_CALL = 'trailing_comma_in_call'# pragma: no cover
    UNPACKING_ON_FLOW = 'unpacking_on_flow'# pragma: no cover
    ANN_ASSIGN_EXTENDED_RHS = 'ann_assign_extended_rhs'# pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = 'parenthesized_context_managers'# pragma: no cover
    PATTERN_MATCHING = 'pattern_matching'# pragma: no cover
    EXCEPT_STAR = 'except_star'# pragma: no cover
    VARIADIC_GENERICS = 'variadic_generics' # pragma: no cover
class MockNode:# pragma: no cover
    def pre_order(self):# pragma: no cover
        return [token.SLASH, 'f''example {x=}', '10_000']# pragma: no cover
# pragma: no cover
node = MockNode() # pragma: no cover
is_string_token = lambda n: isinstance(n, str) # pragma: no cover
iter_fexpr_spans = lambda value: [(0, len(value))] # pragma: no cover
is_number_token = lambda n: isinstance(n, (int, float, str)) and ('_' in n if isinstance(n, str) else False) # pragma: no cover
STARS = [token.STAR] # pragma: no cover
FUTURE_FLAG_TO_FEATURE = {'annotations': Feature.NUMERIC_UNDERSCORES} # pragma: no cover

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
_l_(7574)
if future_imports:
    _l_(7576)

    features |= {
        FUTURE_FLAG_TO_FEATURE[future_import]
        for future_import in future_imports
        if future_import in FUTURE_FLAG_TO_FEATURE
    }
    _l_(7575)

for n in node.pre_order():
    _l_(7624)

    if is_string_token(n):
        _l_(7623)

        value_head = n.value[:2]
        _l_(7577)
        if value_head in {'f"', 'F"', "f'", "F'", "rf", "fr", "RF", "FR"}:
            _l_(7584)

            features.add(Feature.F_STRINGS)
            _l_(7578)
            if Feature.DEBUG_F_STRINGS not in features:
                _l_(7583)

                for span_beg, span_end in iter_fexpr_spans(n.value):
                    _l_(7582)

                    if n.value[span_beg : span_end - 1].rstrip().endswith("="):
                        _l_(7581)

                        features.add(Feature.DEBUG_F_STRINGS)
                        _l_(7579)
                        break
                        _l_(7580)

    elif is_number_token(n):
        _l_(7622)

        if "_" in n.value:
            _l_(7586)

            features.add(Feature.NUMERIC_UNDERSCORES)
            _l_(7585)

    elif n.type == token.SLASH:
        _l_(7621)

        if n.parent and n.parent.type in {
            syms.typedargslist,
            syms.arglist,
            syms.varargslist,
        }:
            _l_(7588)

            features.add(Feature.POS_ONLY_ARGUMENTS)
            _l_(7587)

    elif n.type == token.COLONEQUAL:
        _l_(7620)

        features.add(Feature.ASSIGNMENT_EXPRESSIONS)
        _l_(7589)

    elif n.type == syms.decorator:
        _l_(7619)

        if len(n.children) > 1 and not is_simple_decorator_expression(
            n.children[1]
        ):
            _l_(7591)

            features.add(Feature.RELAXED_DECORATORS)
            _l_(7590)

    elif (
        n.type in {syms.typedargslist, syms.arglist}
        and n.children
        and n.children[-1].type == token.COMMA
    ):
        _l_(7618)

        if n.type == syms.typedargslist:
            _l_(7594)

            feature = Feature.TRAILING_COMMA_IN_DEF
            _l_(7592)
        else:
            feature = Feature.TRAILING_COMMA_IN_CALL
            _l_(7593)

        for ch in n.children:
            _l_(7601)

            if ch.type in STARS:
                _l_(7596)

                features.add(feature)
                _l_(7595)

            if ch.type == syms.argument:
                _l_(7600)

                for argch in ch.children:
                    _l_(7599)

                    if argch.type in STARS:
                        _l_(7598)

                        features.add(feature)
                        _l_(7597)

    elif (
        n.type in {syms.return_stmt, syms.yield_expr}
        and len(n.children) >= 2
        and n.children[1].type == syms.testlist_star_expr
        and any(child.type == syms.star_expr for child in n.children[1].children)
    ):
        _l_(7617)

        features.add(Feature.UNPACKING_ON_FLOW)
        _l_(7602)

    elif (
        n.type == syms.annassign
        and len(n.children) >= 4
        and n.children[3].type == syms.testlist_star_expr
    ):
        _l_(7616)

        features.add(Feature.ANN_ASSIGN_EXTENDED_RHS)
        _l_(7603)

    elif (
        n.type == syms.with_stmt
        and len(n.children) > 2
        and n.children[1].type == syms.atom
    ):
        _l_(7615)

        atom_children = n.children[1].children
        _l_(7604)
        if (
            len(atom_children) == 3
            and atom_children[0].type == token.LPAR
            and atom_children[1].type == syms.testlist_gexp
            and atom_children[2].type == token.RPAR
        ):
            _l_(7606)

            features.add(Feature.PARENTHESIZED_CONTEXT_MANAGERS)
            _l_(7605)

    elif n.type == syms.match_stmt:
        _l_(7614)

        features.add(Feature.PATTERN_MATCHING)
        _l_(7607)

    elif (
        n.type == syms.except_clause
        and len(n.children) >= 2
        and n.children[1].type == token.STAR
    ):
        _l_(7613)

        features.add(Feature.EXCEPT_STAR)
        _l_(7608)

    elif n.type in {syms.subscriptlist, syms.trailer} and any(
        child.type == syms.star_expr for child in n.children
    ):
        _l_(7612)

        features.add(Feature.VARIADIC_GENERICS)
        _l_(7609)

    elif (
        n.type == syms.tname_star
        and len(n.children) == 3
        and n.children[2].type == syms.star_expr
    ):
        _l_(7611)

        features.add(Feature.VARIADIC_GENERICS)
        _l_(7610)
aux = features
_l_(7625)

exit(aux)
