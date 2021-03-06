# Wish Simulator
An application developed using Python that simulates the statistical distribution of obtaining a user inputted amount of characters for the game Genshin Impact.

# About
In the game Genshin Impact, you can "wish" for a character. Every time you wish, you have a chance of receiving a character. This chance is dependent on other factors, such as how long it has been since you received a character, what character you received before, character rarity, and more.

The statistics behind when you will obtain a character is not simple. It's analagous to drawing an Ace from a deck of cards, but the deck is stacked, and the way it's stacked changes with every draw.

Resources are limited in this game, and the opportunity to wish for a character is time-limited. Therefore, understanding the chance that given your current resources, you are successful in obtaining a character is an important factor to whether or not you should try.

While talking with a friend, I realized there wasn't an application that did what I wanted, so I made this simulator. Give the user's parameters, it will simulate a distribution, print out averages, print out amount of wishes needed at various percentage breakpoints, and display a line graph and histogram of the simulated distribution. The user can then save these graphs if they so please.

# Example Graphs

![Line Graph](https://imgur.com/EmXDpNb.png)

![Histogram](https://imgur.com/0l8ijHf.png)

# How to Run

Download the wish-simulator folder and run wish-simulator.exe located inside it.

Alternatively, you can download the wish-simulator.py and can run the main function in an IDE of your choice.

# To Do

1. Transfer the application to the web using React and Material-UI. Eventually I want this application to be more accessible. Once this happens, I will deploy the application onto my GitHub Pages.
