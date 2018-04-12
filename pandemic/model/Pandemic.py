import logging
from pandemic.model.City import City


class Pandemic:

    def __init__(self, p_cities: dict=dict(), p_turns: list=list(), p_max_infection_sources: int=1):
        self._cities = dict(p_cities)
        self._turns = list(p_turns)
        self._current_turn = 1
        self._max_infection_source = p_max_infection_sources
        self.logger = logging.getLogger('pandemic.model.pandemic')

    def add_city(self, p_city: str) -> City:
        """
        Add a city to the game network. Create it if it doesn't exist.
        :param p_city: A city name
        :return: The city object associated to p_city
        """
        if self._cities.get(p_city, None) is None:
            self._cities[p_city] = City(p_name=p_city)

        return self._cities[p_city]

    def add_cities(self, p_city_1, p_city_2):
        """
        Add a couple of city to the game network. Handle their connexion between each other.
        :param p_city_1: A city name
        :param p_city_2: A city name connected to p_city_2
        """
        city_1 = self.add_city(p_city_1)
        city_2 = self.add_city(p_city_2)

        city_1.add_neighbour(city_2)
        city_2.add_neighbour(city_1)

        pass

    def game_over(self) -> bool:
        """
        Check if the game is over or not
        :return: True if the game is over. False else.
        """
        return len(self.get_source_cities()) > self._max_infection_source

    def play_the_game(self):
        """
        Make the game alive
        """
        for city in self._turns:
            self.logger.info(f"Game turn number {self._current_turn}")
            self.logger.info(f"Infection of {city}")
            self.unimmunize_network()
            self._cities[city].infect()
            self._current_turn += 1

            self.logger.info(f"Infected cities : {[(city.name, city.infection) for city in self.get_infected_cities()]}")
            self.logger.info(f"Infection source cities : {[city.name for city in self.get_source_cities()]}")

            if self.game_over():
                self.logger.info("Game over ! ")
                break

    def get_infected_cities(self) -> [City]:
        """
        Get the infected cities of the network
        :return: A list of all infected cities
        """
        return [city for city_name, city in self._cities.items() if city.is_infected()]

    def get_source_cities(self) -> [City]:
        """
        Get the infection source cities of the network
        :return: A list of all infection source cities
        """
        return [city for city_name, city in self._cities.items() if city.is_propagation_source()]

    def unimmunize_network(self):
        """
        Make all cities unimmunized
        """
        for city_name, city in self._cities.items():
            city.is_immunized = False
