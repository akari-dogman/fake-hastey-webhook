import requests
import json
import datetime

webhook = "" # put webhook here

if webhook == "":
    webhook = input("What's the webhook? ")
else:
    print("Webhook detected")

embed = {
  "embeds": [
    {
      "title": "Supreme Swarovski Box Logo Hooded Sweatshirt",
      "description": "Payment Success",
      "url": "https://discordapp.com",
      "color": 16711680,
      "timestamp": str(datetime.datetime.utcnow()),
      "footer": {
        "icon_url": "https://images-ext-2.discordapp.net/external/ta4tJn1LlCb8Htj38238uEXrcIif9Mua3SjqwvEkyfU/https/emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/147/leaf-fluttering-in-wind_1f343.png",
        "text": "HasteyIO Supreme"
      },
      "image": {
        "url": "https://images-ext-1.discordapp.net/external/bScyuQ2zL4s_fSKx9CKA-oHHRQYXCEQr6W0kEGEcIkQ/https/assets.supremenewyork.com/169434/ma/rDJJnS9OT7w.jpg"
      },
      "fields": [
        {
          "name": "Profile",
          "value": "main",
          "inline": True
        },
        {
          "name": "Checkout Time",
          "value": "0.04s",
          "inline": True
        },
        {
          "name": "Style",
          "value": "Heather Grey",
          "inline": True
        },
        {
          "name": "Size",
          "value": "Small",
          "inline": True
        }
      ]
    }
  ]
}

payload = embed
print(payload)
debug = requests.post(webhook,data=json.dumps(payload),headers={"Content-Type":"application/json"})
print(debug)
print(debug.text)