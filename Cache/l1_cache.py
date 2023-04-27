from m5.objects import Cache

class L1Cache(Cache):
    assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr  = 20

    def __init__(self, options):
        if not options or not options.L1Assoc:
            return

        self.assoc = options.L1Assoc

    def connectCPU(self, cpu):
        # need to define this in a base class!
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports


class L1ICache(L1Cache):
    size = '32kB'
    def __init__(self, options=None):
        super(L1ICache, self).__init__(options)
        if not options or not options.L1ICacheSize:
            return
        self.size = options.L1ICacheSize

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port


class L1DCache(L1Cache):
    size = '32kB'
    def __init__(self, options=None):
        super(L1DCache, self).__init__(options)
        if not options or not options.L1DCacheSize:
            return
        self.size = options.L1IDacheSize

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port


