from m5.objects import Cache

class L2Cache(Cache):
    assoc = 2
    size= '256kB'
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tagts_per_mshr = 20

    def __init__(self,options):
        size

    def connectCPU(self, cpu):
        # need to define this in a base class!
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports