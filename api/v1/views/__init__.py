from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.places import *
from api.v1.views.users import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
<<<<<<< HEAD
=======
from api.v1.views.places_reviews import *
>>>>>>> a665912e3e58faedce1479b26a604ae35f72a3ad
