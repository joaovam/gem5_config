from m5.objects import Cache

class L2Cache(Cache):
    assoc = 2
    size = '2MB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr  = 20

    def __init__(self, size="2MB"):
        super(L2Cache, self).__init__()

        self.size = size

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports