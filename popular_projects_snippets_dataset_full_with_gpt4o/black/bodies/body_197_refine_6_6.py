from typing import List, Optional # pragma: no cover
from lib2to3.pgen2 import driver # pragma: no cover
from dataclasses import dataclass # pragma: no cover
import enum # pragma: no cover

lib2to3_parse = lambda src_contents, version: Parse(driver.Driver(driver.load_grammar('Grammar.txt', 'PatternGrammar.txt')).grammar, driver.convert, src_contents) # pragma: no cover
src_contents = 'def example():\n    pass\n' # pragma: no cover
mode = type('Mode', (object,), {'target_versions': None, 'preview': False})() # pragma: no cover
@dataclass# pragma: no cover
class LinesBlock:# pragma: no cover
    content_lines: List[str] = None# pragma: no cover
    after: int = 0# pragma: no cover
    def all_lines(self):# pragma: no cover
        return self.content_lines if self.content_lines else [] # pragma: no cover
class Feature(enum.Enum):# pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = 0# pragma: no cover
    TRAILING_COMMA_IN_CALL = 1# pragma: no cover
    TRAILING_COMMA_IN_DEF = 2 # pragma: no cover
normalize_fmt_off = lambda src_node, preview: None # pragma: no cover
LineGenerator = type('LineGenerator', (object,), {'__init__': lambda self, mode, features: None, 'visit': lambda self, src_node: ['example line']}) # pragma: no cover
EmptyLineTracker = type('EmptyLineTracker', (object,), {'__init__': lambda self, mode: None, 'maybe_empty_lines': lambda self, current_line: LinesBlock([])}) # pragma: no cover
transform_line = lambda current_line, mode, features: [current_line] # pragma: no cover
decode_bytes = lambda byte_str: (byte_str.decode('utf-8').strip(), '', '\n') # pragma: no cover
supports_feature = lambda versions, feature: False # pragma: no cover

from typing import List, Optional # pragma: no cover
from unittest.mock import Mock # pragma: no cover
from collections import namedtuple # pragma: no cover

lib2to3_parse = lambda src_contents, version: Mock() # pragma: no cover
src_contents = 'def example():\n    pass\n' # pragma: no cover
mode = type('Mode', (object,), {'target_versions': None, 'preview': False})() # pragma: no cover
LinesBlock = namedtuple('LinesBlock', ['content_lines', 'after', 'all_lines']) # pragma: no cover
class Feature:# pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = 'PARENTHESIZED_CONTEXT_MANAGERS'# pragma: no cover
    TRAILING_COMMA_IN_CALL = 'TRAILING_COMMA_IN_CALL'# pragma: no cover
    TRAILING_COMMA_IN_DEF = 'TRAILING_COMMA_IN_DEF' # pragma: no cover
normalize_fmt_off = lambda src_node, preview: None # pragma: no cover
LineGenerator = lambda mode, features: Mock(visit=lambda src_node: iter(['line1', 'line2'])) # pragma: no cover
EmptyLineTracker = lambda mode: Mock(maybe_empty_lines=lambda current_line: LinesBlock(content_lines=[], after=0, all_lines=lambda: [])) # pragma: no cover
transform_line = lambda current_line, mode, features: iter([current_line]) # pragma: no cover
decode_bytes = lambda src: ('def example():\n    pass\n', None, '\n') # pragma: no cover
supports_feature = lambda versions, feature: True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
src_node = lib2to3_parse(src_contents.lstrip(), mode.target_versions)
_l_(16122)
dst_blocks: List[LinesBlock] = []
_l_(16123)
if mode.target_versions:
    _l_(16127)

    versions = mode.target_versions
    _l_(16124)
else:
    future_imports = get_future_imports(src_node)
    _l_(16125)
    versions = detect_target_versions(src_node, future_imports=future_imports)
    _l_(16126)

context_manager_features = {
    feature
    for feature in {Feature.PARENTHESIZED_CONTEXT_MANAGERS}
    if supports_feature(versions, feature)
}
_l_(16128)
normalize_fmt_off(src_node, preview=mode.preview)
_l_(16129)
lines = LineGenerator(mode=mode, features=context_manager_features)
_l_(16130)
elt = EmptyLineTracker(mode=mode)
_l_(16131)
split_line_features = {
    feature
    for feature in {Feature.TRAILING_COMMA_IN_CALL, Feature.TRAILING_COMMA_IN_DEF}
    if supports_feature(versions, feature)
}
_l_(16132)
block: Optional[LinesBlock] = None
_l_(16133)
for current_line in lines.visit(src_node):
    _l_(16138)

    block = elt.maybe_empty_lines(current_line)
    _l_(16134)
    dst_blocks.append(block)
    _l_(16135)
    for line in transform_line(
        current_line, mode=mode, features=split_line_features
    ):
        _l_(16137)

        block.content_lines.append(str(line))
        _l_(16136)
if dst_blocks:
    _l_(16140)

    dst_blocks[-1].after = 0
    _l_(16139)
dst_contents = []
_l_(16141)
for block in dst_blocks:
    _l_(16143)

    dst_contents.extend(block.all_lines())
    _l_(16142)
if mode.preview and not dst_contents:
    _l_(16148)

    # Use decode_bytes to retrieve the correct source newline (CRLF or LF),
    # and check if normalized_content has more than one line
    normalized_content, _, newline = decode_bytes(src_contents.encode("utf-8"))
    _l_(16144)
    if "\n" in normalized_content:
        _l_(16146)

        aux = newline
        _l_(16145)
        exit(aux)
    aux = ""
    _l_(16147)
    exit(aux)
aux = "".join(dst_contents)
_l_(16149)
exit(aux)
