import logging


class City:

    def __init__(self, p_name: str, p_infection: int=0, p_neighbours: list=list()):
        self._infection = p_infection
        self._neighbours = list(p_neighbours)
        self._name = p_name
        self._immunity = False

        self.logger = logging.getLogger('pandemic.model.city')

    @property
    def infection(self):
        return self._infection

    @property
    def name(self):
        return self._name

    @property
    def neighbours(self):
        return self._neighbours

    @property
    def is_immunized(self):
        return self._immunity

    @is_immunized.setter
    def is_immunized(self, value):
        self._immunity = value

    def add_neighbour(self, p_neighbour: 'City'):
        """
        Add a neighbour to the city network
        :param p_neighbour: A city to add to the network
        """
        if p_neighbour is not None:
            self._neighbours.append(p_neighbour)
        else:
            self.logger.warning('City null, not append to the network')

    def is_infected(self) -> bool:
        """
        Check if the city is infected
        :return: True if the city is infected, False else
        """
        return self._infection > 0

    def is_propagation_source(self) -> bool:
        """
        Check if the city must propagate the infection or not
        :return: True if the city must propagate, False else
        """
        return self._infection == 3

    def infect(self) -> int:
        """
        Infect the city if not is_immunized
        :return: The infection level of the city
        """
        if not self.is_immunized and not self.is_propagation_source():
            self._infection += 1
            if self.is_propagation_source():
                self.propagate()

            self._immunity = True

        return self._infection

    def propagate(self):
        """
        Propagate the infection to the neighbour
        """
        for city in self._neighbours:
            city.infect()
