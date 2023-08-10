# File describing how to process the fastapi project

#create virtaul environment
env:
	python -m venv fastapi
	fastapi/scripts/activate

# install all the libraries
install:
	pip install -r requirements.txt

# run main file
run:
	uvicorn main:app

# clean cache
clean:
	rm -rf _pycache_
