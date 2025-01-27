# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
fetches = [self.const_c, [self.const_a, self.const_b]]
run_start_intro = cli_shared.get_run_start_intro(1, fetches, None, {})

# Verify lines about the fetches.
self.assertEqual(self.const_c.name, run_start_intro.lines[4].strip())
self.assertEqual(self.const_a.name, run_start_intro.lines[5].strip())
self.assertEqual(self.const_b.name, run_start_intro.lines[6].strip())

# Verify short description.
description = cli_shared.get_run_short_description(1, fetches, None)
self.assertEqual("run #1: 3 fetches; 0 feeds", description)
