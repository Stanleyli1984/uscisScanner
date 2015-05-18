__author__ = 'Stanley Li'


import argparse
import re
from uscisscanner.util.CaseID import CaseID

def raw_case_id(string):
    m = re.match(r"(LIN|SRC)(\d{10})$", string.strip().upper())
    assert m, "We only support NSC and TSC as of now!!"
    return CaseID(m.group(1), m.group(2))


def raw_scan_length(string):
    try:
        length = long(string)
    except ValueError:
        assert 0, "length must be all digits!"
    assert 0 < length < 1000, "Please be gentle to USCIS. Do not scan too much numbers"
    return length


def run_parser():
    parser = argparse.ArgumentParser(description='USCIS status scanner')
    parser.add_argument('-s', '--startId', type=raw_case_id, help='the receipt numer to start scanning')
    parser.add_argument('-l', '--scanNumber', default=1, type=raw_scan_length, help='the number of scanning')
    parser.add_argument('-i', '--scanInterval', default=5, type=int, choices=xrange(2, 100),
                        help='the interval between scanning two numbers')
    parser.add_argument('-o', '--outputFile', default='output', help='output file name')
    # TODO: add type support later
    # parser.add_argument('-t', '--outputType', default='xlsx', choices=['xlsx', 'csv', 'txt'], help='output file type')
    return parser.parse_args()

