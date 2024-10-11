from typing import List, Optional, Any # pragma: no cover
from dataclasses import dataclass # pragma: no cover

STANDALONE_COMMENT = 'standalone_comment' # pragma: no cover
token = type('Mock', (object,), {'STRING': 'string', 'COMMA': 'comma'})() # pragma: no cover
class TErr(Exception): pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""Validate (M)erge (S)tring (G)roup

        Transform-time string validation logic for _merge_string_group(...).

        Returns:
            * Ok(None), if ALL validation checks (listed below) pass.
                OR
            * Err(CannotTransform), if any of the following are true:
                - The target string group does not contain ANY stand-alone comments.
                - The target string is not in a string group (i.e. it has no
                  adjacent strings).
                - The string group has more than one inline comment.
                - The string group has an inline comment that appears to be a pragma.
                - The set of all string prefixes in the string group is of
                  length greater than one and is not equal to {"", "f"}.
                - The string group consists of raw strings.
                - The string group is stringified type annotations. We don't want to
                  process stringified type annotations since pyright doesn't support
                  them spanning multiple string values. (NOTE: mypy, pytype, pyre do
                  support them, so we can change if pyright also gains support in the
                  future. See https://github.com/microsoft/pyright/issues/4359.)
        """
# We first check for "inner" stand-alone comments (i.e. stand-alone
# comments that have a string leaf before them AND after them).
for inc in [1, -1]:
    _l_(5837)

    i = string_idx
    _l_(5828)
    found_sa_comment = False
    _l_(5829)
    is_valid_index = is_valid_index_factory(line.leaves)
    _l_(5830)
    while is_valid_index(i) and line.leaves[i].type in [
        token.STRING,
        STANDALONE_COMMENT,
    ]:
        _l_(5836)

        if line.leaves[i].type == STANDALONE_COMMENT:
            _l_(5834)

            found_sa_comment = True
            _l_(5831)
        elif found_sa_comment:
            _l_(5833)

            aux = TErr(
                "StringMerger does NOT merge string groups which contain "
                "stand-alone comments."
            )
            _l_(5832)
            exit(aux)

        i += inc
        _l_(5835)

num_of_inline_string_comments = 0
_l_(5838)
set_of_prefixes = set()
_l_(5839)
num_of_strings = 0
_l_(5840)
for leaf in line.leaves[string_idx:]:
    _l_(5856)

    if leaf.type != token.STRING:
        _l_(5844)

        # If the string group is trailed by a comma, we count the
        # comments trailing the comma to be one of the string group's
        # comments.
        if leaf.type == token.COMMA and id(leaf) in line.comments:
            _l_(5842)

            num_of_inline_string_comments += 1
            _l_(5841)
        break
        _l_(5843)

    if has_triple_quotes(leaf.value):
        _l_(5846)

        aux = TErr("StringMerger does NOT merge multiline strings.")
        _l_(5845)
        exit(aux)

    num_of_strings += 1
    _l_(5847)
    prefix = get_string_prefix(leaf.value).lower()
    _l_(5848)
    if "r" in prefix:
        _l_(5850)

        aux = TErr("StringMerger does NOT merge raw strings.")
        _l_(5849)
        exit(aux)

    set_of_prefixes.add(prefix)
    _l_(5851)

    if id(leaf) in line.comments:
        _l_(5855)

        num_of_inline_string_comments += 1
        _l_(5852)
        if contains_pragma_comment(line.comments[id(leaf)]):
            _l_(5854)

            aux = TErr("Cannot merge strings which have pragma comments.")
            _l_(5853)
            exit(aux)

if num_of_strings < 2:
    _l_(5858)

    aux = TErr(
        f"Not enough strings to merge (num_of_strings={num_of_strings})."
    )
    _l_(5857)
    exit(aux)

if num_of_inline_string_comments > 1:
    _l_(5860)

    aux = TErr(
        f"Too many inline string comments ({num_of_inline_string_comments})."
    )
    _l_(5859)
    exit(aux)

if len(set_of_prefixes) > 1 and set_of_prefixes != {"", "f"}:
    _l_(5862)

    aux = TErr(f"Too many different prefixes ({set_of_prefixes}).")
    _l_(5861)
    exit(aux)
aux = Ok(None)
_l_(5863)

exit(aux)
