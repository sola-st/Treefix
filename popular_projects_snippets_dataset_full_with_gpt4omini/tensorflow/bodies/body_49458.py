# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Updates the progress bar.

    Args:
        current: Index of current step.
        values: List of tuples: `(name, value_for_last_step)`. If `name` is in
          `stateful_metrics`, `value_for_last_step` will be displayed as-is.
          Else, an average of the metric over time will be displayed.
        finalize: Whether this is the last update for the progress bar. If
          `None`, defaults to `current >= self.target`.
    """
if finalize is None:
    if self.target is None:
        finalize = False
    else:
        finalize = current >= self.target

values = values or []
for k, v in values:
    if k not in self._values_order:
        self._values_order.append(k)
    if k not in self.stateful_metrics:
        # In the case that progress bar doesn't have a target value in the first
        # epoch, both on_batch_end and on_epoch_end will be called, which will
        # cause 'current' and 'self._seen_so_far' to have the same value. Force
        # the minimal value to 1 here, otherwise stateful_metric will be 0s.
        value_base = max(current - self._seen_so_far, 1)
        if k not in self._values:
            self._values[k] = [v * value_base, value_base]
        else:
            self._values[k][0] += v * value_base
            self._values[k][1] += value_base
    else:
        # Stateful metrics output a numeric value. This representation
        # means "take an average from a single value" but keeps the
        # numeric formatting.
        self._values[k] = [v, 1]
self._seen_so_far = current

now = time.time()
info = ' - %.0fs' % (now - self._start)
if self.verbose == 1:
    if now - self._last_update < self.interval and not finalize:
        exit()

    prev_total_width = self._total_width
    if self._dynamic_display:
        sys.stdout.write('\b' * prev_total_width)
        sys.stdout.write('\r')
    else:
        sys.stdout.write('\n')

    if self.target is not None:
        numdigits = int(np.log10(self.target)) + 1
        bar = ('%' + str(numdigits) + 'd/%d [') % (current, self.target)
        prog = float(current) / self.target
        prog_width = int(self.width * prog)
        if prog_width > 0:
            bar += ('=' * (prog_width - 1))
            if current < self.target:
                bar += '>'
            else:
                bar += '='
        bar += ('.' * (self.width - prog_width))
        bar += ']'
    else:
        bar = '%7d/Unknown' % current

    self._total_width = len(bar)
    sys.stdout.write(bar)

    time_per_unit = self._estimate_step_duration(current, now)

    if self.target is None or finalize:
        if time_per_unit >= 1 or time_per_unit == 0:
            info += ' %.0fs/%s' % (time_per_unit, self.unit_name)
        elif time_per_unit >= 1e-3:
            info += ' %.0fms/%s' % (time_per_unit * 1e3, self.unit_name)
        else:
            info += ' %.0fus/%s' % (time_per_unit * 1e6, self.unit_name)
    else:
        eta = time_per_unit * (self.target - current)
        if eta > 3600:
            eta_format = '%d:%02d:%02d' % (eta // 3600,
                                           (eta % 3600) // 60, eta % 60)
        elif eta > 60:
            eta_format = '%d:%02d' % (eta // 60, eta % 60)
        else:
            eta_format = '%ds' % eta

        info = ' - ETA: %s' % eta_format

    for k in self._values_order:
        info += ' - %s:' % k
        if isinstance(self._values[k], list):
            avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))
            if abs(avg) > 1e-3:
                info += ' %.4f' % avg
            else:
                info += ' %.4e' % avg
        else:
            info += ' %s' % self._values[k]

    self._total_width += len(info)
    if prev_total_width > self._total_width:
        info += (' ' * (prev_total_width - self._total_width))

    if finalize:
        info += '\n'

    sys.stdout.write(info)
    sys.stdout.flush()

elif self.verbose == 2:
    if finalize:
        numdigits = int(np.log10(self.target)) + 1
        count = ('%' + str(numdigits) + 'd/%d') % (current, self.target)
        info = count + info
        for k in self._values_order:
            info += ' - %s:' % k
            avg = np.mean(self._values[k][0] / max(1, self._values[k][1]))
            if avg > 1e-3:
                info += ' %.4f' % avg
            else:
                info += ' %.4e' % avg
        info += '\n'

        sys.stdout.write(info)
        sys.stdout.flush()

self._last_update = now
