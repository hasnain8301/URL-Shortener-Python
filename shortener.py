import requests
def Shortener(full_link, link_name):
    API_KEY = '3a4acb156c923191e6c96b656023bd90f7c8b'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key':API_KEY, 'short':full_link, 'name':link_name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print(f'Title : {title}')
        print(f'short link : {short_link}')

    except:
        status = data['url']['status']
        print(f"Error Status : {status}")

link = input("Please Enter the link to be shortener : ")
name = input("Please Enter the name to your link : ")

Shortener(link,name)
