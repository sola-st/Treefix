import token # pragma: no cover
from typing import List # pragma: no cover

Feature = type('Feature', (object,), {'FORCE_OPTIONAL_PARENTHESES': 'FORCE_OPTIONAL_PARENTHESES'}) # pragma: no cover
features = set() # pragma: no cover
rhs = type('Mock', (object,), {'opening_bracket': type('Mock', (object,), {'type': token.LPAR, 'value': False})(), 'closing_bracket': type('Mock', (object,), {'type': token.RPAR, 'value': False})(), 'body': type('Mock', (object,), {'contains_standalone_comments': lambda x: False})(), 'head': type('Mock', (object,), {'leaves': [], 'magic_trailing_comma': None})(), 'tail': type('Mock', (object,), {'contains_multiline_strings': lambda: False})()})() # pragma: no cover
def can_omit_invisible_parens(body, line_length): return True # pragma: no cover
line_length = 80 # pragma: no cover
omit = set() # pragma: no cover
def _first_right_hand_split(line, omit=set()): return type('Mock', (object,), {})() # pragma: no cover
Preview = type('Preview', (object,), {'prefer_splitting_right_hand_side_of_assignments': 'prefer_splitting_right_hand_side_of_assignments'}) # pragma: no cover
def is_line_short_enough(head, line_length=80): return True # pragma: no cover
def _prefer_split_rhs_oop(rhs_oop, line_length=80): return False # pragma: no cover
def _maybe_split_omitting_optional_parens(rhs_oop, line, line_length, features=set(), omit=set()): return None # pragma: no cover
CannotSplit = type('CannotSplit', (Exception,), {}) # pragma: no cover
def can_be_split(body): return True # pragma: no cover
def ensure_visible(bracket): return None # pragma: no cover
BRACKETS = set([token.LPAR, token.RPAR]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
if (
    Feature.FORCE_OPTIONAL_PARENTHESES not in features
    # the opening bracket is an optional paren
    and rhs.opening_bracket.type == token.LPAR
    and not rhs.opening_bracket.value
    # the closing bracket is an optional paren
    and rhs.closing_bracket.type == token.RPAR
    and not rhs.closing_bracket.value
    # it's not an import (optional parens are the only thing we can split on
    # in this case; attempting a split without them is a waste of time)
    and not line.is_import
    # there are no standalone comments in the body
    and not rhs.body.contains_standalone_comments(0)
    # and we can actually remove the parens
    and can_omit_invisible_parens(rhs.body, line_length)
):
    _l_(18483)

    omit = {id(rhs.closing_bracket), *omit}
    _l_(18472)
    try:
        _l_(18482)

        # The _RHSResult Omitting Optional Parens.
        rhs_oop = _first_right_hand_split(line, omit=omit)
        _l_(18473)
        if not (
            Preview.prefer_splitting_right_hand_side_of_assignments in line.mode
            # the split is right after `=`
            and len(rhs.head.leaves) >= 2
            and rhs.head.leaves[-2].type == token.EQUAL
            # the left side of assignement contains brackets
            and any(leaf.type in BRACKETS for leaf in rhs.head.leaves[:-1])
            # the left side of assignment is short enough (the -1 is for the ending
            # optional paren)
            and is_line_short_enough(rhs.head, line_length=line_length - 1)
            # the left side of assignment won't explode further because of magic
            # trailing comma
            and rhs.head.magic_trailing_comma is None
            # the split by omitting optional parens isn't preferred by some other
            # reason
            and not _prefer_split_rhs_oop(rhs_oop, line_length=line_length)
        ):
            _l_(18476)

            aux = _maybe_split_omitting_optional_parens(
                rhs_oop, line, line_length, features=features, omit=omit
            )
            _l_(18474)
            exit(aux)
            exit()
            _l_(18475)

    except CannotSplit as e:
        _l_(18481)

        if not (
            can_be_split(rhs.body)
            or is_line_short_enough(rhs.body, line_length=line_length)
        ):
            _l_(18480)

            raise CannotSplit(
                "Splitting failed, body is still too long and can't be split."
            ) from e
            _l_(18477)

        elif (
            rhs.head.contains_multiline_strings()
            or rhs.tail.contains_multiline_strings()
        ):
            _l_(18479)

            raise CannotSplit(
                "The current optional pair of parentheses is bound to fail to"
                " satisfy the splitting algorithm because the head or the tail"
                " contains multiline strings which by definition never fit one"
                " line."
            ) from e
            _l_(18478)

ensure_visible(rhs.opening_bracket)
_l_(18484)
ensure_visible(rhs.closing_bracket)
_l_(18485)
for result in (rhs.head, rhs.body, rhs.tail):
    _l_(18488)

    if result:
        _l_(18487)

        aux = result
        _l_(18486)
        exit(aux)
