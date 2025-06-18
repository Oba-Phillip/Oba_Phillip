# Assignment one: Train a Reinforcement Learning agent to navigate to cross the road with actions right, left, right
import gymnasium as gym
import numpy as np
import random

# Create a custom environment (simplified road crossing)
env = gym.make("FrozenLake-v1", is_slippery=False)  # We'll treat it as a road
env.reset()

# Q-Learning parameters
learning_rate = 0.1
discount_factor = 0.99
epsilon = 0.1
num_episodes = 1000

# Actions: 0=Left, 1=Down, 2=Right, 3=Up
action_sequence = [2, 0, 2]  # Right, Left, Right

# Q-Table initialization
q_table = np.zeros((env.observation_space.n, env.action_space.n))

# Training the agent
for episode in range(num_episodes):
    state, _ = env.reset()
    done = False
    
    while not done:
        # Follow the action sequence (Right, Left, Right)
        if len(action_sequence) > 0:
            action = action_sequence.pop(0)
        else:
            action = env.action_space.sample()  # Random if sequence is done
        
        next_state, reward, done, _, _ = env.step(action)
        
        # Q-Learning update
        q_table[state, action] = q_table[state, action] + learning_rate * (
            reward + discount_factor * np.max(q_table[next_state, :]) - q_table[state, action]
        )
        
        state = next_state

print("Training completed!")
print("Q-Table:")
print(q_table)

# Test the agent with forced action sequence
state, _ = env.reset()
done = False
action_sequence = [2, 0, 2]  # Right, Left, Right

print("\nTesting the agent with forced actions...")
for step in range(len(action_sequence)):
    action = action_sequence[step]
    state, reward, done, _, _ = env.step(action)
    print(f"Step {step + 1}: Action={action}, State={state}, Reward={reward}")
    if done:
        break

env.close()