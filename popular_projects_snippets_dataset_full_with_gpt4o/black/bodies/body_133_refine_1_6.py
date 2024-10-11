from types import SimpleNamespace # pragma: no cover

target_versions = [] # pragma: no cover
pygram = SimpleNamespace(# pragma: no cover
    python_grammar_no_print_statement_no_exec_statement_no_async_keywords='Python 3.0-3.6 Grammar',# pragma: no cover
    python_grammar_no_print_statement_no_exec_statement='Python 3.7-3.9 Grammar',# pragma: no cover
    python_grammar_soft_keywords='Python 3.10+ Grammar'# pragma: no cover
) # pragma: no cover
supports_feature = lambda target_versions, feature: False # pragma: no cover
Feature = SimpleNamespace(# pragma: no cover
    ASYNC_IDENTIFIERS='async_identifiers',# pragma: no cover
    PATTERN_MATCHING='pattern_matching',# pragma: no cover
    ASYNC_KEYWORDS='async_keywords'# pragma: no cover
) # pragma: no cover

from types import SimpleNamespace # pragma: no cover

target_versions = [] # pragma: no cover
pygram = SimpleNamespace(# pragma: no cover
    python_grammar_no_print_statement_no_exec_statement_no_async_keywords='Python 3.0-3.6 Grammar',# pragma: no cover
    python_grammar_no_print_statement_no_exec_statement_async_keywords='Python 3.7-3.9 Grammar',# pragma: no cover
    python_grammar_soft_keywords='Python 3.10+ Grammar'# pragma: no cover
) # pragma: no cover
supports_feature = lambda target_versions, feature: False # pragma: no cover
Feature = SimpleNamespace(# pragma: no cover
    ASYNC_IDENTIFIERS='async_identifiers',# pragma: no cover
    PATTERN_MATCHING='pattern_matching',# pragma: no cover
    ASYNC_KEYWORDS='async_keywords'# pragma: no cover
) # pragma: no cover

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
