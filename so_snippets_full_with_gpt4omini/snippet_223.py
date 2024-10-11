# Extracted from https://stackoverflow.com/questions/20101834/pip-install-from-git-repo-branch
pip install https://github.com/user/repo.git@branch

pip install -U git+https://github.com/moskomule/anatome.git@dev

(original_anatome_env) brando~/ultimate-anatome ❯ pip install -U git+https://github.com/moskomule/anatome.git@dev
Collecting git+https://github.com/moskomule/anatome.git@dev
  Cloning https://github.com/moskomule/anatome.git (to revision dev) to /private/var/folders/x4/0xq0brj57xz3dbhbmblypbm00000gr/T/pip-req-build-62d_ghd2
  Running command git clone -q https://github.com/moskomule/anatome.git /private/var/folders/x4/0xq0brj57xz3dbhbmblypbm00000gr/T/pip-req-build-62d_ghd2
  Running command git checkout -b dev --track origin/dev
  Switched to a new branch 'dev'
  Branch 'dev' set up to track remote branch 'dev' from 'origin'.
  Resolved https://github.com/moskomule/anatome.git to commit 4b576e51cb1824a57ea04974e0f92b5a6143294d
Requirement already satisfied: torch>=1.10.0 in /Users/brando/anaconda3/envs/metalearning/envs/original_anatome_env/lib/python3.9/site-packages (from anatome==0.0.6) (1.10.0)
Requirement already satisfied: torchvision>=0.11.1 in /Users/brando/anaconda3/envs/metalearning/envs/original_anatome_env/lib/python3.9/site-packages (from anatome==0.0.6) (0.11.1)
Requirement already satisfied: typing-extensions in /Users/brando/anaconda3/envs/metalearning/envs/original_anatome_env/lib/python3.9/site-packages (from torch>=1.10.0->anatome==0.0.6) (3.10.0.2)
Requirement already satisfied: pillow!=8.3.0,>=5.3.0 in /Users/brando/anaconda3/envs/metalearning/envs/original_anatome_env/lib/python3.9/site-packages (from torchvision>=0.11.1->anatome==0.0.6) (8.4.0)
Requirement already satisfied: numpy in /Users/brando/anaconda3/envs/metalearning/envs/original_anatome_env/lib/python3.9/site-packages (from torchvision>=0.11.1->anatome==0.0.6) (1.21.4)
Building wheels for collected packages: anatome
  Building wheel for anatome (setup.py) ... done
  Created wheel for anatome: filename=anatome-0.0.6-py3-none-any.whl size=10167 sha256=63b12a36f33deb8313bfe7756be60bd08915b8ba36711be47e292b590df70f61
  Stored in directory: /private/var/folders/x4/0xq0brj57xz3dbhbmblypbm00000gr/T/pip-ephem-wheel-cache-rde_ngug/wheels/19/e4/be/01479e8cba62ae8cdcd501cd3bf49e199f2bb94732a6a1b006
Successfully built anatome
Installing collected packages: anatome
  Attempting uninstall: anatome
    Found existing installation: anatome 0.0.5
    Uninstalling anatome-0.0.5:
      Successfully uninstalled anatome-0.0.5
Successfully installed anatome-0.0.6

