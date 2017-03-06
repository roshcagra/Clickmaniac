import datetime
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad

from constants import *

# Authentication
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

ad = Ad(parent_id=my_account_id)
ad[Ad.Field.name] = 'My Ad'
ad[Ad.Field.adset_id] = adset_id
ad[Ad.Field.creative] = {
    'creative_id': ad_creative_id,
}
ad.remote_create(params={
    'status': Ad.Status.paused,
})

print(ad)
