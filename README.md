# Pandemic

## Rules
The game involves interconnected cities.
Each city is infected with a given level : from 0 (default, not infected) to 3 (infection source)

At each turn of the game :
- an infection appears in a city : the city's infection is incremented by one unit
- if the level of an infection reaches 3, the city becomes a source of infection and propagates it to all its neighbours
- the propagation mecanism is achieve only one time for a given city during the game
- a propagation can make new propagations occur but the infection of a given city can't be increased more than 1 time in the same game turn

The game ends when X cities have became infection source.

## Input data

### Cities
The city network as an utf-8 file, where each line contains a couple of connected cities

```
london , paris
london, madrid
madrid, alger
```

### Infections
Infected cities are given as a file, where each line match with a game turn and contains the name of the infected city.

```
paris
london
madrid
```

## Output
The program runs all the given game turns and displays, at each step, the infection of each city. It stops when X cities have became an infection source.

## Requirements
You will need python 3.6+ to make the code run

## Install and run
Use the requirements.txt to install the required packages

```
pip install -r requirements.txt
```

You can then run the code with the single command :

```
python pandemic.py
```

Note that adding '--help' to the command line will display all available options.

## Tests
You can run unit tests with this command :

```
pytest tests/
```
