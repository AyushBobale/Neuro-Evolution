from gym.envs.registration import register

register(id='CustomEnvironment-v0',
        entry_point='custom_environment.envs:')