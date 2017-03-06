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
start = str(datetime.datetime(2017, 3, 6, 1, 0))
end = str(datetime.datetime(2017, 3, 8, 6, 0))
targeting = {
    'geo_locations': {
        'countries': ['US'],
    }
}

adset = AdSet(parent_id='act_196943804042546')
adset.update({
    AdSet.Field.name: 'Ad Set 1',
    AdSet.Field.campaign_id: 23842549663270548,
    AdSet.Field.daily_budget: 200,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.impressions,
    AdSet.Field.promoted_object: {
        "page_id": "103185246428488",
    },
    AdSet.Field.bid_amount: 2,
    AdSet.Field.targeting: targeting,
    AdSet.Field.start_time: start,
    AdSet.Field.end_time: end,
})

print adset
adset.remote_create(params={
    'status': AdSet.Status.paused,
})
