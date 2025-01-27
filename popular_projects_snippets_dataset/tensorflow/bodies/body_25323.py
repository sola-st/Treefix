# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
fetches_namedtuple = namedtuple("fetches", "x y")
fetches = fetches_namedtuple(self.const_b, self.const_c)
run_start_intro = cli_shared.get_run_start_intro(1, fetches, None, {})

const_b_name_line = run_start_intro.lines[4]
const_c_name_line = run_start_intro.lines[5]
self.assertEqual(self.const_b.name, const_b_name_line.strip())
self.assertEqual(self.const_c.name, const_c_name_line.strip())

feeds_line = run_start_intro.lines[8]
self.assertEqual("(Empty)", feeds_line.strip())

# Verify short description.
description = cli_shared.get_run_short_description(1, fetches, None)
self.assertEqual("run #1: 2 fetches; 0 feeds", description)
