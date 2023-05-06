#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")

    args = parser.parse_args()
    if args.verbosity:
        print("verbosity turned on")