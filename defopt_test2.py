import json
import typing as T

import defopt

from defopt_test import main


def main2(answer: int = 42):
    pass


if __name__ == "__main__":
    defopt.run([main, main2], parsers={T.Dict[str, T.Any]: json.loads})
