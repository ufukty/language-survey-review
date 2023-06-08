clear:
	python clear-1st-step.py
	python clear-2nd-step.py
	
visualize:
	python visualize/raw/visualize.py

normalized:
	python visualize/normalized/normalize.py
	python visualize/normalized/visualize.py

all:
	clear
	visualize
	normalized