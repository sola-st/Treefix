from typing import List # pragma: no cover
class Feature: # pragma: no cover
    ASYNC_IDENTIFIERS = 'async_identifiers' # pragma: no cover
    PATTERN_MATCHING = 'pattern_matching' # pragma: no cover
    ASYNC_KEYWORDS = 'async_keywords' # pragma: no cover
class Pygram: # pragma: no cover
    python_grammar_no_print_statement_no_exec_statement_async_keywords = 'grammar_async_keywords' # pragma: no cover
    python_grammar_no_print_statement_no_exec_statement = 'grammar_no_print_no_exec' # pragma: no cover
    python_grammar_soft_keywords = 'grammar_soft_keywords' # pragma: no cover
def supports_feature(target_versions: List[str], feature: str) -> bool: # pragma: no cover
    return feature in target_versions # pragma: no cover

target_versions = ['3.7', '3.8', '3.9'] # pragma: no cover
pygram = Pygram() # pragma: no cover
supports_feature = supports_feature # pragma: no cover

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
