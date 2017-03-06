from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adimage import AdImage
from constants import *

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

image = AdImage(parent_id=my_account_id)
image[AdImage.Field.filename] = 'clickmaniac/humane_society/Puppies.jpg'
image.remote_create()

print(image[AdImage.Field.hash])
