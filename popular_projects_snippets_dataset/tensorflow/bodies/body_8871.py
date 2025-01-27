# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
with coord.stop_on_exception():
    has_been_put_back = False
    while True:
        closure = closure_queue.get(timeout=30)
        if closure is None:
            break
        if not has_been_put_back:
            has_been_put_back = True
            closure_queue.put_back(closure)
            continue
        closure._function()
        closure_queue.mark_finished()
