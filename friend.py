import requests

cookies = open("cookies.txt", "r").read().split("\n")
                                                
bot = input("User ID: ")

for cookie in cookies:
  session.cookies['.ROBLOSECURITY'] = cookie
  session.headers['x-csrf-token'] = session.get('https://www.roblox.com/home').content.decode('utf8').split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
  session.post(f'https://friends.roblox.com/v1/users/{bot}/request-friendship')
# omg so annoying spam good 2022 fast ez legit no cap!!
