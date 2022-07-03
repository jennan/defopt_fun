import sys
import typing as T
import json
import argparse

import defopt


parse_known_args_orig = argparse.ArgumentParser.parse_known_args


# adapted from https://gist.github.com/kgaughan/b659d6c173b5a2203dfb3ae225135cce
def parse_known_args(self, args=None, namespace=None):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-c", "--config", type=argparse.FileType("r"), help="Configuration file"
    )
    args, remaining = parse_known_args_orig(parser, args)

    if args.config:
        try:
            defaults = json.load(args.config)
        except ValueError:
            print("Error: Could not parse config file", file=sys.stderr)
            sys.exit(1)
        finally:
            args.config.close()
        self.set_defaults(**defaults)

        for action in self._actions:
            if not isinstance(action, argparse._SubParsersAction):
                continue
            for subparser in action.choices.values():
                subparser.set_defaults(**defaults)

    self.add_argument(
        "-c", "--config", type=argparse.FileType("r"), help="Configuration file"
    )
    return parse_known_args_orig(self, remaining)


argparse.ArgumentParser.parse_known_args = parse_known_args


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
