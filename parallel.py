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



def main(args):
    with open(args.csvfilename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            run(args.script, row)
            print(f"Server {i+1} done.")
    
def p_main(args):
    processes = []
    # start a process running our script
    def run_parallel(script, row, i):
        with open(f"srv_{i+1}.log", "a") as log:
            
            print(f"Starting script #{i+1} : {script} with environment : {row} ...")
            log.write(f"Log for target #{i+1} : {script} with environment : {row} :\n")

            # Forward env with and row's values
            this_env = os.environ.copy()
            for key, value in row.items():
                this_env[key] = value
            # Add our process to the process list
            processes.append(
                subprocess.Popen(
                    ["/bin/sh", script],
                    env=this_env,
                    stdout=log,
                    stderr=log
                )
            )

    with open(args.csvfilename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            run_parallel(args.script, row, i)
    
    print("Waiting for processes to finish...")
    # Wait for every process to finish
    for i, process in enumerate(processes):
        print(f"Target #{i+1} : Done.")
        process.communicate() #this waits and ensures stdout/err is written in the logs
    print("All done ;)")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="run a script multiple times setting environment variables from a csv file from google sheets"
        )
    parser.add_argument(
        "-p",
        action="store_true",
        help="If this flag is provided, run the scripts in parallel - creating a log file named srv_n for each process"
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

    if args.p:
        p_main(args)
    else:
        main(args)

    