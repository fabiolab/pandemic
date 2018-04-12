"""Joue à pandemic

Usage:
    pandemic.py [--max_infection_sources=<max_infection_sources>]

Options:
    --help      Displays this help
    --version   Displays the version numbre
    --max_infection_sources=<max_infection_sources>   Sets the max number of infection source cities
"""

from docopt import docopt
from pandemic.dao.PandemicDao import PandemicDao
import logging


def get_logger() -> logging.Logger:
    logger = logging.getLogger('pandemic')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

if __name__ == '__main__':
    arguments = docopt(__doc__)

    pandemic_logger = get_logger()

    if not arguments['--max_infection_sources']:
        arguments['--max_infection_sources'] = 1

    pandemicdao = PandemicDao()
    pandemic = pandemicdao.load_pandemic(p_nb_max_source_cities=arguments['--max_infection_sources'])
    pandemic.play_the_game()
