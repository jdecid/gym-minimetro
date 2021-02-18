import gym
import numpy as np
from gym import spaces

from gym_minimetro.actions import DISCRETE_ACTIONS


class MinimetroEnv(gym.Env):
    """Minimetro game gym environment"""
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(DISCRETE_ACTIONS)
        self.observation_space = spaces.Box(low=0, high=255, shape=(64, 128, 3), dtype=np.uint8)

    def step(self, action):
        # Execute one time step within the environment
        pass

    def reset(self):
        # Reset the state of the environment to an initial state
        pass

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        pass
