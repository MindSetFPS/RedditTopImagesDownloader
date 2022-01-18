import os
import shutil
import praw
import requests
from dotenv import load_dotenv
import datetime
import time

load_dotenv('./.env')


reddit = praw.Reddit(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    user_agent = os.getenv('USER_AGENT'),
    username = os.getenv('USERNAME'),
    password = os.getenv('PASSWORD')
)


dir = os.getcwd()
current_week = datetime.datetime.utcnow().isocalendar()[1]
dirpath = os.path.join(dir, 'week' + str(current_week))

if (os.path.isdir(dirpath) == False):
    os.mkdir(dirpath)
else:
    print('Directory already exists')

subreddits = ["LeagueOfMemes", "AatroxMains", "AhriMains", "akalimains", "AkshanMains", "alistarmains", "amumumains", "AniviaMains", "AnnieMains", "ApheliosMains", "AsheMains", "Aurelion_Sol_mains", "azirmains","bardmains", "blitzcrankmains", "BrandMains", "BraumMains", "Caitlynmains", "CamilleMains", "CassiopeiaMains", "ChoGathMains", "CorkiMains", "Dariusmains", "DianaMains", "DrMundoMains", "Draven", "ekkomains", "Elisemains", "EvelynnMains", "ezrealmains", "FiddlesticksMains", "FioraMains", "fizzmains", "galiomains", "gangplankmains", "GarenMains", "GnarMains", "GragasMains", "GravesMains", "GwenMains", "HecarimMains", "HeimerdingerMains", "Illaoi", "IreliaMains", "ivernmains", "Janna", "JarvanIVmains", "Jaxmains", "jaycemains", "JhinMains", "leagueofjinx", "kaisamains", "KalistaMains", "karmamains", "karthusmains", "KassadinMains", "KatarinaMains", "Kaylemains", "KaynMains", "Kennenmains", "KhaZixMains", "Kindred", "KledMains", "KogMawMains", "LeBlancMains", "LeeSinMains", "LeonaMains", "LilliaMains", "LissandraMains", "LucianMains", "lulumains", "lux", "YIMO", "malphitemains", "MalzaharMains", "MaokaiMains", "MissFortuneMains", "MordekaiserMains", "MorganaMains", "NamiMains",  "nasusmains", "NautilusMains", "neekomains", "NidaleeMains", "nocturnemains", "nunumains", "Olafmains", "OriannaMains", "ornnmains", "PantheonMains", "PoppyMains", "pykemains", "QiyanaMains", "QuinnMains", "RakanMains", "RammusMains", "reksaimains", "RellMains", "RenektonMains", "Rengarmains","Rivenmains", "Rumblemains", "RyzeMains", "SamiraMains", "sejuanimains",    "sennamains",    "SeraphineMains", "settmains", "shacomains", "Shen", "shyvanamains", "singedmains", "DirtySionMains", "Sivir", "SkarnerMains", "sonamains", "SorakaMains", "SwainMains", "sylasmains", "syndramains",  "Tahmkenchmains", "TaliyahMains", "Talonmains", "taricmains", "TeemoTalk","ThreshMains", "TristanaMains", "Trundlemains" , "TryndamereMains", "TwistedFateMains", "TwitchMains", "Udyrmains", "UrgotMains", "VarusMains", "vaynemains", "VeigarMains" ,"Velkoz","ViMains",  "ViegoMains", "viktormains", "VladimirMains", "VolibearMains", "warwickmains", "Wukongmains","xayahmains", "XerathMains", "XinZhaoMains", "YasuoMains", "YoneMains",    "yorickmains", "yuumimains", "thesecretweapon", "zedmains", "ZiggsMains",   "ZileanMains", "zoemains","zyramains"]

for subreddit in subreddits:
    print(subreddit)
    subreddit_instance = reddit.subreddit(subreddit)

    for submission in subreddit_instance.top("week", limit=2):
        #get submission url
        print(submission.title)
        url = str(submission.url)
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
            #give the file a name
            filename = str(submission.score) + ' upv ' + str(submission.upvote_ratio) +  '% ' + subreddit_instance.display_name + ' ' + submission.id
            r = requests.get(submission.url, stream = True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open( os.path.join( dirpath, filename ), 'wb') as f:
                    shutil.copyfileobj(r.raw,  f)
                time.sleep(2)
            # print(submission.url)