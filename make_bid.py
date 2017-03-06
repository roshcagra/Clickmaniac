from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adset import AdSet

# Authentication
my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
my_access_token = 'EAAEQRPLI1TYBAIDSZBKRNcvNDI0CSQ033ZBBSTg7AUVVJ7rmUFRHelM8xAJwGd9rZBGT9SckueUU7AkxqHRKIq1FMn0gI0f8K6Q57xaAAGkMDgxxtFxGlPjkhsZAVbIeFXZBZAqto6GnkPGmZCZBFtLV9fTpdY8bQ16zhGZC2f2rmfgZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

# Get Ad Set
adset = AdSet(23842549663280548)
adset[AdSet.Field.bid_amount] = 1
adset.remote_update()
