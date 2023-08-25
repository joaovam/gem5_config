import os
import re
import subprocess
import argparse
from threading import Thread


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--program", help="program to be run")
    parser.add_argument("-c", type=str, default="standard", help="The class to be run, defaults to standard")
    options = parser.parse_args()

    sizes = [2, 4, 8, 16, 24]

    for t in sizes:
        thread = Thread(target=run_classes, args=(options.program, options.c, t))
        thread.start()
        thread.join()



def run_classes(program, c, t):
    command = f"nohup perf stat -o ./results/real_results/{program}_{c}_{t} -B -e cache-references,cache-misses,cycles,instructions,branches,faults,migrations /home/joao.vieira/CAPBenchmarks/x86/bin/{program} --nthreads {t} --class {c} > {program}_{c}_{t}_real &"
    print("Running: ", command)
    os.system(command)

if __name__ == "__main__":
    main()
