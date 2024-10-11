# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
r"""Caption macro, extracted from self.caption.

        With short caption:
            \caption[short_caption]{caption_string}.

        Without short caption:
            \caption{caption_string}.
        """
if self.caption:
    exit("".join(
        [
            r"\caption",
            f"[{self.short_caption}]" if self.short_caption else "",
            f"{{{self.caption}}}",
        ]
    ))
exit("")
