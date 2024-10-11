from typing import List # pragma: no cover

target_versions = [] # pragma: no cover
class Mock: pass # pragma: no cover
pygram = type('MockPygram', (object,), { # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement_async_keywords': 'Grammar for Python 3.7+ with async keywords', # pragma: no cover
    'python_grammar_no_print_statement_no_exec_statement': 'Grammar for Python 3.0-3.6 without print and exec statements', # pragma: no cover
    'python_grammar_soft_keywords': 'Grammar for Python 3.10+ with soft keywords' # pragma: no cover
})() # pragma: no cover
def supports_feature(target_versions: List[int], feature): # pragma: no cover
    return True # pragma: no cover
class Feature: # pragma: no cover
    ASYNC_IDENTIFIERS = 1, # pragma: no cover
    PATTERN_MATCHING = 2, # pragma: no cover
    ASYNC_KEYWORDS = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
from l3.Runtime import _l_
if not target_versions:
    _l_(5530)

    aux = [
        # Python 3.7+
        pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords,
        # Python 3.0-3.6
        pygram.python_grammar_no_print_statement_no_exec_statement,
        # Python 3.10+
        pygram.python_grammar_soft_keywords,
    ]
    _l_(5529)
    # No target_version specified, so try all grammars.
    exit(aux)

grammars = []
_l_(5531)
# If we have to parse both, try to parse async as a keyword first
if not supports_feature(
    target_versions, Feature.ASYNC_IDENTIFIERS
) and not supports_feature(target_versions, Feature.PATTERN_MATCHING):
    _l_(5533)

    # Python 3.7-3.9
    grammars.append(
        pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords
    )
    _l_(5532)
if not supports_feature(target_versions, Feature.ASYNC_KEYWORDS):
    _l_(5535)

    # Python 3.0-3.6
    grammars.append(pygram.python_grammar_no_print_statement_no_exec_statement)
    _l_(5534)
if supports_feature(target_versions, Feature.PATTERN_MATCHING):
    _l_(5537)

    # Python 3.10+
    grammars.append(pygram.python_grammar_soft_keywords)
    _l_(5536)
aux = grammars
_l_(5538)

# At least one of the above branches must have been taken, because every Python
# version has exactly one of the two 'ASYNC_*' flags
exit(aux)
