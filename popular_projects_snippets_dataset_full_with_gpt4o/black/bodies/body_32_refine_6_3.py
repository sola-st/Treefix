from enum import Enum # pragma: no cover
import token # pragma: no cover
from typing import List # pragma: no cover

class Feature(Enum):# pragma: no cover
    FORCE_OPTIONAL_PARENTHESES = 1 # pragma: no cover
features = set() # pragma: no cover
rhs = type('MockRHS', (object,), {# pragma: no cover
    'opening_bracket': type('MockBracket', (object,), {'type': token.LPAR, 'value': None})(),# pragma: no cover
    'closing_bracket': type('MockBracket', (object,), {'type': token.RPAR, 'value': None})(),# pragma: no cover
    'body': type('MockBody', (object,), {'contains_standalone_comments': lambda self, x: False})(),# pragma: no cover
    'head': type('MockHead', (object,), {# pragma: no cover
        'leaves': [type('MockLeaf', (object,), {'type': token.NAME})() for _ in range(2)],# pragma: no cover
        'magic_trailing_comma': None,# pragma: no cover
        'contains_multiline_strings': lambda self: False# pragma: no cover
    })(),# pragma: no cover
    'tail': type('MockTail', (object,), {'contains_multiline_strings': lambda self: False})()# pragma: no cover
}) # pragma: no cover
can_omit_invisible_parens = lambda x, y: True # pragma: no cover
line_length = 80 # pragma: no cover
omit = set() # pragma: no cover
_first_right_hand_split = lambda l, omit: 'MockedRHSResult' # pragma: no cover
class Preview(Enum):# pragma: no cover
    prefer_splitting_right_hand_side_of_assignments = 1 # pragma: no cover
is_line_short_enough = lambda x, line_length: True # pragma: no cover
_prefer_split_rhs_oop = lambda x, line_length: False # pragma: no cover
_maybe_split_omitting_optional_parens = lambda x, y, z, features, omit: -1 # pragma: no cover
class CannotSplit(Exception):# pragma: no cover
    pass # pragma: no cover
can_be_split = lambda x: True # pragma: no cover
ensure_visible = lambda x: None # pragma: no cover
BRACKETS = set([token.LSQB, token.RSQB, token.LBRACE, token.RBRACE]) # pragma: no cover

from enum import Enum # pragma: no cover
import token # pragma: no cover

class Feature(Enum):# pragma: no cover
    FORCE_OPTIONAL_PARENTHESES = 1 # pragma: no cover
features = set() # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self, **kwargs):# pragma: no cover
        for key, value in kwargs.items():# pragma: no cover
            setattr(self, key, value)# pragma: no cover
# pragma: no cover
rhs = Mock(# pragma: no cover
    opening_bracket=Mock(type=token.LPAR, value=False),# pragma: no cover
    closing_bracket=Mock(type=token.RPAR, value=False),# pragma: no cover
    body=Mock(contains_standalone_comments=lambda x: False),# pragma: no cover
    head=Mock(# pragma: no cover
        leaves=[Mock(type=token.EQUAL), Mock(type=token.NAME)],# pragma: no cover
        magic_trailing_comma=None,# pragma: no cover
        contains_multiline_strings=lambda: False# pragma: no cover
    ),# pragma: no cover
    tail=Mock(contains_multiline_strings=lambda: False)# pragma: no cover
)# pragma: no cover
# pragma: no cover
can_omit_invisible_parens = lambda body, line_length: True # pragma: no cover
line_length = 80 # pragma: no cover
omit = set() # pragma: no cover
_first_right_hand_split = lambda line, omit: Mock() # pragma: no cover
class Preview(Enum):# pragma: no cover
    prefer_splitting_right_hand_side_of_assignments = 1 # pragma: no cover
is_line_short_enough = lambda head, line_length: True # pragma: no cover
_prefer_split_rhs_oop = lambda rhs_oop, line_length: False # pragma: no cover
_maybe_split_omitting_optional_parens = lambda rhs_oop, line, line_length, features, omit: Mock() # pragma: no cover
class CannotSplit(Exception):# pragma: no cover
    pass # pragma: no cover
can_be_split = lambda body: True # pragma: no cover
ensure_visible = lambda bracket: None # pragma: no cover
BRACKETS = {token.LPAR, token.RPAR, token.LSQB, token.RSQB, token.LBRACE, token.RBRACE} # pragma: no cover

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
