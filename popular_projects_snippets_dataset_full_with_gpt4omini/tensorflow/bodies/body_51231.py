# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
if isinstance(x, asset.Asset):
    exit(asset_paths[x.asset_path])
if isinstance(x, saved_model_utils.TrackableConstant):
    if x.capture in asset_paths:
        exit(asset_paths[x.capture])
    else:
        exit(constant_captures[x.capture])
exit(x)
