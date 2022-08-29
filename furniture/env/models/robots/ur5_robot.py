import numpy as np

from ...mjcf_utils import array_to_string, xml_path_completion
from .robot import Robot


class Ur5(Robot):
    ### This is copied from jaco_robot.py
    ### Task1 TODO Make changes for working with UR5 robot.
    ### There exists a ur5_robot.py in the Master branch.
    ### If there is no change between the old and the new version it can be used.
    """Jaco is a single-arm robot designed by Kinova."""

    def __init__(
        self,
        use_torque=False,
        xml_path="robots/ur5/robot.xml",
    ):
        if use_torque:
            xml_path = "robots/ur5/robot_torque.xml"
        super().__init__(xml_path_completion(xml_path))

        self.bottom_offset = np.array([0, 0, -0.913])

    def set_base_xpos(self, pos):
        """
        Places the robot on position @pos.
        """
        node = self.worldbody.find("./body[@name='base']")
        node.set("pos", array_to_string(pos - self.bottom_offset))

    def set_base_xquat(self, quat):
        """
        Places the robot on position @quat.
        """
        node = self.worldbody.find("./body[@name='base']")
        node.set("quat", array_to_string(quat))

    @property
    def dof(self):
        return 6

    @property
    def joints(self):
        return ["shoulder_pan_joint","shoulder_lift_joint","elbow_joint","wrist_1_joint","wrist_2_joint","wrist_3_joint"]

    @property
    def init_qpos(self):
        return np.array([0, -np.pi/4, np.pi/2, -3*np.pi/4, -np.pi/2,  np.pi/2])

    @property
    def contact_geoms(self):
        return ["base_geom","shoulder_geom","upperarm_geom","forearm_geom","wrist1_geom","wrist2_geom","wrist3_geom"]

