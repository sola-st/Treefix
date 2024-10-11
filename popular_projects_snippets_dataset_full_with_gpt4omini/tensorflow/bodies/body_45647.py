# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
"""Tests whether the CFG has the specified entry and exits."""
self.assertEqual(repr(graph.entry), entry_repr)
self.assertSetEqual(frozenset(map(repr, graph.exit)), frozenset(exit_reprs))
