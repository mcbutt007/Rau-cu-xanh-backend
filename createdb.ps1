python3 -m flask db init
python3 -m flask db migrate -m "init"
python3 -m flask db upgrade
python3 input.py
