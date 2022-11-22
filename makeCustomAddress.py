from eth_account import Account
from datetime import datetime
from requests import get
import hashlib
import os

def _telegram(text):
    CHAT_ID = "CHATID"
    BOT_TOKEN = "BOT TOKEN"
    data = {'chat_id': CHAT_ID, 'text':text, 'parse_mode':'html'}
    get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data=data)

def doWork():
    iw = 0
    while True:
        iw += 1
        mTime = datetime.now().strftime("%H:%M:%S")
        random_data = os.urandom(128)
        private = hashlib.sha256(random_data).hexdigest()
        acct = Account.from_key(private)
        
        if acct.address[:8] == "0x666666" and acct.address[-10:] == "6666666666":
            print(f"[{mTime}][{iw}]{acct.address}:{private}")
            _telegram(f"""[<b>WalletMaker</b>]\n[<code>{acct.address}</code>]\n<b>{private}</b>""")
        
        elif acct.address[:8] == "0x777777" and acct.address[-10:] == "7777777777":
            print(f"[{mTime}][{iw}]{acct.address}:{private}")
            _telegram(f"""[<b>WalletMaker</b>]\n[<code>{acct.address}</code>]\n<b>{private}</b>""")
        
        elif acct.address[:8] == "0x555555" and acct.address[-10:] == "5555555555":
            print(f"[{mTime}][{iw}]{acct.address}:{private}")
            _telegram(f"""[<b>WalletMaker</b>]\n[<code>{acct.address}</code>]\n<b>{private}</b>""")
        
        elif acct.address[:8] == "0x000000" and acct.address[-10:] == "0000000000":
            print(f"[{mTime}][{iw}]{acct.address}:{private}")
            _telegram(f"""[<b>WalletMaker</b>]\n[<code>{acct.address}</code>]\n<b>{private}</b>""")

        elif acct.address[:8] == "0x333333" and acct.address[-10:] == "3333333333":
            print(f"[{mTime}][{iw}]{acct.address}:{private}")
            _telegram(f"""[<b>WalletMaker</b>]\n[<code>{acct.address}</code>]\n<b>{private}</b>""")
        
        else:
            output = f"[{mTime}][{iw}]{acct.address}:{private}"
            print(output, end="\r")

doWork()