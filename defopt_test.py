import typing as T
import json
import argparse

import wrapt
import defopt


@wrapt.patch_function_wrapper(argparse.ArgumentParser, "parse_args")
def parse_args(wrapped, instance, args, kwargs):
    print("pouet", flush=True)
    return wrapped(*args, **kwargs)


def main(*, params: T.Dict[str, T.Any]):
    print("params:", params, type(params))


if __name__ == "__main__":
    defopt.run(main, parsers={T.Dict[str, T.Any]: json.loads})
