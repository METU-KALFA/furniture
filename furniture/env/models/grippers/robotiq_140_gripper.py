"""
6-DoF gripper with its open/close variant
"""
import numpy as np

from . import Gripper
from ...mjcf_utils import xml_path_completion


class Robotiq140GripperBase(Gripper):
    """
    6-DoF Robotiq 2f-140 gripper.
    """

    def __init__(self):
        super().__init__(xml_path_completion("grippers/robotiq_140_gripper.xml"))

    @property
    def init_qpos(self):
        return np.zeros(6)

    @property
    def joints(self):
        return [
            "left_outer_knuckle_joint",
            "left_inner_finger_joint",
            "left_inner_knuckle_joint",
            "right_outer_knuckle_joint",
            "right_inner_finger_joint",
            "right_inner_knuckle_joint"
        ]

    @property
    def dof(self):
        return 6

    @property
    def contact_geoms(self):
        return [
            "left_outer_knuckle",
            "left_outer_finger",
            "left_inner_finger",
            "left_inner_knuckle",
            "right_outer_knuckle",
            "right_outer_finger",
            "right_inner_finger",
            "right_inner_knuckle",
        ]

    @property
    def visualization_sites(self):
        return ["grip_site", "grip_site_cylinder"]

    @property
    def left_finger_geoms(self):
        return [
            "left_outer_finger",
            ]

    @property
    def right_finger_geoms(self):
        return [
            "right_outer_finger",
            ]


class Robotiq140Gripper(Robotiq140GripperBase):
    """
    1-DoF variant of RobotiqGripperBase.
    """

    def format_action(self, action):
        """
        Args:
            action: 1 => open, -1 => closed
        """
        assert len(action) == 1
        movement = np.array([1.,-1.,1.,1.,-1.,1.])
        return -1 * movement * action

    @property
    def dof(self):
        return 1
