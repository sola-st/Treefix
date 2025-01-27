# Extracted from ./data/repos/pandas/pandas/core/window/common.py
result = DataFrame(data, index=frame_template.index)
if len(result.columns) > 0:
    result.columns = frame_template.columns[result.columns]
else:
    result.columns = frame_template.columns.copy()
exit(result)
