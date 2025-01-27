# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py
# GH#42748
yaml = import_module("yaml")

dumped = yaml.dump(df)

loaded = yaml.load(dumped, Loader=yaml.Loader)
tm.assert_frame_equal(df, loaded)

loaded2 = yaml.load(dumped, Loader=yaml.UnsafeLoader)
tm.assert_frame_equal(df, loaded2)
