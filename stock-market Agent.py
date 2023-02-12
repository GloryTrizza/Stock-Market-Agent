import random


class Environment():
    prices = [234, 234, 234, 234, 255, 255, 275, 275, 211, 211, 211,
              234, 234, 234, 234, 199, 199, 275, 275, 234, 234, 234, 234, 255,
              255, 260, 260, 265, 265, 265, 265, 270, 270, 255, 255, 260, 260,
              265, 265, 150, 150, 265, 265, 270, 270, 255, 255, 260, 260, 265,
              265, 265, 265, 270, 270, 211, 211, 255, 255, 260, 260, 265, 265,
              260, 265, 270, 270, 205, 255, 255, 260, 260, 265, 265, 265, 265,
              270, 270]
    max_price_addon = 20  # maximum of random value added to get price

    def __init__(self):
        """constructor-initializes paper buying agent"""
        self.time = 0
        self.stock = 20
        self.stock_history = []  # memory of the stock history
        self.price_history = []  # memory of the price history

    """DEFINE INITIAL STATE-PRICE & RANDOM STOCK"""
# decide when to buy!!!
    def initial_percepts(self):  # define initial state (price & stock) and keep log (history)
        """return initial percepts-price and stock"""
        self.stock_history.append(self.stock)
        price = self.prices[0] + random.randrange(self.max_price_addon)
        self.price_history.append(price)
        print("initial stock and price", self.stock, price)
        return {'price': price,
                'instock': self.stock}

    """UPDATE STATE-AFTER BUYING AND USING"""

    def do(self, action):  # change state (price & stock) by using and keep log (history)
        """does action (buy) and returns percepts (price and instock)"""
        used = pick_from_dist({6: 0.1, 5: 0.1, 4: 0.2, 3: 0.3, 2: 0.2, 1: 0.1})
        """ item_prob_dist is an item:probability dictionary, """
        print("used", used)
        bought = action['buy']
        self.stock = self.stock + bought - used
        self.stock_history.append(self.stock)
        self.time += 1
        price = (self.prices[self.time % len(self.prices)]  # repeating pattern
                 + random.randrange(self.max_price_addon)  # plus randomness
                 + self.time // 2)  # plus inflation
        self.price_history.append(price)
        print('price', price, 'instock', self.stock)  # see new environment
        return {'price': price,
                'instock': self.stock}


"""USE-RANDOM NUMBER"""


def pick_from_dist(item_prob_dist):  # randomly select how many items to used based on probabilities
    """    returns No of item in proportion to its probability """
    ranreal = random.random()
    print("ranreal", ranreal)

    for (it, prob) in item_prob_dist.items():
        print("prob", prob, "it", it)
        if ranreal < prob:
            return it
        else:
            ranreal -= prob

# time to buy...Buy? or no?
class Agent():
    def __init__(self, env):
        self.env = env
        self.spent = 0
        percepts = env.initial_percepts()  # read initial state (price & stock)
        self.ave = self.last_price = percepts['price']
        self.instock = percepts['instock']
        print("agent params spent stock price", self.spent, self.instock, self.last_price)

    """DECIDE HOW MANY TO BUY - CALL DO FUNCTION  TO UPDATE & USE N TIMES"""

    def go(self, n):  # make decision on how many to buy
        """go for n time steps """
        for i in range(n):
            if self.last_price < 0.9 * self.ave and self.instock < 60: # if price below a certain value and price in stock is below 60
                tobuy = 48
            elif self.instock < 12:
                tobuy = 12
            else:
                tobuy = 0
            self.spent += tobuy * self.last_price
            percepts = env.do({'buy': tobuy})  # call env.do to use and update state
            self.last_price = percepts['price']
            self.ave = self.ave + (self.last_price - self.ave) * 0.05
            self.instock = percepts['instock']
            print("updated agent params", self.spent, self.instock, self.last_price)
        print("final agent params", self.spent, self.instock, self.last_price)

        """CREATE OBJECTS & RUN AGENT"""


env = Environment()  # create env object
ag = Agent(env)  # create agent object

import matplotlib.pyplot as plt


class Plot_prices(object):
    """Set up the plot for history of price and number in stock"""

    def __init__(self, ag, env):
        self.ag = ag
        self.env = env

        plt.xlabel("Time")
        plt.ylabel("Number in stock.                                              Price.")

    def plot_run(self):
        """plot history of price and instock"""
        num = len(env.stock_history)
        plt.plot(range(num), env.stock_history, label="In stock")
        plt.plot(range(num), env.price_history, label="Price")
        plt.legend(loc="upper left")
        plt.show()


pl = Plot_prices(ag, env)
ag.go(90)
pl.plot_run()

