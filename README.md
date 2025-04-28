# CPM_MUNAR
pkg update
pkg upgrade -y
pkg install git
pkg install python -y
git clone https://github.com/MUNAR09/MNR_TOOL.git
cd MNR_TOOL
git pull
pip install -r requirements.txt
python main.py
