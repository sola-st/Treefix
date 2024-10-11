import token # pragma: no cover
from typing import Set, Any, Optional # pragma: no cover
class CannotSplit(Exception): pass # pragma: no cover
class Feature: FORCE_OPTIONAL_PARENTHESES = 'force_optional_parentheses' # pragma: no cover

features = {Feature.FORCE_OPTIONAL_PARENTHESES} # pragma: no cover
line_length = 80 # pragma: no cover
omit = set() # pragma: no cover
def can_omit_invisible_parens(body, line_length): return True # pragma: no cover
def is_line_short_enough(head, line_length): return True # pragma: no cover
def _first_right_hand_split(line, omit): return [] # pragma: no cover
def _prefer_split_rhs_oop(rhs_oop, line_length): return False # pragma: no cover
def _maybe_split_omitting_optional_parens(rhs_oop, line, line_length, features, omit): return None # pragma: no cover
def ensure_visible(bracket): pass # pragma: no cover
def can_be_split(body): return True # pragma: no cover

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
    _l_(6996)

    omit = {id(rhs.closing_bracket), *omit}
    _l_(6985)
    try:
        _l_(6995)

        # The _RHSResult Omitting Optional Parens.
        rhs_oop = _first_right_hand_split(line, omit=omit)
        _l_(6986)
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
            _l_(6989)

            aux = _maybe_split_omitting_optional_parens(
                rhs_oop, line, line_length, features=features, omit=omit
            )
            _l_(6987)
            exit(aux)
            exit()
            _l_(6988)

    except CannotSplit as e:
        _l_(6994)

        if not (
            can_be_split(rhs.body)
            or is_line_short_enough(rhs.body, line_length=line_length)
        ):
            _l_(6993)

            raise CannotSplit(
                "Splitting failed, body is still too long and can't be split."
            ) from e
            _l_(6990)

        elif (
            rhs.head.contains_multiline_strings()
            or rhs.tail.contains_multiline_strings()
        ):
            _l_(6992)

            raise CannotSplit(
                "The current optional pair of parentheses is bound to fail to"
                " satisfy the splitting algorithm because the head or the tail"
                " contains multiline strings which by definition never fit one"
                " line."
            ) from e
            _l_(6991)

ensure_visible(rhs.opening_bracket)
_l_(6997)
ensure_visible(rhs.closing_bracket)
_l_(6998)
for result in (rhs.head, rhs.body, rhs.tail):
    _l_(7001)

    if result:
        _l_(7000)

        aux = result
        _l_(6999)
        exit(aux)
