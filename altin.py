import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "6142462229"

mesaj = """
💰 Gram Altın

Test mesajı

🕒 İlk kurulum başarılı
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mesaj
    }
)

print("Mesaj gönderildi")
