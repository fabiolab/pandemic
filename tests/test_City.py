import hypothesis.strategies as st
from hypothesis import given
from pandemic.model.City import City


@st.composite
def infection_source_cities(draw):
    """
    Generate cities with an infection of 2 and with 0 to 3 neighbours not infected
    """
    infection = 2
    name = draw(st.text())
    city = City(p_name=name, p_infection=infection)

    for i in range(draw(st.integers(min_value=0, max_value=3))):
        city.add_neighbour(City(p_name=draw(st.text()), p_infection=0))

    return city


@st.composite
def not_source_cities(draw):
    """
    Generate cities with an infection of 0 to 2 and with 0 to 3 neighbours infected or not
    """
    city = City(p_name=draw(st.text()), p_infection=draw(st.integers(min_value=0, max_value=2)))

    for i in range(draw(st.integers(min_value=0, max_value=3))):
        city.add_neighbour(City(p_name=draw(st.text()), p_infection=draw(st.integers(min_value=0, max_value=3))))

    return city


@st.composite
def cities(draw):
    """
    Generate cities with a random infection and 0 to 3 neigbours infected or not
    """
    city = City(p_name=draw(st.text()), p_infection=draw(st.integers(min_value=0, max_value=3)))

    for i in range(draw(st.integers(min_value=0, max_value=3))):
        city.add_neighbour(City(p_name=draw(st.text()), p_infection=draw(st.integers(min_value=0, max_value=3))))

    return city


@given(p_city=cities())
def test_add_neighbour(p_city):
    """
    Adding a neighbour to a city increases the number of neighour of 1
    City infected or not with 0 to 3 neighbours infected or not
    """

    nb_neighbours_before = len(p_city.neighbours)
    p_city.add_neighbour(City(p_name='Paris'))
    nb_neighbours_after = len(p_city.neighbours)

    assert nb_neighbours_after == nb_neighbours_before + 1


@given(p_city=not_source_cities())
def test_infect_increase(p_city):
    """
    Increase infection by 1 unit each time infect() is called
    City infected or not but not source
    """

    infection_before = p_city.infection
    p_city.infect()
    infection_after = p_city.infection

    assert infection_after == infection_before + 1


def test_infect_increase_city_source():
    """
    Do not increase infection of a source city while infect() is called
    City infection source
    """

    city = City(p_name='Paris', p_infection=3)

    infection_before = city.infection
    city.infect()
    infection_after = city.infection

    assert infection_after == infection_before


@given(p_city=infection_source_cities())
def test_infect_propagate(p_city: City):
    """
    If a city becomes an infection source, neighbours are infected too
    :param p_city: A city with an infection of 2, and 0 to 3 neighbours with no infection
    """

    p_city.infect()
    for city in p_city.neighbours:
        assert city.infection == 1

