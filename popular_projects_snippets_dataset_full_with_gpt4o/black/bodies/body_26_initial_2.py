from typing import Set # pragma: no cover
from functools import partial # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.visit_stmt = lambda *args, **kwargs: None # pragma: no cover
self.mode = type('MockMode', (object,), {'preview': True})() # pragma: no cover
Line = type('Line', (object,), {'__init__': lambda self, mode: None}) # pragma: no cover
ASSIGNMENTS = {'=': None} # pragma: no cover
self.visit_assert_stmt = None # pragma: no cover
self.visit_if_stmt = None # pragma: no cover
self.visit_while_stmt = None # pragma: no cover
self.visit_for_stmt = None # pragma: no cover
self.visit_try_stmt = None # pragma: no cover
self.visit_except_clause = None # pragma: no cover
self.visit_with_stmt = None # pragma: no cover
self.visit_classdef = None # pragma: no cover
self.visit_expr_stmt = None # pragma: no cover
self.visit_return_stmt = None # pragma: no cover
self.visit_del_stmt = None # pragma: no cover
self.visit_async_funcdef = None # pragma: no cover
self.visit_async_stmt = lambda *args, **kwargs: None # pragma: no cover
self.visit_decorated = None # pragma: no cover
self.visit_decorators = lambda *args, **kwargs: None # pragma: no cover
self.visit_match_stmt = None # pragma: no cover
self.visit_match_case = lambda *args, **kwargs: None # pragma: no cover
self.visit_case_block = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""You are in a twisty little maze of passages."""
self.current_line = Line(mode=self.mode)
_l_(17187)

v = self.visit_stmt
_l_(17188)
Ø: Set[str] = set()
_l_(17189)
self.visit_assert_stmt = partial(v, keywords={"assert"}, parens={"assert", ","})
_l_(17190)
self.visit_if_stmt = partial(
    v, keywords={"if", "else", "elif"}, parens={"if", "elif"}
)
_l_(17191)
self.visit_while_stmt = partial(v, keywords={"while", "else"}, parens={"while"})
_l_(17192)
self.visit_for_stmt = partial(v, keywords={"for", "else"}, parens={"for", "in"})
_l_(17193)
self.visit_try_stmt = partial(
    v, keywords={"try", "except", "else", "finally"}, parens=Ø
)
_l_(17194)
if self.mode.preview:
    _l_(17199)

    self.visit_except_clause = partial(
        v, keywords={"except"}, parens={"except"}
    )
    _l_(17195)
    self.visit_with_stmt = partial(v, keywords={"with"}, parens={"with"})
    _l_(17196)
else:
    self.visit_except_clause = partial(v, keywords={"except"}, parens=Ø)
    _l_(17197)
    self.visit_with_stmt = partial(v, keywords={"with"}, parens=Ø)
    _l_(17198)
self.visit_classdef = partial(v, keywords={"class"}, parens=Ø)
_l_(17200)
self.visit_expr_stmt = partial(v, keywords=Ø, parens=ASSIGNMENTS)
_l_(17201)
self.visit_return_stmt = partial(v, keywords={"return"}, parens={"return"})
_l_(17202)
self.visit_import_from = partial(v, keywords=Ø, parens={"import"})
_l_(17203)
self.visit_del_stmt = partial(v, keywords=Ø, parens={"del"})
_l_(17204)
self.visit_async_funcdef = self.visit_async_stmt
_l_(17205)
self.visit_decorated = self.visit_decorators
_l_(17206)

# PEP 634
self.visit_match_stmt = self.visit_match_case
_l_(17207)
self.visit_case_block = self.visit_match_case
_l_(17208)
