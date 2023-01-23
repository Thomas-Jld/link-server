.PHONE: all run

all:
	run

run:
	python3.9 -m gunicorn --worker-class eventlet -w 1 link:app --reload
