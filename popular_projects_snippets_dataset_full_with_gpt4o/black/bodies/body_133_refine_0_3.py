from typing import List # pragma: no cover

target_versions: List[str] = [] # pragma: no cover
pygram = type('Mock', (object,), { 'python_grammar_no_print_statement_no_exec_statement_async_keywords': 'Python 3.7+', 'python_grammar_no_print_statement_no_exec_statement': 'Python 3.0-3.6', 'python_grammar_soft_keywords': 'Python 3.10+' }) # pragma: no cover
def supports_feature(target_versions: List[str], feature: 'Feature') -> bool:# pragma: no cover
    return feature in target_versions # pragma: no cover
Feature = type('Mock', (object,), { 'ASYNC_IDENTIFIERS': 'ASYNC_IDENTIFIERS', 'PATTERN_MATCHING': 'PATTERN_MATCHING', 'ASYNC_KEYWORDS': 'ASYNC_KEYWORDS' }) # pragma: no cover

from typing import List # pragma: no cover

target_versions: List[str] = [] # pragma: no cover
pygram = type('Mock', (object,), { 'python_grammar_no_print_statement_no_exec_statement_async_keywords': object(), 'python_grammar_no_print_statement_no_exec_statement': object(), 'python_grammar_soft_keywords': object() }) # pragma: no cover
def supports_feature(target_versions: List[str], feature: 'Feature') -> bool:# pragma: no cover
    return feature.value in target_versions # pragma: no cover
Feature = type('Mock', (object,), { 'ASYNC_IDENTIFIERS': type('MockFeature', (object,), { 'value': 'ASYNC_IDENTIFIERS' }), 'PATTERN_MATCHING': type('MockFeature', (object,), { 'value': 'PATTERN_MATCHING' }), 'ASYNC_KEYWORDS': type('MockFeature', (object,), { 'value': 'ASYNC_KEYWORDS' }) }) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
if not target_versions:
    _l_(17242)

    aux = [
        # Python 3.7+
        pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords,
        # Python 3.0-3.6
        pygram.python_grammar_no_print_statement_no_exec_statement,
        # Python 3.10+
        pygram.python_grammar_soft_keywords,
    ]
    _l_(17241)
    # No target_version specified, so try all grammars.
    exit(aux)

grammars = []
_l_(17243)
# If we have to parse both, try to parse async as a keyword first
if not supports_feature(
    target_versions, Feature.ASYNC_IDENTIFIERS
) and not supports_feature(target_versions, Feature.PATTERN_MATCHING):
    _l_(17245)

    # Python 3.7-3.9
    grammars.append(
        pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords
    )
    _l_(17244)
if not supports_feature(target_versions, Feature.ASYNC_KEYWORDS):
    _l_(17247)

    # Python 3.0-3.6
    grammars.append(pygram.python_grammar_no_print_statement_no_exec_statement)
    _l_(17246)
if supports_feature(target_versions, Feature.PATTERN_MATCHING):
    _l_(17249)

    # Python 3.10+
    grammars.append(pygram.python_grammar_soft_keywords)
    _l_(17248)
aux = grammars
_l_(17250)

# At least one of the above branches must have been taken, because every Python
# version has exactly one of the two 'ASYNC_*' flags
exit(aux)
