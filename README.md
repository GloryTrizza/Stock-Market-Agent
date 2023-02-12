# Stock Market AI Agent
## Introduction
This code provides a simulation of an AI agent that buys stocks in a stock market. The AI agent interacts with an environment that provides information about stock prices and the number of stocks in hand. The AI agent decides how many stocks to buy based on the current price and the number of stocks in hand.

## Dependencies
The code requires the random module.

## Classes
The code contains two classes:
Environment: The environment class keeps track of the stock prices and the number of stocks in hand. It provides information to the AI agent through the initial_percepts and do functions.
Agent: The AI agent class takes decisions on how many stocks to buy based on the information provided by the environment. It updates its parameters with each interaction with the environment.

## Functions
pick_from_dist: A helper function that randomly selects an item based on its probability of occurrence.

## Usage
To use the code, create an instance of the Environment class, and then create an instance of the Agent class with the Environment instance as its input. Call the go function on the Agent instance with the number of time steps to simulate.
