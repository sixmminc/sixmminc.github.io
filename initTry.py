#!/usr/bin/env python
# Copyright (C) 2002-2020 CERN for the benefit of the ATLAS collaboration

import os, sys
import requests
import json


def main():

    cAccessToken = 'IGQVJYVVFnNlIxY1E3YWswc2lKckMxR0x5QkVaUXN1OFdCbWkxNXk3UUZAqTTgxOXlENm5sRk5wZAmVfY1ZAPZAEhQQWhQa3lmY2RCaGt2MHlFUlFPaElDai1IX0hjRmpmd2M4M3J0MWwyOF9lT2ZAJaVkydnYtcHZAUZAnhzajlF'
    userID = "17841437702100017"
    aAccessToken = "820869755388323|CKYO2xmTmcrt5x6HxrlRY3RnYh0"

    userInfo = getUserInfo(userID, cAccessToken)

    _printJson(userInfo)

    for media in userInfo["media"]["data"]:
        print media['id']

        mediaObj = getMediaInfo(media['id'], cAccessToken)

        _printJson(mediaObj)

        _printJson(getPostEmbed(mediaObj['permalink'], aAccessToken))



    # _printJson(getPostEmbed('https://www.instagram.com/p/CF5caZ1BPqw/', aAccessToken))



def getPostEmbed(url, accessToken):
    url = 'https://graph.facebook.com/v8.0/instagram_oembed?url=%s' %(url) 

    param = {}
    # param['url']          = url
    param['access_token'] = str(accessToken)

    output = _curlGet(url, param)

    return _toJson(output.text)



def getUserInfo(userID, accessToken):
    url = 'https://graph.instagram.com/%s' %(str(userID))

    param = {}
    param['fields']       = 'id,username,media_count,media'
    param['access_token'] = str(accessToken)

    output = _curlGet(url, param)

    return _toJson(output.text)


def getMediaInfo(mediaID, accessToken):
    url = 'https://graph.instagram.com/%s' %(str(mediaID))

    param = {}
    param['fields']       = 'caption,id,media_type,media_url,permalink,thumbnail_url,timestamp,username'
    param['access_token'] = str(accessToken)

    output = _curlGet(url, param)

    return _toJson(output.text)


def _curlGet(url, param):
    return requests.get(url, param)

def _toJson(inStr):
    return json.loads(inStr)

def _printJson(obj):
    print(json.dumps(obj, indent=2))

if __name__ == '__main__':
    sys.exit( main() )
