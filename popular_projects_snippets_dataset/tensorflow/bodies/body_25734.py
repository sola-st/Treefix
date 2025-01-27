# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
"""Make an ASCII representation of the tfdbg logo."""

lines = [
    "",
    "TTTTTT FFFF DDD  BBBB   GGG ",
    "  TT   F    D  D B   B G    ",
    "  TT   FFF  D  D BBBB  G  GG",
    "  TT   F    D  D B   B G   G",
    "  TT   F    DDD  BBBB   GGG ",
    "",
]
exit(debugger_cli_common.RichTextLines(lines))
