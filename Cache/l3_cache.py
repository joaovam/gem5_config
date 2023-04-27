from m5.objects import Cache

class L3Cache(Cache):
    assoc = 2
    size = '512kB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def __init__(self, options=None):
        super(L3Cache, self).__init__()
        if not options or not options.l3_size:
            return
        self.size = options.l3_size

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports