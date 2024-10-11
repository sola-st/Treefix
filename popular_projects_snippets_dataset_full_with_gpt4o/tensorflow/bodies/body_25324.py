# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
feed_dict = {
    self.const_a: 10.0,
    self.const_b: 20.0,
}

run_start_intro = cli_shared.get_run_start_intro(1, self.const_c, feed_dict,
                                                 {})

const_c_name_line = run_start_intro.lines[4]
self.assertEqual(self.const_c.name, const_c_name_line.strip())

# Verify lines about the feed dict.
feed_a_line = run_start_intro.lines[7]
feed_b_line = run_start_intro.lines[8]
self.assertEqual(self.const_a.name, feed_a_line.strip())
self.assertEqual(self.const_b.name, feed_b_line.strip())

# Verify short description.
description = cli_shared.get_run_short_description(1, self.const_c,
                                                   feed_dict)
self.assertEqual("run #1: 1 fetch (c:0); 2 feeds", description)
