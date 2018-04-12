from pandemic.model.Pandemic import Pandemic
import logging
import os


class PandemicDao:

    CITIES_PATHFILE = 'data/Cities.txt'
    TURNS_PATHFILE = 'data/Turns.txt'

    def __init__(self, p_turns_pathfile: str=None, p_cities_pathfile: str=None):
        if p_turns_pathfile is None:
            p_turns_pathfile = PandemicDao.TURNS_PATHFILE
        if p_cities_pathfile is None:
            p_cities_pathfile = PandemicDao.CITIES_PATHFILE

        script_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self._turns_pathfile = os.path.join(script_dir, p_turns_pathfile)
        self._cities_pathfile = os.path.join(script_dir, p_cities_pathfile)

        self.logger = logging.getLogger('pandemic.dao.pandemicdao')

    def load_pandemic(self, p_nb_max_source_cities: int) -> Pandemic:
        """
        Create a pandemic object from data files
        :return: An instantiated pandemic object
        """
        pandemic = Pandemic(p_max_infection_sources=p_nb_max_source_cities)

        self.load_turns(pandemic)
        self.load_cities(pandemic)

        return pandemic

    def load_turns(self, p_pandemic: Pandemic):
        """
        Load game turns from a data file
        :param p_pandemic: A pandemic object
        """
        with open(self._turns_pathfile) as file:
            try:
                p_pandemic._turns = file.read().splitlines()
            except IOError:
                self.logger.error(f"Can't read file {self._turns_pathfile}")

    def load_cities(self, p_pandemic: Pandemic):
        """
        Load cities and connexions from a data file
        :param p_pandemic: A pandemic object
        """
        with open(self._cities_pathfile) as file:
            try:
                connexions = file.read().splitlines()
                for con in connexions:
                    neighbours = con.split(',')
                    p_pandemic.add_cities(neighbours[0].strip(), neighbours[1].strip())
            except IOError:
                self.logger.error(f"Can't read file {self._cities_pathfile}")
            except KeyError:
                self.logger.error(f"Bad file format for {self._cities_pathfile}")
