from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec \
    import AdCreativeObjectStorySpec

from constants import *

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

link_data = AdCreativeLinkData()
link_data[AdCreativeLinkData.Field.message] = 'Everyone needs a home! Click "Like" and help the Pasadena Humane Society!'
link_data[AdCreativeLinkData.Field.link] = 'https://www.facebook.com/caltech.clickmaniac'
link_data[AdCreativeLinkData.Field.caption] = 'Puppies'
link_data[AdCreativeLinkData.Field.image_hash] = puppy_image_hash

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = 103185246428488
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id=my_account_id)
creative[AdCreative.Field.name] = 'Puppy Ad'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

print(creative)
