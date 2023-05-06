#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")

    args = parser.parse_args()
    print(args.echo)