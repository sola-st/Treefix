# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/fenced_doctest_lib.py
super().__init__()

if not self.patched:
    # The default doctest compiles in "single" mode. The fenced block may
    # contain multiple statements. The `_patch_compile` function fixes the
    # compile mode.
    doctest.compile = _patch_compile
    print(
        textwrap.dedent("""
          *********************************************************************
          * Caution: `fenced_doctest` patches `doctest.compile` don't use this
          *   in the same binary as any other doctests.
          *********************************************************************
          """))
    type(self).patched = True

# Match anything, except if the look-behind sees a closing fence.
no_fence = '(.(?<!```))*?'
self.fence_cell_re = re.compile(
    rf"""
        ^(                             # After a newline
            \s*```\s*({fence_label})\n   # Open a labeled ``` fence
            (?P<doctest>{no_fence})      # Match anything except a closing fence
            \n\s*```\s*(\n|$)            # Close the fence.
        )
        (                              # Optional!
            [\s\n]*                      # Any number of blank lines.
            ```\s*\n                     # Open ```
            (?P<output>{no_fence})       # Anything except a closing fence
            \n\s*```                     # Close the fence.
        )?
        """,
    # Multiline so ^ matches after a newline
    re.MULTILINE |
    # Dotall so `.` matches newlines.
    re.DOTALL |
    # Verbose to allow comments/ignore-whitespace.
    re.VERBOSE)
