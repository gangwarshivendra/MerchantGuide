import fileinput
from CustomParser import CustomParser
from constant import romanArr
import logging
import argparse
import os

def _parse_args(clargs=None):
    """Parse the command line arguments.

    @return: The parse args object
    @raise IOError: Raises an IOError if the file cannot be found
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--file ', type=str, required=True, help='Provide a file with set of inputs',dest="file")
    args = parser.parse_args(clargs)

    logging.info("Parameters: {}".format(args))
    return args



def start_conversion(clargs=None):
    args = _parse_args(clargs=None)
    cust = CustomParser(romanArr)
    logging.info("Output")
    if args.file is not None:
        if not os.path.exists(args.file):
            raise IOError("Could not find iput file file {}".format(args.file))
        else:
            for Line in fileinput.input(args.file):
                try:
                    str_return = cust.str_resolve(Line.rstrip())
                    if str_return:
                        print(str_return)
                except:
                        print("I have no idea what you are talking about")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    #logger = logging.getLogger(__name__)
    start_conversion()
