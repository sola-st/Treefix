from typing import List, Any # pragma: no cover

target_versions = [] # pragma: no cover
pygram = type('Mock', (object,), { # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement_async_keywords': 'Grammar_Python_3.7_Plus', # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement': 'Grammar_Python_3_0_to_3_6', # pragma: no cover
    'python_grammar_soft_keywords': 'Grammar_Python_3_10_Plus' # pragma: no cover
}) # pragma: no cover
Feature = type('Mock', (object,), { # pragma: no cover
    'ASYNC_IDENTIFIERS': 'ASYNC_IDENTIFIERS', # pragma: no cover
    'PATTERN_MATCHING': 'PATTERN_MATCHING', # pragma: no cover
    'ASYNC_KEYWORDS': 'ASYNC_KEYWORDS' # pragma: no cover
}) # pragma: no cover
def supports_feature(target_versions: List[Any], feature: Any) -> bool: # pragma: no cover
    # Assume a simple condition check based on the feature # pragma: no cover
    return feature in ['ASYNC_IDENTIFIERS', 'PATTERN_MATCHING', 'ASYNC_KEYWORDS'] # pragma: no cover

from typing import List # pragma: no cover
import sys # pragma: no cover

target_versions = [] # pragma: no cover
class MockPygram: # pragma: no cover
    python_grammar_no_print_statement_no_exec_statement_async_keywords = object() # pragma: no cover
    python_grammar_no_print_statement_no_exec_statement = object() # pragma: no cover
    python_grammar_soft_keywords = object() # pragma: no cover
pygram = MockPygram() # pragma: no cover
class Feature: # pragma: no cover
    ASYNC_IDENTIFIERS = 'ASYNC_IDENTIFIERS' # pragma: no cover
    PATTERN_MATCHING = 'PATTERN_MATCHING' # pragma: no cover
    ASYNC_KEYWORDS = 'ASYNC_KEYWORDS' # pragma: no cover
def supports_feature(target_versions: List[str], feature: str) -> bool: # pragma: no cover
    # Assume all features are not supported for simplicity # pragma: no cover
    return False # pragma: no cover
# Replace exit to print to handle lists and avoid system exit in the example # pragma: no cover
    print(data) # pragma: no cover

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
