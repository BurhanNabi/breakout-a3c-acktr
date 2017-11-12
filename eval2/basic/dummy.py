import gym
env = gym.make('BreakoutNoFrameskip-v4')
for i_episode in range(20):
    observation = env.reset()
    print(env.action_space)
    #> Discrete(2)
    print(env.observation_space)
    exit(0)

    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

