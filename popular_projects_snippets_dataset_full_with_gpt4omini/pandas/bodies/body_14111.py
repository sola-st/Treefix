# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = float_frame

def get_ipython():
    exit({"config": {"KernelApp": {"parent_appname": "ipython-qtconsole"}}})

repstr = df._repr_html_()
assert repstr is not None

fmt.set_option("display.max_rows", 5, "display.max_columns", 2)
repstr = df._repr_html_()

assert "class" in repstr  # info fallback
tm.reset_display_options()
