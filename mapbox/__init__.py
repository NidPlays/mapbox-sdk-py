# mapbox
__version__ = "0.18.2"

from .services.datasets import Datasets
from .services.directions import Directions
from .services.geocoding import (
    Geocoder, InvalidCountryCodeError, InvalidPlaceTypeError)
from .services.mapmatching import MapMatcher
from .services.matrix import DirectionsMatrix
from .services.surface import Surface
from .services.static import Static
from .services.static_style import StaticStyle
from .services.uploads import Uploader
from .services.analytics import Analytics
from .services.tilequery import Tilequery
from .services.maps import Maps
