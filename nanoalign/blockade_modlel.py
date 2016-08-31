#(c) 2015-2016 by Authors
#This file is a part of Nano-Align program.
#Released under the BSD license (see LICENSE file)

"""
Abstract blockade model
"""

class ModelDump(object):
    def __init__(self, name, predictor):
        self.name = name
        self.predictor = predictor


class BlockadeModel(object):
    def __init__(self):
        self.name = None
        self.predictor = None
        self.window = 4

        self.volumes = {"I": 1688, "F": 2034, "V": 1417, "L": 1679,
                        "W": 2376, "M": 1708, "A": 915, "G": 664,
                        "C": 1056, "Y": 2036, "P": 1293, "T": 1221,
                        "S": 991, "H": 1673, "E": 1551, "N": 1352,
                        "Q": 1611, "D": 1245, "K": 1713, "R": 2021,
                        "X": 1500, "U": 1056, "Z": 1580, "B": 1300,
                        "-": 0}

        self.hydro =   {"I": 450, "F": 280, "V": 420, "L": 380,
                        "W": -90, "M": 190, "A": 180, "G": -40,
                        "C": 250, "Y": -130, "P": -160, "T": -70,
                        "S": -80, "H": -320, "E": -350, "N": -350,
                        "Q": -350, "D": -350, "K": -390, "R": -450,
                        "X": 0, "U": 250, "Z": -350, "B": -350,
                        "-": 0}

    def train(self, peptides, signals):
        pass

    def peptide_signal(self, peptide):
        pass

    def load_from_dump(self, dump):
        if self.name == dump.name:
            self.predictor = dump.predictor
            return True
        return False

    def get_dump(self):
        assert self.predictor is not None
        return ModelDump(self.name, self.predictor)