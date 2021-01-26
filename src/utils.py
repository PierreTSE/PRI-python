from pathlib import Path

from definitions import ROOT_DIR


def path_from_root(path):
    return ROOT_DIR / Path(path)
