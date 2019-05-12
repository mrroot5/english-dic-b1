#!/bin/bash
echo "Delete old enviorement_________"
rm -rf venv
echo -e "Done\n"
echo "Install requirements.apt_______"
if [ -s "requirements.apt" ]
then
   sudo apt-get install $(cat requirements.apt)
fi
echo -e "Done\n"
echo "Create environment_____________"
virtualenv -p python3 venv
echo -e "Done\n"
echo "Start environment______________"
source venv/bin/activate
echo -e "Done\n"
echo "Install requirements-dev.txt_______"
if [ -s "requirements-dev.txt" ]
then
   pip install -r requirements-dev.txt
fi
echo -e "Done\n"
echo "[Finish]"
