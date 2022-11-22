# You can create a beautiful address for your wallet by generating addresses and searching them for the parameters you need.

Customization:
````python
CHAT_ID = "CHATID" - "Add your telegram id here (you can find out from the bot) @getmyid_bot"
BOT_TOKEN = "BOT TOKEN" - "Сan be created in a BotFather bot"
````
If the address you specified is found, it will come to you in the cart.


## In the Fields below, we substitute your values, the fewer characters, the faster the address will be found.
````python
if acct.address[:8] == "0x666666" and acct.address[-10:] == "6666666666":
````
````python
"0x666666" - "The first digits in the address"
[:8] - "Number of characters"
````
````python
"6666666666" - "The last digits in the address"
[-10:] - "Number of characters"
````
