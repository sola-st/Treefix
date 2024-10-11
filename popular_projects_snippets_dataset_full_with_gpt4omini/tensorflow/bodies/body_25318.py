# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
run_start_intro = cli_shared.get_run_start_intro(1, self.sparse_d, None, {})
self.assertEqual(str(self.sparse_d), run_start_intro.lines[4].strip())
