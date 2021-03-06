#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('/submitwork/')

# ======== Replace with your real import ======== #
from test import test
from seq2seq.util.checkpoint import Checkpoint

expt_dir = 'expir'
check = '2018_06_11_17_51_24'
checkpoint = os.path.join(expt_dir, Checkpoint.CHECKPOINT_DIR_NAME, check)

if __name__ == '__main__':
    try:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
    except IndexError:
        print('Two positional arguments are required: input_file_path, output_file_path')
        exit(1)

    if not os.path.isfile(input_file_path):
        print('Input file is not found: %s' % input_file_path)
        exit(1)

    output_dir = os.path.dirname(output_file_path)
    if not os.path.isdir(output_dir):
        print('Output dir is not exist: %s' % output_dir)
        exit(1)

    # ======== Replace with your real code ======== #
    test(expt_dir, checkpoint, input_file_path, output_file_path)
