#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 00:56:34 2021

Script to scrape tinder API

@author: gauravanand
"""
# In[]
import os
from Tinder import tinder_api
from Tinder import fb_auth_token


from dotenv import load_dotenv

host = 'https://api.gotinder.com' #thanks to this line you do not need to import config.py or tinder_config_ex.py



load_dotenv()

email = os.environ.get("email")
password = os.environ.get("password")

fb_access_token = fb_auth_token.get_fb_access_token(email, password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
tinder_api.get_auth_token(fb_access_token, fb_user_id, host)


# In[]
recommendations = tinder_api.get_recommendations()
display(recommendations)

# In[]
testid=recommendations['results'][3]['_id']
print(testid)
testperson=tinder_api.get_person(testid,host)
# In[]

display(testperson)