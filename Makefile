setup:
	# You may want to do this
	virtualenv --python python3 ~/miniwiki_env
	# afterward then source
	source ~/miniwiki_env/bin/activate

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

all: install lint