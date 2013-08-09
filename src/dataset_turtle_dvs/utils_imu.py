from procgraph.core.registrar_other import simple_block

@simple_block
def angular_from_imu(x):
    return x.angular_velocity.z


