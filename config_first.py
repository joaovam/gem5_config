import m5
from m5.objects import *

# Create a system with a single Xeon CPU
system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2.5GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

system.membus = SystemXBar()

system.physmem = SimpleMemory()
system.physmem.port = system.membus.cpu_side_ports

system.mem_ctrl = DDR3_1600_8x8()
system.mem_ctrl.port = system.membus.master

system.cpu = DerivO3CPU()
system.cpu.clock_domain = SrcClockDomain()
system.cpu.clock_domain.clock = '2.5GHz'
system.cpu.voltage_domain = VoltageDomain()

system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

system.cpu.icache.port = system.cpu.icache.cpu_side
system.cpu.dcache.port = system.cpu.dcache.cpu_side

system.cpu.icache.mem_side = system.membus.master
system.cpu.dcache.mem_side = system.membus.master

system.cpu.l2cache = L2Cache()
system.cpu.l2cache.port = system.membus.master

# Create a process and set its command-line arguments
process = Process()
process.cmd = ['hello', 'world']

# Assign the process to the CPU
system.cpu.workload = process
system.cpu.createThreads()

# Set up the simulation statistics
system.cpu.stats = Stats()
system.cpu.stats.addList(['ipc', 'cpi', 'idleCycles', 'brPredAccuracy'])

# Run the simulation
sim = Simulation()
sim.setSystem(system)
sim.setSimulationEndTime('10us')
sim.run()
