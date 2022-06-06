import sys
import typing as T
import json
import argparse

import wrapt
import defopt


# adapted from https://gist.github.com/kgaughan/b659d6c173b5a2203dfb3ae225135cce
@wrapt.patch_function_wrapper(argparse.ArgumentParser, "parse_args")
def parse_args(wrapped, instance, args, kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--conf", type=argparse.FileType("r"), help="Configuration file"
    )
    args, remaining = parser.parse_known_args()

    if args.conf:
        try:
            defaults = json.load(args.conf)
        except ValueError:
            print("Error: Could not parse config file", file=sys.stderr)
            sys.exit(1)
        finally:
            args.conf.close()
        instance.set_defaults(**defaults)

    return wrapped(remaining)


def main(*, params: T.Optional[T.Dict[str, T.Any]] = None):
    print("params:", params, type(params))


if __name__ == "__main__":
    defopt.run(main, parsers={T.Dict[str, T.Any]: json.loads})
