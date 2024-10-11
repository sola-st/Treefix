from typing import List, Dict, Any # pragma: no cover

target_versions: List[str] = [] # pragma: no cover
pygram: Any = type('Mock', (object,), { # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement_async_keywords': 'Grammar_Async_Keywords', # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement': 'Grammar_No_Print_No_Exec', # pragma: no cover
    'python_grammar_soft_keywords': 'Soft_Keywords_Grammar' # pragma: no cover
}) # pragma: no cover
Feature: Any = type('Mock', (object,), { # pragma: no cover
    'ASYNC_IDENTIFIERS': 'ASYNC_IDENTIFIERS', # pragma: no cover
    'PATTERN_MATCHING': 'PATTERN_MATCHING', # pragma: no cover
    'ASYNC_KEYWORDS': 'ASYNC_KEYWORDS' # pragma: no cover
}) # pragma: no cover
def supports_feature(versions: List[str], feature: str) -> bool: # pragma: no cover
    # Dummy implementation for the purpose of making the snippet executable # pragma: no cover
    # In reality, you should replace this with proper logic # pragma: no cover
    features_supported: Dict[str, List[str]] = { # pragma: no cover
        'ASYNC_IDENTIFIERS': ['3.7', '3.8', '3.9'], # pragma: no cover
        'PATTERN_MATCHING': ['3.10', '3.11'], # pragma: no cover
        'ASYNC_KEYWORDS': ['3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.6'] # pragma: no cover
    } # pragma: no cover
    for version in versions: # pragma: no cover
        if feature in features_supported and version in features_supported[feature]: # pragma: no cover
            return True # pragma: no cover
    return False # pragma: no cover

import sys # pragma: no cover
from typing import List # pragma: no cover

target_versions: List[str] = [] # pragma: no cover
pygram = type('Mock', (object,), { # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement_async_keywords': 'Grammar_Async_Keywords', # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement': 'Grammar_No_Print_No_Exec', # pragma: no cover
    'python_grammar_soft_keywords': 'Soft_Keywords_Grammar' # pragma: no cover
})() # pragma: no cover
Feature = type('Mock', (object,), { # pragma: no cover
    'ASYNC_IDENTIFIERS': 'ASYNC_IDENTIFIERS', # pragma: no cover
    'PATTERN_MATCHING': 'PATTERN_MATCHING', # pragma: no cover
    'ASYNC_KEYWORDS': 'ASYNC_KEYWORDS' # pragma: no cover
})() # pragma: no cover
def supports_feature(versions: List[str], feature: str) -> bool: # pragma: no cover
    # Dummy implementation for the purpose of making the snippet executable # pragma: no cover
    # In reality, you should replace this with proper logic # pragma: no cover
    features_supported = { # pragma: no cover
        Feature.ASYNC_IDENTIFIERS: False, # pragma: no cover
        Feature.PATTERN_MATCHING: False, # pragma: no cover
        Feature.ASYNC_KEYWORDS: False # pragma: no cover
    } # pragma: no cover
    return features_supported.get(feature, False) # pragma: no cover
sys.exit = lambda x: x # pragma: no cover

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
