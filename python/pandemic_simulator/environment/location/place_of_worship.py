# Confidential, Copyright 2020, Sony Corporation of America, All rights reserved.
from dataclasses import dataclass

from ..interfaces import NonEssentialBusinessLocationState, ContactRate, SimTimeTuple, NonEssentialBusinessBaseLocation

__all__ = ['PlaceOfWorship', 'PlaceOfWorshipState']


@dataclass
class PlaceOfWorshipState(NonEssentialBusinessLocationState):
    contact_rate: ContactRate = ContactRate(5, 1, 0, 0.1, 0., 0.1)
    open_time: SimTimeTuple = SimTimeTuple(hours=tuple(range(9, 12)), week_days=tuple(range(6,7)))


class PlaceOfWorship(NonEssentialBusinessBaseLocation[PlaceOfWorshipState]):
    """Implements a place of worship."""
    state_type = PlaceOfWorshipState
