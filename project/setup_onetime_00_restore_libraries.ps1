
# This powershell script sets up up a virtualenv for python libraries in this project
# Run this once - when you first populate the project 
# reference:  https://packaging.python.org/guides/installing-using-pip-and-virtualenv/

#
# confirm at least we have python with pip
python --version
python -m pip --version

# add virtualenv if user doesn't have it
python -m pip install virtualenv
python -m virtualenv --version

# create an empty virtualenv
python -m virtualenv pymote_env --no-site-packages

# activate the (empty) virtualenv
.\pymote_env\Scripts\activate

# list what the blank environment has
pip list

# get the libraries specified in the requirements.txt file
pip install -r requirements.txt

