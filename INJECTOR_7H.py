import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleventh = STRING11
twelve = STRING12
thirteen = STRING13
fourteen  = STRING14
fifteen = STRING15
sixteen = STRING16
seventeen = STRING17
eighteen = STRING18
nineteen = STRING19
twenty = STRING20
twentyone = STRING21
twentytwo = STRING22
twentythree = STRING23
twentyfour = STRING24
twentyfive = STRING25
twentysix = STRING26
twentyseven = STRING27
twentyeight = STRING28
twentynine = STRING29
thirty = STRING30


xtr1 = ""
xtr2 = ""
xtr3 = ""
xtr5 = ""
xtr4 = ""
xtr6 = ""
xtr7 = ""
xtr8 = ""
xtr9 = ""
xtr10 = ""
xtr11 = ""
xtr12 = ""
xtr13 = ""
xtr14 = ""
xtr14 = ""
xtr16 = ""
xtr17 = ""
xtr18 = ""
xtr19 = ""
xtr20 = ""
xtr21 = ""
xtr22 = ""
xtr23 = ""
xtr24 = ""
xtr25 = ""
xtr26 = ""
xtr27 = ""
xtr28 = ""
xtr29 = ""
xtr30 = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_yukki():
    global xtr1
    global xtr2
    global xtr3
    global xtr5
    global xtr4
    global xtr6
    global xtr7
    global xtr8
    global xtr9
    global xtr10
    global xtr11
    global xtr12
    global xtr13
    global xtr14
    global xtr14
    global xtr16
    global xtr17
    global xtr18
    global xtr19
    global xtr20
    global xtr21
    global xtr22
    global xtr23
    global xtr24
    global xtr25
    global xtr26
    global xtr27
    global xtr28
    global xtr29
    global xtr30
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        xtr1 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await xtr1.start()
            botme = await xtr1.get_me()
            await xtr1(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr1(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            xtr1 = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        xtr1 = TelegramClient(session_name, a, b)
        try:
            await xtr1.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        xtr2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await xtr2.start()
            await xtr2(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr2(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        xtr2 = TelegramClient(session_name, a, b)
        try:
            await xtr2.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        xtr3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  xtr3.start()
            await xtr3(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr3(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        xtr3 = TelegramClient(session_name, a, b)
        try:
            await xtr3.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        xtr4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await xtr4.start()
            await xtr4(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr4(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        xtr4 = TelegramClient(session_name, a, b)
        try:
            await xtr4.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        xtr5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await xtr5.start()
            await xtr5(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr5(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        xtr5 = TelegramClient(session_name, a, b)
        try:
            await xtr5.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        xtr6 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await xtr6.start()
            await xtr6(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr6(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        xtr6 = TelegramClient(session_name, a, b)
        try:
            await xtr6.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        xtr7 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await xtr7.start()
            await xtr7(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr7(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        xtr7 = TelegramClient(session_name, a, b)
        try:
            await xtr7.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        xtr8 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await xtr8.start()
            await xtr8(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr8(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        xtr8 = TelegramClient(session_name, a, b)
        try:
            await xtr8.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        xtr10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await xtr10.start()
            await xtr10(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr10(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        xtr10 = TelegramClient(session_name, a, b)
        try:
            await xtr10.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        xtr9 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await xtr9.start()
            await xtr9(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr9(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        xtr9 = TelegramClient(session_name, a, b)
        try:
            await xtr9.start()
        except Exception as e:
            pass 
    if eleventh:
        session_name = str(eleventh)
        print("String 11 Found")
        xtr11 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await xtr11.start()
            botme = await xtr11.get_me()
            await xtr11(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr11(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            xtr11 = "eleventh"
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "startup"
        xtr11 = TelegramClient(session_name, a, b)
        try:
            await xtr11.start()
        except Exception as e:
            pass
   
    if twelve:
        session_name = str(twelve)
        print("String 12 Found")
        xtr12 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await xtr12.start()
            await xtr12(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr12(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        xtr12 = TelegramClient(session_name, a, b)
        try:
            await xtr12.start()
        except Exception as e:
            pass

    if thirteen:
        session_name = str(thirteen)
        print("String 13 Found")
        xtr13 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await  xtr13.start()
            await xtr13(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr13(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        xtr13 = TelegramClient(session_name, a, b)
        try:
            await xtr13.start()
        except Exception as e:
            pass

    if fourteen:
        session_name = str(fourteen)
        print("String 14 Found")
        xtr14 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await xtr14.start()
            await xtr14(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr14(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        xtr14 = TelegramClient(session_name, a, b)
        try:
            await xtr14.start()
        except Exception as e:
            pass

    if fifteen:
        session_name = str(fifteen)
        print("String 15 Found")
        xtr15 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await xtr15.start()
            await xtr15(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr15(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        xtr15 = TelegramClient(session_name, a, b)
        try:
            await xtr15.start()
        except Exception as e:
            pass
                  
    if sixteen:
        session_name = str(sixteen)
        print("String 16 Found")
        xtr16 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await xtr16.start()
            await xtr16(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr16(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr16.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        pass
        session_name = "startup"
        xtr16 = TelegramClient(session_name, a, b)
        try:
            await xtr16.start()
        except Exception as e:
            pass

    if seventeen:
        session_name = str(seventeen)
        print("String 17 Found")
        xtr17 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await xtr17.start()
            await xtr17(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr17(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr17.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        pass
        session_name = "startup"
        xtr17 = TelegramClient(session_name, a, b)
        try:
            await xtr17.start()
        except Exception as e:
            pass    
        
    
    if eighteen:
        session_name = str(eighteen)
        print("String 18 Found")
        xtr18 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await xtr18.start()
            await xtr18(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr18(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr18.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        pass
        session_name = "startup"
        xtr18 = TelegramClient(session_name, a, b)
        try:
            await xtr18.start()
        except Exception as e:
            pass   
        
    if nineteen:
        session_name = str(nineteen)
        print("String 19 Found")
        xtr19 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await xtr19.start()
            await xtr19(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr19(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr19.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        pass
        session_name = "startup"
        xtr19 = TelegramClient(session_name, a, b)
        try:
            await xtr19.start()
        except Exception as e:
            pass   
        
    
  
    if twenty:
        session_name = str(twenty)
        print("String 20 Found")
        xtr20 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await xtr20.start()
            await xtr20(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr20(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr20.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        pass
        session_name = "startup"
        xtr20 = TelegramClient(session_name, a, b)
        try:
            await xtr20.start()
        except Exception as e:
            pass   
        

    if twentyone:
        session_name = str(twentyone)
        print("String 21 Found")
        xtr21 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await xtr21.start()
            botme = await xtr21.get_me()
            await xtr21(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr21(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            xtr21 = "twentyone"
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        xtr21 = TelegramClient(session_name, a, b)
        try:
            await xtr21.start()
        except Exception as e:
            pass
   
    if twentytwo:
        session_name = str(twentytwo)
        print("String 22 Found")
        xtr22 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await xtr22.start()
            await xtr22(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr22(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "startup"
        xtr22 = TelegramClient(session_name, a, b)
        try:
            await xtr22.start()
        except Exception as e:
            pass

    if twentythree:
        session_name = str(twentythree)
        print("String 23 Found")
        xtr23 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await  xtr23.start()
            await xtr23(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr23(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "startup"
        xtr23 = TelegramClient(session_name, a, b)
        try:
            await xtr23.start()
        except Exception as e:
            pass

    if twentyfour:
        session_name = str(twentyfour)
        print("String 24 Found")
        xtr24 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await xtr24.start()
            await xtr24(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr24(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "startup"
        xtr24 = TelegramClient(session_name, a, b)
        try:
            await xtr24.start()
        except Exception as e:
            pass

    if twentyfive:
        session_name = str(twentyfive)
        print("String 25 Found")
        xtr25 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await xtr25.start()
            await xtr25(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr25(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "startup"
        xtr25 = TelegramClient(session_name, a, b)
        try:
            await xtr25.start()
        except Exception as e:
            pass
                  
    if twentysix:
        session_name = str(twentysix)
        print("String 26 Found")
        xtr26 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await xtr26.start()
            await xtr26(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr26(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "startup"
        xtr26 = TelegramClient(session_name, a, b)
        try:
            await xtr26.start()
        except Exception as e:
            pass

    if twentyseven:
        session_name = str(twentyseven)
        print("String 27 Found")
        xtr27 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await xtr27.start()
            await xtr27(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr27(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        xtr27 = TelegramClient(session_name, a, b)
        try:
            await xtr27.start()
        except Exception as e:
            pass    
        
    
    if twentyeight:
        session_name = str(twentyeight)
        print("String 28 Found")
        xtr28 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await xtr28.start()
            await xtr28(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr28(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        xtr28 = TelegramClient(session_name, a, b)
        try:
            await xtr28.start()
        except Exception as e:
            pass   
        
    if twentynine:
        session_name = str(twentynine)
        print("String 29 Found")
        xtr29 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await xtr29.start()
            await xtr29(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr29(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        xtr29 = TelegramClient(session_name, a, b)
        try:
            await xtr29.start()
        except Exception as e:
            pass   
        
    
  
    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        xtr30 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await xtr30.start()
            await xtr30(functions.channels.JoinChannelRequest(channel="@CHAT_INJECTOR7H"))
            await xtr30(functions.channels.JoinChannelRequest(channel="@INJECTOR_7H"))
            botme = await xtr30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        xtr30 = TelegramClient(session_name, a, b)
        try:
            await xtr30.start()
        except Exception as e:
            pass 




loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki()       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.join"))       
async def _(e):
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗝𝗼𝗶𝗻×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "𝙹𝙾𝙸𝙽𝙸𝙽𝙶..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]   〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))        
async def _(e):
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]   〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.leave"))       
async def _(e):
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗟𝗲𝗮𝘃𝗲×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "𝙻𝙴𝙰𝚅𝙸𝙽𝙶....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙻𝙴𝙵𝚃 !!\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗕𝗶𝗴𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗥𝗮𝗶𝗱×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@xtr1.on(events.NewMessage(incoming=True))
@xtr2.on(events.NewMessage(incoming=True))
@xtr3.on(events.NewMessage(incoming=True))
@xtr4.on(events.NewMessage(incoming=True))
@xtr5.on(events.NewMessage(incoming=True))
@xtr6.on(events.NewMessage(incoming=True))
@xtr7.on(events.NewMessage(incoming=True))
@xtr8.on(events.NewMessage(incoming=True))
@xtr9.on(events.NewMessage(incoming=True))
@xtr10.on(events.NewMessage(incoming=True))
@xtr11.on(events.NewMessage(incoming=True))
@xtr12.on(events.NewMessage(incoming=True))
@xtr13.on(events.NewMessage(incoming=True))
@xtr14.on(events.NewMessage(incoming=True))
@xtr15.on(events.NewMessage(incoming=True))
@xtr16.on(events.NewMessage(incoming=True))
@xtr17.on(events.NewMessage(incoming=True))
@xtr18.on(events.NewMessage(incoming=True))
@xtr19.on(events.NewMessage(incoming=True))
@xtr20.on(events.NewMessage(incoming=True))
@xtr21.on(events.NewMessage(incoming=True))
@xtr22.on(events.NewMessage(incoming=True))
@xtr23.on(events.NewMessage(incoming=True))
@xtr24.on(events.NewMessage(incoming=True))
@xtr25.on(events.NewMessage(incoming=True))
@xtr26.on(events.NewMessage(incoming=True))
@xtr27.on(events.NewMessage(incoming=True))
@xtr28.on(events.NewMessage(incoming=True))
@xtr29.on(events.NewMessage(incoming=True))
@xtr30.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱×××】\n\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᖇEᑭᒪY ᖇᗩIᗪ [ᗩᑕTIᐯᗩTEᗪ]!!\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱×××】\n【﻿Command :】\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!! ᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝚁𝙰𝙽𝙳𝙸 𝙺𝙸 𝙲𝙷𝚄𝙳𝙰𝙸 𝙳𝙾𝙽𝙴!!\nᖇEᑭᒪY ᖇᗩIᗪ [ᗪE-ᗩᑕTIᐯᗩTEᗪ]\n           〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🤤𝐆𝐀𝐍𝐃 !\n`{ms}` 𝗺𝘀\n           ⚔️𝟳𝗛 𝗦𝗣𝗔𝗠𝗕𝗢𝗧⚔️")




@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr15.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def alive(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 !!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f".🤖 I Am Still alive Lomdike !!!!\n`{ms}` 𝗺𝘀\n          〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄")
        
                      
        

@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "【﻿ＲＥＳＴＡＲＴＩＮＧ】!!!\nPʟᴇᴀꜱᴇ Wᴀɪᴛ Tɪʟʟ lᴛ Rᴇʙᴏᴏᴛꜱ..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await xtr1.disconnect()
        except Exception as e:
            pass
        try:
            await xtr2.disconnect()
        except Exception as e:
            pass
        try:
            await xtr3.disconnect()
        except Exception as e:
            pass
        try:
            await xtr4.disconnect()
        except Exception as e:
            pass
        try:
            await xtr5.disconnect()
        except Exception as e:
            pass
        try:
            await xtr6.disconnect()
        except Exception as e:
            pass
        try:
            await xtr7.disconnect()
        except Exception as e:
            pass
        try:
            await xtr8.disconnect()
        except Exception as e:
            pass
        try:
            await xtr10.disconnect()
        except Exception as e:
            pass
        try:
            await xtr9.disconnect()
        except Exception as e:
            pass
        try:
            await xtr11.disconnect()
        except Exception as e:
            pass
        try:
            await xtr12.disconnect()
        except Exception as e:
            pass
        try:
            await xtr13.disconnect()
        except Exception as e:
            pass
        try:
            await xtr14.disconnect()
        except Exception as e:
            pass
        try:
            await xtr15.disconnect()
        except Exception as e:
            pass
        try:
            await xtr16.disconnect()
        except Exception as e:
            pass
        try:
            await xtr17.disconnect()
        except Exception as e:
            pass
        try:
            await xtr18.disconnect()
        except Exception as e:
            pass
        try:
            await xtr19.disconnect()
        except Exception as e:
            pass
        try:
            await xtr20.disconnect()
        except Exception as e:
            pass
        try:
            await xtr21.disconnect()
        except Exception as e:
            pass
        try:
            await xtr22.disconnect()
        except Exception as e:
            pass
        try:
            await xtr23.disconnect()
        except Exception as e:
            pass
        try:
            await xtr24.disconnect()
        except Exception as e:
            pass
        try:
            await xtr25.disconnect()
        except Exception as e:
            pass
        try:
            await xtr26.disconnect()
        except Exception as e:
            pass
        try:
            await xtr27.disconnect()
        except Exception as e:
            pass
        try:
            await xtr28.disconnect()
        except Exception as e:
            pass
        try:
            await xtr29.disconnect()
        except Exception as e:
            pass
        try:
            await xtr30.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@xtr1.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr2.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr3.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr4.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr5.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr6.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr7.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr8.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr9.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr10.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr11.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr12.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr13.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr14.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr16.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr17.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr18.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr19.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr20.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr21.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr22.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr23.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr24.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr25.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr26.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr27.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr28.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr29.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xtr30.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "〄 ╔»⟦★𝟳𝗛★⟧«╗ SᑭᗩᗰᗰEᖇ ᗷOT 〄\n\n【﻿×××𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀×××】\n\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n.alive\n.restart\n.join\n.pjoin\n.leave\n\n【﻿𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n.raid\n.replyraid\n.dreplyraid\n.spam\n.bigspam\n.delayspam\nFor More Help Regarding Usage Of Plugins Type Plugins Name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """𝟳𝗛 𝗦𝗣𝗔𝗠𝗕𝗢𝗧"""

print(text)
print("")
print("SMEX! 𝟳𝗛 𝗦𝗣𝗔𝗠𝗕𝗢𝗧 STARTED.")
if len(sys.argv) not in (1, 3, 4):
    try:
        xtr1.disconnect()
    except Exception as e:
        pass
    try:
        xtr2.disconnect()
    except Exception as e:
        pass
    try:
        xtr3.disconnect()
    except Exception as e:
        pass
    try:
        xtr4.disconnect()
    except Exception as e:
        pass
    try:
        xtr5.disconnect()
    except Exception as e:
        pass
    try:
        xtr6.disconnect()
    except Exception as e:
        pass
    try:
        xtr7.disconnect()
    except Exception as e:
        pass
    try:
        xtr8.disconnect()
    except Exception as e:
        pass
    try:
        xtr9.disconnect()
    except Exception as e:
        pass
    try:
        xtr10.disconnect()
    except Exception as e:
        pass
    try:
        xtr11.disconnect()
    except Exception as e:
        pass
    try:
        xtr12.disconnect()
    except Exception as e:
        pass
    try:
        xtr13.disconnect()
    except Exception as e:
        pass
    try:
        xtr14.disconnect()
    except Exception as e:
        pass
    try:
        xtr14.disconnect()
    except Exception as e:
        pass
    try:
        xtr16.disconnect()
    except Exception as e:
        pass
    try:
        xtr17.disconnect()
    except Exception as e:
        pass
    try:
        xtr18.disconnect()
    except Exception as e:
        pass
    try:
        xtr19.disconnect()
    except Exception as e:
        pass
    try:
        xtr20.disconnect()
    except Exception as e:
        pass
    try:
        xtr21.disconnect()
    except Exception as e:
        pass
    try:
        xtr22.disconnect()
    except Exception as e:
        pass
    try:
        xtr23.disconnect()
    except Exception as e:
        pass
    try:
        xtr24.disconnect()
    except Exception as e:
        pass
    try:
        xtr25.disconnect()
    except Exception as e:
        pass
    try:
        xtr26.disconnect()
    except Exception as e:
        pass
    try:
        xtr27.disconnect()
    except Exception as e:
        pass
    try:
        xtr28.disconnect()
    except Exception as e:
        pass
    try:
        xtr29.disconnect()
    except Exception as e:
        pass
    try:
        xtr30.disconnect()
    except Exception as e:
        pass
else:
    try:
        xtr1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xtr30.run_until_disconnected()
    except Exception as e:
        pass
