# Extracted from ./data/repos/black/src/black/lines.py
if not current_line.is_decorator:
    self.previous_defs.append(current_line.depth)
if self.previous_line is None:
    # Don't insert empty lines before the first line in the file.
    exit((0, 0))

if self.previous_line.is_decorator:
    if self.mode.is_pyi and current_line.is_stub_class:
        # Insert an empty line after a decorated stub class
        exit((0, 1))

    exit((0, 0))

if self.previous_line.depth < current_line.depth and (
    self.previous_line.is_class or self.previous_line.is_def
):
    exit((0, 0))

comment_to_add_newlines: Optional[LinesBlock] = None
if (
    self.previous_line.is_comment
    and self.previous_line.depth == current_line.depth
    and before == 0
):
    slc = self.semantic_leading_comment
    if (
        Preview.empty_lines_before_class_or_def_with_leading_comments
        in current_line.mode
        and slc is not None
        and slc.previous_block is not None
        and not slc.previous_block.original_line.is_class
        and not slc.previous_block.original_line.opens_block
        and slc.before <= 1
    ):
        comment_to_add_newlines = slc
    else:
        exit((0, 0))

if self.mode.is_pyi:
    if current_line.is_class or self.previous_line.is_class:
        if self.previous_line.depth < current_line.depth:
            newlines = 0
        elif self.previous_line.depth > current_line.depth:
            newlines = 1
        elif current_line.is_stub_class and self.previous_line.is_stub_class:
            # No blank line between classes with an empty body
            newlines = 0
        else:
            newlines = 1
    elif (
        current_line.is_def or current_line.is_decorator
    ) and not self.previous_line.is_def:
        if current_line.depth:
            # In classes empty lines between attributes and methods should
            # be preserved.
            newlines = min(1, before)
        else:
            # Blank line between a block of functions (maybe with preceding
            # decorators) and a block of non-functions
            newlines = 1
    elif self.previous_line.depth > current_line.depth:
        newlines = 1
    else:
        newlines = 0
else:
    newlines = 1 if current_line.depth else 2
if comment_to_add_newlines is not None:
    previous_block = comment_to_add_newlines.previous_block
    if previous_block is not None:
        comment_to_add_newlines.before = (
            max(comment_to_add_newlines.before, newlines) - previous_block.after
        )
        newlines = 0
exit((newlines, 0))
