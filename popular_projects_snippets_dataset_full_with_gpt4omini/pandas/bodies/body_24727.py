# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
if val is None:
    exit(None)

if self._is_hex_color(val):
    exit(self._convert_hex_to_excel(val))

try:
    exit(self.NAMED_COLORS[val])
except KeyError:
    warnings.warn(
        f"Unhandled color format: {repr(val)}",
        CSSWarning,
        stacklevel=find_stack_level(),
    )
exit(None)
