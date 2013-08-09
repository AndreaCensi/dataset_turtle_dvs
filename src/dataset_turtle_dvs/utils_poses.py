from geometry import SE2_from_SE3, angular_from_se2, linear_angular_from_se2
from procgraph import simple_block


@simple_block
def SE2_from_posecov(x):
    """ Returns element of SE2 from ROS timestamped covariance. """ 
    from ros_node_utils.conversions import pose_from_ROS_pose
    q = pose_from_ROS_pose(x.pose.pose)
    return SE2_from_SE3(q)

@simple_block
def SE2_from_odometry(x):
    """ Returns element of SE2 from ROS timestamped covariance. """
    from ros_node_utils.conversions import pose_from_ROS_pose
    q = pose_from_ROS_pose(x.pose.pose)
    return SE2_from_SE3(q)

@simple_block
def omega_from_se2(x):
    return angular_from_se2(x)

@simple_block
def vx_from_se2(x):
    v, _ = linear_angular_from_se2(x)
    return v[0]

@simple_block
def vy_from_se2(x):
    v, _ = linear_angular_from_se2(x)
    return v[1]

@simple_block
def angle_from_SE2(q):
    from geometry.poses import angle_from_SE2
    angle = angle_from_SE2(q)
    return angle

@simple_block
def x_from_SE2(q):
    from geometry.poses import translation_from_SE2
    return translation_from_SE2(q)[0]

@simple_block
def y_from_SE2(q):
    from geometry.poses import translation_from_SE2
    return translation_from_SE2(q)[1]
