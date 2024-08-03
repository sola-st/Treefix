# Installation Guide

Create and enter a virtual environment:

```
virtualenv -p /usr/bin/python3.8 treefix_env
source treefix_env/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

Locally install the package in development/editable mode:

```
pip install -e ./
```

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
