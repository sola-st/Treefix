# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
if self._op is not None:
    output = [
        "%s\n\nOriginal stack trace for %r:\n" % (
            self.message,
            self._op.name,
        )
    ]
    curr_traceback_list = traceback.format_list(self._op.traceback or [])
    output.extend(curr_traceback_list)
    # pylint: disable=protected-access
    original_op = self._op._original_op
    # pylint: enable=protected-access
    while original_op is not None:
        output.append(
            "\n...which was originally created as op %r, defined at:\n" %
            (original_op.name,))
        prev_traceback_list = curr_traceback_list
        curr_traceback_list = traceback.format_list(original_op.traceback or [])

        # Attempt to elide large common subsequences of the subsequent
        # stack traces.
        #
        # TODO(mrry): Consider computing the actual longest common subsequence.
        is_eliding = False
        elide_count = 0
        last_elided_line = None
        for line, line_in_prev in zip(curr_traceback_list, prev_traceback_list):
            if line == line_in_prev:
                if is_eliding:
                    elide_count += 1
                    last_elided_line = line
                else:
                    output.append(line)
                    is_eliding = True
                    elide_count = 0
            else:
                if is_eliding:
                    if elide_count > 0:
                        output.extend([
                            "[elided %d identical lines from previous traceback]\n" %
                            (elide_count - 1,), last_elided_line
                        ])
                    is_eliding = False
                output.extend(line)

        # pylint: disable=protected-access
        original_op = original_op._original_op
        # pylint: enable=protected-access
    exit("".join(output))
else:
    exit(self.message)
