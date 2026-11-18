import requests
import os
from dotenv import load_dotenv
load_dotenv()

# 사용자입력 0 : 전역 커멘드 지정, 1 : 길드 커멘드 지정
print("전역커멘드면 0,\n길드커멘드면 1를 입력하세요")
# input()은 문자열을 돌려주므로 "0"/"1"과 비교하고, 올바른 값이 들어올 때까지 다시 묻는다.
while True:
    a = input().strip()
    if a == "0":
        url ="https://discord.com/api/v10/applications/"+str(os.environ.get("APPLICATION_ID"))+"/commands"
        break
    elif a == "1":
        url = "https://discord.com/api/v10/applications/"+str(os.environ.get("APPLICATION_ID"))+"/guilds/"+str(os.environ.get("GUILD_ID"))+"/commands"
        break
    else:
        print("잘못입력되었습니다. 다시입력하세요")
        
# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "blep2",
    "type": 1,
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": 5,
            "required": False
        }
    ]
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot " + str(os.environ.get("TOKEN"))
}

# or a client credentials token for your app with the applications.commands.update scope
# headers = {
#     "Authorization": "Bearer <my_credentials_token>"
# }

r = requests.post(url, headers=headers, json=json)