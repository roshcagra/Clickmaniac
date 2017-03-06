from facebookads.api import FacebookAdsApi
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.adobjects.targeting import Targeting
from constants import *

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

params = {
    'q': 'Pasadena, California',
    'type': 'adinterest',
}

resp = TargetingSearch.search(params=params)

print(resp)

# targeting = {
#     Targeting.Field.geo_locations: {
#         Targeting.Field.countries: ['US'],
#     },

# }
