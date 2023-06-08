clear:
	python clear-1st-step.py
	python clear-2nd-step.py
	
visualize/raw:
	python visualize/raw/visualize.py


visualize/normalized:
	python visualize/normalized/normalize.py
	python visualize/normalized/visualize-want.py
	python visualize/normalized/visualize-have.py

all:
	clear
	visualize/raw
	visualize/normalized