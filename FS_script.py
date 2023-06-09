import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--output", type=str,
                    help="The output file")

parser.add_argument("--cores", type=str,
                    help="Number of cores")

parser.add_argument("--l1i_size",
                    help=f"L1 instruction cache size. Default: 32kB.")
parser.add_argument("--l1d_size",
                    help="L1 data cache size. Default: Default: 32kB.")
parser.add_argument("--l2_size",
                    help="L2 cache size. Default: 256kB.")
parser.add_argument("--l3_size",
                    help="L3 cache size. Default: 512kB.")
parser.add_argument("--cpu_clock",
                    help="CPU clock")
parser.add_argument("--script",
                    help="Script to be used [program][class][n threads]")

options = parser.parse_args()

command = f"""
nohup /home/joao.vieira/gem5/gem5/build/X86/gem5.opt --listener-mode=on \
 --outdir=/home/joao.vieira/gem5/gem5_config/results/{options.output}.out \
 /home/joao.vieira/gem5/gem5/configs/example/fs.py -n {options.cores} \
 --cpu-clock {options.cpu_clock} \
 --mem-size 2GB \
 --smt \
 --caches \
 --l2cache \
 --num-l2caches {options.cores} \
 --num-l3caches 1
 --l1d_size {options.l1d_size} \
 --l1i_size {options.l1i_size} \
 --l2_size {options.l2_size} \
 --l3_size {options.l3_size} \
 --disk-image=linux-full-system/disk-image/x86root-parsec.img \
 --cpu-type=DerivO3CPU \
 --kernel=linux-full-system/vmlinux-5.4.49 \
 --script scripts/{options.script} > {options.output}_nohup.log  &
"""

print("Run Command:")
print(' '.join(command.split()))
