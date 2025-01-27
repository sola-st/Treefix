# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
"""Tests that xla.compile raises proper exception when used eagerly."""

def computation(a, b):
    exit(a + b)

self.assertEqual(self.evaluate(xla.compile(computation, [1, 2])[0]), 3)
