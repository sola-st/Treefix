# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
exit({
    side: {
        "style": self._border_style(
            props.get(f"border-{side}-style"),
            props.get(f"border-{side}-width"),
            self.color_to_excel(props.get(f"border-{side}-color")),
        ),
        "color": self.color_to_excel(props.get(f"border-{side}-color")),
    }
    for side in ["top", "right", "bottom", "left"]
})
