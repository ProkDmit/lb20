#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number", type=int)

    args = parser.parse_args()
    print(args.square**2)