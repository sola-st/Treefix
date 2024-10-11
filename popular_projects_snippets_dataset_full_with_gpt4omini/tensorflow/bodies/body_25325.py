# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
feed_dict = {self.const_a: 10.0}
tensor_filters = {
    "filter_a": lambda x: True,
    "filter_b": lambda x: False,
}

run_start_intro = cli_shared.get_run_start_intro(1, self.const_c, feed_dict,
                                                 tensor_filters)

# Verify the listed names of the tensor filters.
filter_names = set()
filter_names.add(run_start_intro.lines[20].split(" ")[-1])
filter_names.add(run_start_intro.lines[21].split(" ")[-1])

self.assertEqual({"filter_a", "filter_b"}, filter_names)

# Verify short description.
description = cli_shared.get_run_short_description(1, self.const_c,
                                                   feed_dict)
self.assertEqual("run #1: 1 fetch (c:0); 1 feed (a:0)", description)

# Verify the command links for the two filters.
command_set = set()
annot = run_start_intro.font_attr_segs[20][0]
command_set.add(annot[2].content)
annot = run_start_intro.font_attr_segs[21][0]
command_set.add(annot[2].content)
self.assertEqual({"run -f filter_a", "run -f filter_b"}, command_set)
