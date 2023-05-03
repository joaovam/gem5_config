import m5
from m5.objects import *

from Cache.l1_cache import *
from Cache.l2_cache import L2Cache
from Cache.l3_cache import L3Cache
import argparse

parser = argparse.ArgumentParser(description='An O3 system with 3-level cache.')

parser.add_argument("binary", default="", nargs="?", type=str,
                    help="Path to the binary to execute.")
parser.add_argument("--arguments", help="Arguments to be passed to binary program")
parser.add_argument("--cores", help="The number of cores in the simulated machine",type=int)
parser.add_argument("--l1i_size",
                    help=f"L1 instruction cache size. Default: 32kB.")
parser.add_argument("--l1d_size",
                    help="L1 data cache size. Default: Default: 32kB.")
parser.add_argument("--l2_size",
                    help="L2 cache size. Default: 256kB.")
parser.add_argument("--l3_size",
                    help="L3 cache size. Default: 512kB.")

parser.add_argument("--clock",default="3GHz", help="the core of the processor, example: 3GHz")

options = parser.parse_args()

system = System()

system.clk_domain = SrcClockDomain()
system.clk_domain.clock = options.clock
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('32GB')]

#creating CPU
system.cpu = [O3CPU(cpu_id=i) for i in range(options.cores)]
system.membus = SystemXBar()

#Connecting Cache
for i in range(options.cores):
    system.cpu[i].icache = L1ICache(options)
    system.cpu[i].dcache = L1DCache(options)

    system.cpu[i].icache.connectCPU(system.cpu[i])
    system.cpu[i].dcache.connectCPU(system.cpu[i])

system.l2bus = L2XBar()
system.l3bus = L2XBar()

for i in range(options.cores):
    system.cpu[i].icache.connectBus(system.l2bus)
    system.cpu[i].dcache.connectBus(system.l2bus)


system.l2cache = L2Cache(options)
system.l3cache = L3Cache(options)

system.l2cache.connectCPUSideBus(system.l2bus)
system.l3cache.connectCPUSideBus(system.l3bus)

system.l2cache.connectMemSideBus(system.l3bus)
system.membus = SystemXBar()

system.l3cache.connectMemSideBus(system.membus)

for i in range(options.cores):
    system.cpu[i].createInterruptController()
    system.cpu[i].interrupts[0].pio = system.membus.mem_side_ports
    system.cpu[i].interrupts[0].int_requestor = system.membus.cpu_side_ports
    system.cpu[i].interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

binary = '/gem5/gem5/tests/test-progs/hello/bin/x86/linux/hello'

# for gem5 V21 and beyond
system.workload = SEWorkload.init_compatible(binary)

process = Process()
process.cmd = [options.binary]
#FIX - create threads with multiple CPUs
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()

print('Exiting @ tick {} because {}'
      .format(m5.curTick(), exit_event.getCause()))

