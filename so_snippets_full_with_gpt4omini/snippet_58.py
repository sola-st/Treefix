# Extracted from https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv
; cd dtree 
Switching to virtual environment: Development tree utiles
;dtree(feature/task24|✓); cat .autoenv.zsh       
# Autoenv.
echo -n "Switching to virtual environment: "
printf "\e[38;5;93m%s\e[0m\n" "Development tree utiles"
workon dtree
# eof
dtree(feature/task24|✓); cat .autoenv_leave.zsh 
deactivate

