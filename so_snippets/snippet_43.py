# Extracted from https://stackoverflow.com/questions/4906977/how-can-i-access-environment-variables-in-python
python -c "import os;L=[f'{k}={v}' for k,v in os.environ.items()]; print('\n'.join(L))"

