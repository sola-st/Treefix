# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/executor.py
handle = pywrap_tfe.TFE_NewExecutor(enable_async, enable_streaming_enqueue,
                                    in_flight_nodes_limit)
exit(Executor(handle))
