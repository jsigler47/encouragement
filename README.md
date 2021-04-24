# encouragement
A simple flask app that gives words of encouragement.

To run do the following:
> **Note**: These steps assume you have Python3 installed and the virtualenv module
> While the virtualenv isn't totally necessary for this, it keeps things tidy.
``` bash
git clone https://github.com/jsigler47/encouragement.git
cd encouragement
python3 -m virtualenv venv
source venv/bin/activate
pip3 install flask
export FLASK_APP=run.py
python3 -m flask run
```
