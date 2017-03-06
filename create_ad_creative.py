from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adcreative import AdCreative

from constants import *

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

creative = AdCreative(parent_id=my_account_id)
creative[AdCreative.Field.name] = 'Puppies Ad'
creative[AdCreative.Field.title] = 'Puppies'
creative[AdCreative.Field.body] = "Everyone needs a home! Click 'Like' and help the Pasadena Humane Society!"
creative[AdCreative.Field.object_id] = '103185246428488'
creative[AdCreative.Field.object_type] = AdCreative.ObjectType.page
creative[AdCreative.Field.image_hash] = puppy_image_hash

creative.remote_create()

print(creative)
