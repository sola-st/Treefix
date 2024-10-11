# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
sparse_feed_val = ([[0, 0], [1, 1]], [10.0, 20.0])
run_start_intro = cli_shared.get_run_start_intro(
    1, self.sparse_d, {self.sparse_d: sparse_feed_val}, {})
self.assertEqual(str(self.sparse_d), run_start_intro.lines[7].strip())

short_description = cli_shared.get_run_short_description(
    1, self.sparse_d, {self.sparse_d: sparse_feed_val})
self.assertEqual(
    "run #1: 1 fetch; 1 feed (%s)" % self.sparse_d, short_description)
