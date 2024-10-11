# Extracted from ./data/repos/tensorflow/tensorflow/tools/benchmark/parse_onednn_benchmarks.py
"""Parses benchmark results from run_onednn_benchmarks.sh.

  Stores results in a global dict.

  Args:
    lines: Array of strings corresponding to each line of the output from
      run_onednn_benchmarks.sh

  Raises:
    RuntimeError: If the program reaches an unknown state.
  """
idx = 0
batch, onednn, model = None, None, None
state = State.FIND_CONFIG_OR_MODEL
while idx < len(lines):
    if state is State.FIND_CONFIG_OR_MODEL:
        config = re.match(
            r"\+ echo 'BATCH=(?P<batch>[\d]+), ONEDNN=(?P<onednn>[\d]+)",
            lines[idx])
        if config:
            batch = int(config.group("batch"))
            onednn = int(config.group("onednn"))
            batch_sizes.add(batch)
        else:
            model_re = re.search(r"tf-graphs\/(?P<model>[\w\d_-]+).pb", lines[idx])
            assert model_re
            model = model_re.group("model")
            models.add(model)
            state = State.FIND_RUNNING_TIME
    elif state is State.FIND_RUNNING_TIME:
        match = re.search(r"no stats: (?P<avg>[\d.]+)", lines[idx])
        state = State.FIND_CONFIG_OR_MODEL
        if match:
            avg = float(match.group("avg"))
            key = (model, batch, onednn)
            assert None not in key
            db[key] = avg
        else:
            # Some models such as ssd-resnet34 can't run on CPU with vanilla TF and
            # won't have results. This line contains either a config or model name.
            continue
    else:
        raise RuntimeError("Reached the unreachable code.")
    idx = idx + 1
