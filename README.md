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
python3 defopt_test.py -c config.json
```

TODO
- propagate `-h/--help`
- make sure it works with sub-commands
