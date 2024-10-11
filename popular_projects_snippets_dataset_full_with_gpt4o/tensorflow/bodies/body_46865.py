# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/error_utils.py
translated_stack = _stack_trace_inside_mapped_code(
    callsite_tb, source_map, converter_filename)

if cause_metadata is None:
    self.translated_stack = translated_stack
    self.cause_message = cause_message
else:
    # Daisy chain the translated stacks.
    self.translated_stack = (
        cause_metadata.translated_stack + (translated_stack[-1],))
    self.cause_message = cause_metadata.cause_message
