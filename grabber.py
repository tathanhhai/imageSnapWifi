#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division
from datetime import datetime
import sys
from time import sleep, time

import argparse
import requests


def parse_args():
    parser = argparse.ArgumentParser(
        description='This script grabs images from AirBeam camera'
    )

    parser.add_argument('ip', help="IP address of AirBeam camera")
    parser.add_argument('--frames', '-f', help="Number of frames to grab",
                        type=int, default=30)
    parser.add_argument('--delay', '-d', help="Delay between subsequent requests",
                        type=float, default=0.25)

    return parser.parse_args()

def get_timestamp():
    return str(time()).replace('.', '')

def get_filename():
    now = datetime.now()
    return '{0:%Y%m%d_%H%M_%S}_{1:03.0f}.jpg'.format(now, now.microsecond / 1000)

def print_dot():
    print('.', sep='', end='')
    sys.stdout.flush()


if __name__ == '__main__':
    args = parse_args()

    for i in range(args.frames):
        resp = requests.get('http://%s/image.jpg?%s' % (args.ip, get_timestamp()))
        print_dot()

        with open(get_filename(), 'w') as f:
            f.write(resp.content)

        sleep(args.delay)
