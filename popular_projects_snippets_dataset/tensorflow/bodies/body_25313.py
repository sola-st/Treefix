# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared_test.py
self.assertEqual("40s",
                 cli_shared.time_to_readable_str(
                     40e6, force_time_unit=cli_shared.TIME_UNIT_S))
self.assertEqual("40000ms",
                 cli_shared.time_to_readable_str(
                     40e6, force_time_unit=cli_shared.TIME_UNIT_MS))
self.assertEqual("40000000us",
                 cli_shared.time_to_readable_str(
                     40e6, force_time_unit=cli_shared.TIME_UNIT_US))
self.assertEqual("4e-05s",
                 cli_shared.time_to_readable_str(
                     40, force_time_unit=cli_shared.TIME_UNIT_S))
self.assertEqual("0",
                 cli_shared.time_to_readable_str(
                     0, force_time_unit=cli_shared.TIME_UNIT_S))

with self.assertRaisesRegex(ValueError, r"Invalid time unit: ks"):
    cli_shared.time_to_readable_str(100, force_time_unit="ks")
