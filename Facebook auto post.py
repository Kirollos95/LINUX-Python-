import requests
#Your Access Keys
page_id_1 = 100092406670152
facebook_access_token_1 = 'EAACtQXqZCFecBAHIHVM9BPfUcWaQNKbF9c5K0NdvgU8GMGxYEsx0gTKWBWYThFvmynd5ki4ky6WRwSQ6ZCgOyFdZALRqXma1poYV7zHPiPhIn8UmeNFD8F6mgG7ewSYzuQLXTlqLpZCXG6iBVnddbsCGJENZBFwe2I72OwqBmS9ZBCWO7kZCocSGNB2O7ZBYqkNGnHKW2EqKawZDZD'
msg = 'This Is An Automated Post Using Python'
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
payload = {
'message': msg,
'access_token': facebook_access_token_1
}
r = requests.post(post_url, data=payload)
print(r.text)