from m5.objects import Cache

class L3Cache(Cache):
    assoc = 16
    size = '64MB'
    tag_latency = 2
    data_latency = 2
    response_latency = 50
    mshrs = 4
    tgts_per_mshr = 20

    def __init__(self, size="64MB"):
        super(L3Cache, self).__init__()

        self.size = size

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports