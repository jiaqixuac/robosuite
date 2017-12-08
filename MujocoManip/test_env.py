from MujocoManip import SawyerStackEnv, SawyerPushEnv, SawyerGraspEnv, SawyerReachEnvEEVel, SawyerReachEnv
import numpy as np

if __name__ == '__main__':

    ### TODO: for some reason, when you just open a new terminal, import the env, do reset, then render, ###
    ###       it doesn't render the correct configuration. ###
    ### TODO: define observation space, action space (you can look at Julian's code for this) ###

    # a test case: do completely random actions at each time step
    # env = SawyerStackEnv(gripper='TwoFingerGripper')
    # env = SawyerStackEnv(gripper='RobotiqGripper')
    # env = SawyerStackEnv(gripper='PR2Gripper')
    # env = SawyerPushEnv()
    # env = SawyerGraspEnv(gripper="RobotiqThreeFingerGripper")
    # env = SawyerGraspEnv(gripper="RobotiqThreeFingerGripper")
    env = SawyerReachEnv(end_effector_control=True, reward_objective_factor=500)
    obs = env._reset()
    dof = env.dof()
    print('action space', env.action_space)
    print('Obs: {}'.format(len(obs)))
    print('DOF: {}'.format(dof))
    while True:
        obs = env._reset()
        # action = np.random.randn(dof)
        action = obs[len(obs) - 3: len(obs)]
        # action[:7] = [0, -1.18, 0.00, 2.18, 0.00, 0.57, 3.3161]
        # action[7] = 1
        for i in range(2000):
            # print(obs[len(obs) - 6: len(obs) - 3])
            # print(obs[len(obs) - 9: len(obs) - 6])
            action = obs[len(obs) - 3: len(obs)]
            # action[:7] = [0, -1.18, 0.00, 2.18, 0.00, 0.57, 3.3161]
            # action[7] = 1
            obs, reward, done, info = env._step(action)
            print('obs: {}'.format(obs))
            print('reward: {}'.format(reward))
            env._render()
            if done:
                print('done: {}'.format(reward))
                break