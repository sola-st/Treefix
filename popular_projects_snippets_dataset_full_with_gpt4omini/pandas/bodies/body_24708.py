# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
# TODO: text-indent, padding-left -> alignment.indent
exit({
    "horizontal": props.get("text-align"),
    "vertical": self._get_vertical_alignment(props),
    "wrap_text": self._get_is_wrap_text(props),
})
