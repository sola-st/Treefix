# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/loader_test.py
test_source = textwrap.dedent(u"""
      # coding=utf-8
      def f(a):
        '日本語 Δθₜ ← Δθₜ₋₁ + ∇Q(sₜ, aₜ)(rₜ + γₜ₊₁ max Q(⋅))'
        return a + 1
    """)
module, _ = loader.load_source(test_source, delete_on_exit=True)
self.assertEqual(module.f(1), 2)
self.assertEqual(
    module.f.__doc__, '日本語 Δθₜ ← Δθₜ₋₁ + ∇Q(sₜ, aₜ)(rₜ + γₜ₊₁ max Q(⋅))')
