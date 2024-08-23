# Usage Guide

As a simple example, consider that the following code is in `./files/file.py`. 

```python
if (not has_min_size(all_data)):
    raise RuntimeError("not enough data")

train_len = round(0.8 * len(all_data))

logger.info(f"Extracting training data with {config_str}")

train_data = all_data[0:train_len]
```
Then, to predict the missing variables in the code, run:

```
python -m l3.Run --files ./files/file.py --openai_api_key $OPENAI_API_KEY
```

The metrics, such as *coverage_percentage* and *minimal_predictions_set*, calculated for each step of Treefix will be available at `./metrics/../../raw/metrics__file.csv`.

The predictions made by Treefix are available in the same folder of the original code. In this example, `./files/`. 
