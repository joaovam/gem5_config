from m5.objects import Cache

class L3Cache(Cache):
    assoc = 16
    size = '64MB'
    tag_latency = 20
    data_latency = 20
    response_latency = 1
    mshrs: int = 20,
    tgts_per_mshr: int = 12,


    def __init__(self, addr_ranges, size="64MB"):
        super(L3Cache, self).__init__()

        self.addr_ranges = addr_ranges
        self.size = size

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports