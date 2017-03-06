import datetime
from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adimage import AdImage

from constants import *

# Authentication
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

# Get Ad Account
my_account = objects.AdAccount(my_account_id)
print(my_account)

# Get Ad Campaign
campaign = Campaign(my_campaign_id)
campaign.remote_read(fields=[
    Campaign.Field.name,
    Campaign.Field.effective_status,
    Campaign.Field.objective,
])

print(campaign)

# Get Ad Set
adset = AdSet(23842549663280548)
adset.remote_read(fields=[
    AdSet.Field.name,
    AdSet.Field.effective_status,
    AdSet.Field.bid_amount,
])
print adset
adset[AdSet.Field.bid_amount] = 1
adset.remote_update()

# Do shit with the campaign: make an ad, set target, etc, etc

# Do bidding (make this a standalone file)


#
# today = datetime.date.today()
# start_time = str(today + datetime.timedelta(days=-1))
# end_time = str(today + datetime.timedelta(days=2))
#
# print end_time
#
# exit()
#
# adset = AdSet(parent_id='act_196943804042546')
# adset.update({
#     AdSet.Field.name: 'My Ad Set',
#     AdSet.Field.campaign_id: 23842549663270548,
#     AdSet.Field.daily_budget: 1000,
#     AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
#     AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
#     AdSet.Field.bid_amount: 2,
#     #AdSet.Field.targeting: <TARGETING>,
#     AdSet.Field.start_time: start_time,
#     AdSet.Field.end_time: end_time,
# })
#
# adset.remote_create(params={
#     'status': AdSet.Status.paused,
# })
#
#
# from facebookads.adobjects.adimage import AdImage
#
# image = AdImage(parent_id='act_<AD_ACCOUNT_ID>')
# image[AdImage.Field.filename] = '<IMAGE_PATH>'
# image.remote_create()
#
# # Output image Hash
# print(image[AdImage.Field.hash])
#
#
# from facebookads.adobjects.adcreative import AdCreative
# from facebookads.adobjects.adcreative'<LINK>'data import AdCreativeLinkData
# from facebookads.adobjects.adcreativeobjectstoryspec \
#     import AdCreativeObjectStorySpec
#
# link_data = AdCreativeLinkData()
# link_data[AdCreativeLinkData.Field.message] = 'try it out'
# link_data[AdCreativeLinkData.Field.link] = '<LINK>'
# link_data[AdCreativeLinkData.Field.caption] = 'My caption'
# link_data[AdCreativeLinkData.Field.image_hash] = '<IMAGE_HASH>'
#
# object_story_spec = AdCreativeObjectStorySpec()
# object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = <PAGE_ID>
# object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data
#
# creative = AdCreative(parent_id='act_<AD_ACCOUNT_ID>')
# creative[AdCreative.Field.name] = 'AdCreative for Link Ad'
# creative[AdCreative.Field.object_story_spec] = object_story_spec
# creative.remote_create()
#
# print(creative)
