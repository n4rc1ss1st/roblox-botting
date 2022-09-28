import requests
cookies = open("cookies.txt", "r").read().split("\n")

bot = input("User ID: ")

for cookie in cookies:
  session = requests.Session()
  session.cookies['.ROBLOSECURITY'] = cookie
  session.headers['x-csrf-token'] = session.get('https://www.roblox.com/home').content.decode('utf8').split("Roblox.XsrfToken.setToken('")[1].split("');")[0]
  requests.post(f"https://friends.roblox.com/v1/users/{bot}/follow")

# ezzz lel
