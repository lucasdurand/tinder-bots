import requests
import json
facebook_token='CAAGm0PX4ZCpsBAFQb8oMZBOrniUqqvkhcfhKPzPxXgPvn7YZAOKZCISzakm0CFDzctwrLYtsUz6XqfpnGvG7vVn8E7YZAqmQ9EFE2nnReimR03YZAHxfDoRIYy8hhwZBbDjfCNlnuE9vQ4o4EdP3vrZBS1vwkB5itQ3qYncRzpZByeYfzZBHzFMNtzZCg3ma6MKEsRtY5CdpbKLSH0uSrrUM4ZBiZAUpcKJ3ZCNH4ZD'
facebook_id = '100008877671078'	#'id' #your numerical facebook id

loginCredentials = {'facebook_token':facebook_token, 'facebook_id' : facebook_id}
headers = {'Content-Type' : 'application/json', 'User-Agent' : 'Tinder Android Version 3.2.0'}

r = requests.post('https://api.gotinder.com/auth', data=json.dumps(loginCredentials), headers=headers)
x_auth_token = r.json()['token']


headers2 = {'User-Agent' : 'Tinder Android Version 3.2.0', 'Content-Type' : 'application/json', 'X-Auth-Token' : x_auth_token}
r2 = requests.get('https://api.gotinder.com/user/recs', headers=headers2)
hoes = r2.json()['results']
print hoes[0].keys()
#r3 = requests.post('https://api.gotinder.com/updates', data=json.dumps({'last_activity_date':''}),headers=headers2)


#prof = requests.get('https://api.gotinder.com/profile', headers=headers2)

#r4 = requests.post('https://api.gotinder.com/user/matches/544747f87ec2d347094b8bf954b71d2ca38bda49704e878c', data=json.dumps({'message':'Are you a magician?'}),headers=headers2)



'''for hoe in hoes:
        _id = hoe['_id']
        name = hoe['name']
        headers3 = {'X-Auth-Token' : x_auth_token, 'User-Agent' : 'Tinder Android Version 3.2.0'}
        r3 = requests.get('https://api.gotinder.com/like/' + _id, headers=headers3)
        print(_id)
        print(r3.status_code)
        print(name)
        '''
