

image = AdImage(parent_id='act_<AD_ACCOUNT_ID>')
image[AdImage.Field.filename] = '<IMAGE_PATH>'
image.remote_create()
