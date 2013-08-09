from procgraph.core.registrar_other import simple_block

@simple_block
def aer_num(x):
    """ Number of events in the packet """
    return x.size
