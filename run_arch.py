import re
import subprocess
import argparse

gem5_location = "/home/joao.vieira/gem5/"
opt_location = gem5_location + "gem5/build/X86/gem5.opt"
script = gem5_location  +"gem5_config/arch_config.py"
programs_location = "/home/joao.vieira/CAPBenchmarks/x86/bin/"
test = gem5_location +"gem5/tests/test-progs/hello/bin/x86/linux/hello"

classes = ["Tiny", "Small"]
programs = ["fast", "fn", "gf", "is", "km", "lu", "nb", "rt", "tsp"]


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--arch1", type=bool, help="Run architecture number 1")
    parser.add_argument("--arch2", type=bool, help="Run architecture number 2")
    parser.add_argument("--arch3", type=bool, help="Run architecture number 3")
    parser.add_argument("--class_run", type=str, default="all", help="The class to be run, defaults to all")
    options = parser.parse_args()

    if options.arch1:
        if options.class_run == "all":
            for program in programs:
                for argument in classes:
                    command = gem5_location + " " + script + f' --clock "3.2GHz"\
                                                  --cores 8\
                                                  --binary {program}.intel\
                                                  --arguments "{argument}"\
                                                  --l1i_size 32kB\
                                                  --l1d_size 32kB\
                                                  --l2_size 512kB\
                                                  --l3_size 16MB'
                    print("Running Command:")
                    print(' '.join(command.split()))
                    # subprocess.Popen(command.split())
        elif options.class_run == "test":
            command = gem5_location + " " + script + f' --clock 3.2GHz\
                                          --cores 8\
                                          --arguments {options.class_run}\
                                          --l1i_size 32kB\
                                          --l1d_size 32kB\
                                          --l2_size 512kB\
                                          --l3_size 16MB \
                                          {test}'



            print("Running Command:")
            print(' '.join(command.split()))
            p = subprocess.Popen(command.split())
            p.wait()





if __name__ == "__main__":
    main()
