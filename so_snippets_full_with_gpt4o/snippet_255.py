# Extracted from https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
python -m unittest discover -s ../test

setlocal & cd src & python -m unittest discover -s ../test

