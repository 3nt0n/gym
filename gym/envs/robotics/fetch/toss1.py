import os
from gym import utils
from gym.envs.robotics import fetch_tossball_env1


# Ensure we get the path separator correct on windows
MODEL_XML_PATH = os.path.join('fetch', 'toss1.xml')


class FetchTossEnv1(fetch_tossball_env1.FetchTossballEnv1, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
            'object0:joint': [1.25, 0.53, 0.4, 1., 0., 0., 0.],
        }
        fetch_tossball_env1.FetchTossballEnv1.__init__(
            self, MODEL_XML_PATH, has_object=True, block_gripper=False, n_substeps=20,
            gripper_extra_height=0.2, target_in_the_air=True, target_offset=0.0,
            obj_range=0.15, target_range=0, distance_threshold=0.2,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)

#changed target range to 0, changed treshold to 0.2 (almost the whole box)
