# ropro reputation botter by blood#1000


import requests


cookies = open("cookies.txt", "r").read().split("\n")

target = input("User ID: ")



for cookie in cookies:
  
  roproveritoken = "" # find out how ropros auth system works
  roproid = "" # find out how ropros auth system works
  userid = "" # do some roblox api shit
  
  r=requests.post(
    "https://api.ropro.io/postReputation.php",
    headers={
      "ropro-verification": roproveritoken,
      "ropro-id": roproid
    },
    json={
      "type": "add",
      myUser: userid,
      theirUser: target
    }
  )

  
  # discountined look at my other repos
  # i have made this a full project
