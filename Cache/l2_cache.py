from m5.objects import Cache

class L2Cache(Cache):
    assoc = 8
    size = '2MB'
    tag_latency = 10
    data_latency = 10
    response_latency = 1
    mshrs: int = 20
    tgts_per_mshr: int = 12

    def __init__(self, size="2MB"):
        super(L2Cache, self).__init__()

        self.size = size

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports