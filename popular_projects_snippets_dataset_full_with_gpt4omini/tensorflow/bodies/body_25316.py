# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
run_start_intro = cli_shared.get_run_start_intro(12, self.const_a, None, {})

# Verify line about run() call number.
self.assertTrue(run_start_intro.lines[1].endswith("run() call #12:"))

# Verify line about fetch.
const_a_name_line = run_start_intro.lines[4]
self.assertEqual(self.const_a.name, const_a_name_line.strip())

# Verify line about feeds.
feeds_line = run_start_intro.lines[7]
self.assertEqual("(Empty)", feeds_line.strip())

# Verify lines about possible commands and their font attributes.
self.assertEqual("run:", run_start_intro.lines[11][2:])
annot = run_start_intro.font_attr_segs[11][0]
self.assertEqual(2, annot[0])
self.assertEqual(5, annot[1])
self.assertEqual("run", annot[2][0].content)
self.assertEqual("bold", annot[2][1])
annot = run_start_intro.font_attr_segs[13][0]
self.assertEqual(2, annot[0])
self.assertEqual(8, annot[1])
self.assertEqual("run -n", annot[2][0].content)
self.assertEqual("bold", annot[2][1])
self.assertEqual("run -t <T>:", run_start_intro.lines[15][2:])
self.assertEqual([(2, 12, "bold")], run_start_intro.font_attr_segs[15])
self.assertEqual("run -f <filter_name>:", run_start_intro.lines[17][2:])
self.assertEqual([(2, 22, "bold")], run_start_intro.font_attr_segs[17])

# Verify short description.
description = cli_shared.get_run_short_description(12, self.const_a, None)
self.assertEqual("run #12: 1 fetch (a:0); 0 feeds", description)

# Verify the main menu associated with the run_start_intro.
self.assertIn(debugger_cli_common.MAIN_MENU_KEY,
              run_start_intro.annotations)
menu = run_start_intro.annotations[debugger_cli_common.MAIN_MENU_KEY]
self.assertEqual("run", menu.caption_to_item("run").content)
self.assertEqual("exit", menu.caption_to_item("exit").content)
