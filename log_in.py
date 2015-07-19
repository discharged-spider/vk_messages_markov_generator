import urllib
import webbrowser
import vk

def vk_log_in (ACCESS_TOKEN = None):
    if ACCESS_TOKEN == None:
        APP_ID = '3840303' #REPLACE WITH YOUR APP!
        SCOPE = 'notify,friends,photos,audio,video,docs,status,notes,pages,wall,groups,messages,offline,notifications,ads'

        auth_url = ("https://oauth.vk.com/authorize?client_id={app_id}"
                    "&scope={scope}"
                    "&redirect_uri=http://oauth.vk.com/blank.html"
                    "&display=page&response_type=token".format(scope=SCOPE, app_id=APP_ID))
        webbrowser.open_new_tab(auth_url)

        print ('Logging in. Put access token, please')

        redirected_url = input ("Paste here url you were redirected:\n")
        parsed_url = urllib.parse.parse_qs(redirected_url)

        print(parsed_url)

        parsed_url ['access_token'] = parsed_url ['https://oauth.vk.com/blank.html#access_token'];

        ACCESS_TOKEN = parsed_url ['access_token'][0]

    vkapi = vk.API (access_token=ACCESS_TOKEN, api_version='5.34')

    return vkapi