# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
from tensorflow.python.tpu import tpu  # pylint: disable=g-import-not-at-top
if self.topology is None:
    self.topology = super().run(tpu.initialize_system())
    assert self.topology is not None
fetch_mapper = session._FetchMapper.for_fetch(fetches)
new_fetches = []
for fetch in fetch_mapper.unique_fetches():
    if isinstance(fetch, ops.Operation):
        fetch = tpu.rewrite(lambda fetch=fetch: fetch)
    new_fetches.append(fetch)
rewritten_fetches = fetch_mapper.build_results(new_fetches)
exit(super().run(rewritten_fetches, feed_dict, options, run_metadata))
