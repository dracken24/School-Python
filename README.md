install raylib on wsl2

# Installer python3-venv si ce n'est pas déjà fait
sudo apt install python3-venv

# Créer un environnement virtuel
python3 -m venv mon_env

# Activer l'environnement virtuel
source mon_env/bin/activate

# Maintenant vous pouvez installer raylib
pip install raylib


python main.py
