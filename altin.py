import os
import requests
from datetime import datetime

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "6142462229"

# Gram altın verisi
r = requests.get(
    "https://api.genelpara.com/json/?list=altin&sembol=GA"
)

data = r.json()

gram = data["GA"]

fiyat = gram["satis"]
degisim = gram["degisim"]

tarih = datetime.now().strftime("%d.%m.%Y")

mesaj = f"""
📅 {tarih}

💰 Gram Altın
{fiyat} TL

📈 Günlük Değişim: %{degisim}
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mesaj
    }
)

print("Mesaj gönderildi")
