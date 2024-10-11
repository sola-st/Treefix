# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
fetches = {"c": self.const_c, "ab": {"a": self.const_a, "b": self.const_b}}
run_start_intro = cli_shared.get_run_start_intro(1, fetches, None, {})

# Verify lines about the fetches. The ordering of the dict keys is
# indeterminate.
fetch_names = set()
fetch_names.add(run_start_intro.lines[4].strip())
fetch_names.add(run_start_intro.lines[5].strip())
fetch_names.add(run_start_intro.lines[6].strip())

self.assertEqual({"a:0", "b:0", "c:0"}, fetch_names)

# Verify short description.
description = cli_shared.get_run_short_description(1, fetches, None)
self.assertEqual("run #1: 3 fetches; 0 feeds", description)
