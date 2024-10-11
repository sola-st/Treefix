# Extracted from https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste
pip install lxml

soup = BeautifulSoup(html, "lxml")

