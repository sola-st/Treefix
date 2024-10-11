from functools import partial # pragma: no cover
from typing import Set # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.mode = Mock() # pragma: no cover
self.mode.preview = False # pragma: no cover
self.visit_stmt = lambda x: x # pragma: no cover
Line = lambda mode: 'Line instance with mode ' + mode # pragma: no cover
ASSIGNMENTS = {'='} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""You are in a twisty little maze of passages."""
self.current_line = Line(mode=self.mode)
_l_(5766)

v = self.visit_stmt
_l_(5767)
Ø: Set[str] = set()
_l_(5768)
self.visit_assert_stmt = partial(v, keywords={"assert"}, parens={"assert", ","})
_l_(5769)
self.visit_if_stmt = partial(
    v, keywords={"if", "else", "elif"}, parens={"if", "elif"}
)
_l_(5770)
self.visit_while_stmt = partial(v, keywords={"while", "else"}, parens={"while"})
_l_(5771)
self.visit_for_stmt = partial(v, keywords={"for", "else"}, parens={"for", "in"})
_l_(5772)
self.visit_try_stmt = partial(
    v, keywords={"try", "except", "else", "finally"}, parens=Ø
)
_l_(5773)
if self.mode.preview:
    _l_(5778)

    self.visit_except_clause = partial(
        v, keywords={"except"}, parens={"except"}
    )
    _l_(5774)
    self.visit_with_stmt = partial(v, keywords={"with"}, parens={"with"})
    _l_(5775)
else:
    self.visit_except_clause = partial(v, keywords={"except"}, parens=Ø)
    _l_(5776)
    self.visit_with_stmt = partial(v, keywords={"with"}, parens=Ø)
    _l_(5777)
self.visit_classdef = partial(v, keywords={"class"}, parens=Ø)
_l_(5779)
self.visit_expr_stmt = partial(v, keywords=Ø, parens=ASSIGNMENTS)
_l_(5780)
self.visit_return_stmt = partial(v, keywords={"return"}, parens={"return"})
_l_(5781)
self.visit_import_from = partial(v, keywords=Ø, parens={"import"})
_l_(5782)
self.visit_del_stmt = partial(v, keywords=Ø, parens={"del"})
_l_(5783)
self.visit_async_funcdef = self.visit_async_stmt
_l_(5784)
self.visit_decorated = self.visit_decorators
_l_(5785)

# PEP 634
self.visit_match_stmt = self.visit_match_case
_l_(5786)
self.visit_case_block = self.visit_match_case
_l_(5787)
