# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/csv_dataset_benchmark.py
self._set_up(self.STR_VAL)
for i in range(len(self._filenames)):
    num_cols = self._num_cols[i]
    kwargs = {'record_defaults': [['']] * num_cols}
    dataset = core_readers.TextLineDataset(self._filenames[i]).repeat()
    dataset = dataset.map(lambda l: parsing_ops.decode_csv(l, **kwargs))  # pylint: disable=cell-var-from-loop
    self._run_benchmark(
        dataset=dataset,
        num_cols=num_cols,
        prefix='csv_strings_map_decode_csv',
        benchmark_id=2)
self._tear_down()
