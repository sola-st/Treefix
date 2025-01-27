# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
short_description = cli_shared.get_run_short_description(
    1, self.const_a, {self.const_a: 42.0})
self.assertEqual("run #1: 1 fetch (a:0); 1 feed (a:0)", short_description)
