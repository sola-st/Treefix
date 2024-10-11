# Extracted from https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from
pip install --download <DIR> -r requirements.txt

pip install --no-index --find-links=[file://]<DIR> -r requirements.txt

