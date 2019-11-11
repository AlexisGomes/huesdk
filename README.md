This is a python sdk to manipulate the Philips hue API

#installation

pip install huesdk


HUE Documentation : https://developers.meethue.com/develop/get-started-2/
HUE interface : https://{bridge ip address}/debug/clip.html

#### Get Started
Step 1: Find your hue bridge IP 
https://www.meethue.com/api/nupnp

Step 2 : use method `get_user` to create an authorized user

### Create python package

sudo python -m pip install --upgrade pip setuptools wheel

sudo python -m pip install tqdm

sudo python -m pip install --user --upgrade twine

### Build package
python setup.py bdist_wheel

python -m twine upload dist/*
