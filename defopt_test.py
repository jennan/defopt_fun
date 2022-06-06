import typing as T
import json

import defopt


def main(*, params: T.Dict[str, T.Any]):
    print("params:", params, type(params))


if __name__ == "__main__":
    defopt.run(main, parsers={T.Dict[str, T.Any]: json.loads})
