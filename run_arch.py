import os
import re
import subprocess
import argparse

gem5_location = "/home/joao.vieira/gem5/"
opt_location = gem5_location + "gem5/build/X86/gem5.opt"
script = gem5_location  +"gem5_config/arch_config.py"
programs_location = "/home/joao.vieira/CAPBenchmarks/x86/bin/"
test = gem5_location + "gem5/tests/test-progs/hello/bin/x86/linux/hello"

kernel='linux-full-system/vmlinux-5.4.49'
disk_image='linux-full-system/disk-image/x86root-parsec.img'

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--arch1", type=bool, help="Run architecture number 1")
    parser.add_argument("--arch2", type=bool, help="Run architecture number 2")
    parser.add_argument("--arch3", type=bool, help="Run architecture number 3")
    parser.add_argument("--program", help="program to be run")
    parser.add_argument("--classr", type=str, default="all", help="The class to be run, defaults to all")
    options = parser.parse_args()
    command = ""

    output_file = "out_" + options.program + "_" + options.classr + " "
    if options.arch1:

        #os.mkdir("/home/joao.vieira/gem5/out")
        command = opt_location + f" --listener-mode=on \
        --outdir=/home/joao.vieira/gem5/gem5_config/{output_file}"\
                  + script + f' --clock "3.2GHz"\
                                      --cores 8\
                                      --l1i_size 32kB\
                                      --l1d_size 32kB\
                                      --l2_size 512kB\
                                      --l3_size 16MB '

    # subprocess.Popen(command.split())
    elif options.arch2:
        command = opt_location + " " + script + f' --clock 3.2GHz\
                                      --cores 8\
                                      --l1i_size 32kB\
                                      --l1d_size 32kB\
                                      --l2_size 512kB\
                                      --l3_size 16MB \
                                        '

    elif options.arch3:
        command = opt_location + " " + script + f' --clock 3.2GHz\
                                              --cores 8\
                                              --l1i_size 32kB\
                                              --l1d_size 32kB\
                                              --l2_size 512kB\
                                              --l3_size 16MB \
                                              '

    command+= f'--kernel={kernel} --disk_image={disk_image}'
    print("Running Command:")
    print(' '.join(command.split()))
    p = subprocess.Popen(command.split())
    p.wait()






if __name__ == "__main__":
    main()
