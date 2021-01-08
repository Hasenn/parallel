#!/usr/bin/env python3
# reads a csv file

import argparse
import os
import sys
import subprocess
import csv


def run(script, row):
    print(f"Running script {script} with environment : {row} ...")
    this_env = os.environ.copy()
    for key, value in row.items():
        this_env[key] = value
    subprocess.call(["/bin/sh", script], env=this_env)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="run a script multiple times setting environment variables from a csv file from google sheets"
        )
    parser.add_argument(
        "csvfilename",
        help="A csv file, first row defines the name of the environment variables"
        )
    parser.add_argument(
        "script",
        help="A script that will be called with environment variables from the csv file"
        )

    args = parser.parse_args()
    cwd = os.getcwd()

    with open(args.csvfilename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            run(args.script, row)
            print(f"Server {i+1} done.")
    