import os
import re


class Config:
    ADMIN = "1331188677"
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = 1971546
    CHAT = "-1001166584294"
    LOG_GROUP= "-1001166584294"
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL= "https://radioindia.net/radio/hungamanow/icecast.audio"
    API_HASH = "b994bccad6118cd6fb6d091b9bbfe5cf"
    BOT_TOKEN = "1701786146:AAEOQxCqkUQfoK3iWyPHYmZemg1bWJwt_9U" 
    SESSION = "BQBRfZNvZ_OJfC75U-BU-IyW_IStzWVY0HGPhtZKfHAufWqJz6syhcX8blJNEijlsU2NNkTJgD3opJSY-dpA-m24IQeqdxWu9oBoug-JAen8zdddD2QojCY-7ehGMKaJ08KhSUuExNSzwoC9ya_KYuY3ObZR41Y3_sI9ogEZO4q-bZRcWVsLANUTHDehQqtD4GmCNdBL9zfY4Mp82ln60njKOx40HC7GPEZaqF2C2D6HOVNTwowpBAadU4a6r32AL8D7lD_T4-4Qk7TlXjLLlzPaavJjpzjeiTHLa15XwqSaoNayrPRNRPtUwyVvl2-C87WFjo3ZJHLJUbb9Yt3HfeOKT1hTxQA"

