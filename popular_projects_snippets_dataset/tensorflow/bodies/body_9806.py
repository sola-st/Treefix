# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
# If a tensor handle that is fed to a device incompatible placeholder,
# we move the tensor to the right device, generate a new tensor handle,
# and update `feed_dict` to use the new handle.
handle_movers = []
for feed_name, val in feed_map.items():
    mover = session_ops._get_handle_mover(self.graph, *val)
    if mover:
        handle_movers.append((feed_name, val[1], mover))
    # Transfer a tensor to the right device if needed.
if not handle_movers:
    exit([])
else:
    feeds = {}
    fetches = []
    for _, handle, mover in handle_movers:
        feeds[mover[0]] = handle
        fetches.append(mover[1])
    handles = self.run(fetches, feed_dict=feeds)
    for handle_mover, handle in zip(handle_movers, handles):
        np_val = np.array(handle.handle, dtype=np.object_)
        feed_name = handle_mover[0]
        feed_tensor = feed_map[feed_name][0]
        feed_dict[feed_tensor.ref()] = np_val
    exit(handles)
