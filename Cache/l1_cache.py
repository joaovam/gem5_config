from m5.objects import Cache

class L1Cache(Cache):
    assoc = 8
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr  = 20

    def __init__(self):
        super(L1Cache, self).__init__()


    def connectCPU(self, cpu):
        # need to define this in a base class!
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports


class L1ICache(L1Cache):
    size = '32kB'
    is_read_only = True
    # Writeback clean lines as well
    writeback_clean = True

    def __init__(self, size='32kB'):
        super(L1ICache, self).__init__()
        self.size = size

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port


class L1DCache(L1Cache):
    size = '32kB'
    is_read_only = True
    # Writeback clean lines as well
    writeback_clean = True

    def __init__(self, size='32kB'):
        super(L1DCache, self).__init__()
        self.size = size

    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port


