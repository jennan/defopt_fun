import sys
import typing as T
import json
import argparse

import wrapt
import defopt


# adapted from https://gist.github.com/kgaughan/b659d6c173b5a2203dfb3ae225135cce
@wrapt.patch_function_wrapper(argparse.ArgumentParser, "parse_args")
def parse_args(wrapped, instance, args, kwargs):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-c", "--config", type=argparse.FileType("r"), help="Configuration file"
    )
    args, remaining = parser.parse_known_args()

    if args.config:
        try:
            defaults = json.load(args.config)
        except ValueError:
            print("Error: Could not parse config file", file=sys.stderr)
            sys.exit(1)
        finally:
            args.config.close()
        instance.set_defaults(**defaults)

    instance.add_argument(
        "-c", "--config", type=argparse.FileType("r"), help="Configuration file"
    )
    return wrapped(remaining)


def main(
    *,
    verbose: bool = False,
    maxiter: int = 100,
    params: T.Optional[T.Dict[str, T.Any]] = None,
):
    for varname, value in locals().items():
        print(f"{varname}: {value} ({type(value)})")


if __name__ == "__main__":
    defopt.run(main, parsers={T.Dict[str, T.Any]: json.loads})
