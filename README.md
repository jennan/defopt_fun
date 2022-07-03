# Defopt fun

This repository contains some random experiments around [defopt](https://github.com/anntzer/defopt).

To use the code, first create a virtual environment and install `defopt`:

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Then run the script:

```
python3 defopt_test.py -h
python3 defopt_test.py -p '{"a": 3, "b": [1, 2, 3]}'
python3 defopt_test.py -c config.json -m 10
```

or test the version with multiple commands

```
python3 defopt_test2.py -h
python3 defopt_test2.py main -h
python3 defopt_test2.py main -p '{"a": 3, "b": [1, 2, 3]}'
python3 defopt_test2.py main -c config.json -m 10
python3 defopt_test2.py -c config.json main -m 10
```

TODO
- allow multiple configuration files