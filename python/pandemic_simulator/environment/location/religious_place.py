from dataclasses import dataclass

from ..interfaces import NonEssentialBusinessLocationState, ContactRate, SimTimeTuple, NonEssentialBusinessBaseLocation

__all__ = ['ReligiousPlace', 'ReligiousPlaceState']


@dataclass
class ReligiousPlaceState(NonEssentialBusinessLocationState):
    #TO D0: Rewrite these values
    contact_rate: ContactRate = ContactRate(1, 1, 1, 0.5, 0.7, 0.2)
    """
    Minimum number of contacts between assignees in the location
    Minimum number of contacts between assignees and visitors in the location
    Minimum number of contacts between visitors in the location
    A fraction of contacts between all assignees currently in the location. A value in [0, 1]
    A fraction of contacts between assignees and visitors currently in the location. A value in [0, 1]
    A fraction of contacts between all visitors currently in the location. A value in [0, 1]
    """
    # Churches open for 1 hour every Sunday
    open_time: SimTimeTuple = SimTimeTuple(hours=tuple(range(9, 11)), week_days=tuple(range(0, 1)))


class ReligiousPlace(NonEssentialBusinessBaseLocation[ReligiousPlaceState]):
    """Implements a religious place"""
    state_type = ReligiousPlaceState