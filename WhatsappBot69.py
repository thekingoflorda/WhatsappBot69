from ast import parse
from urllib import response

#from sqlalchemy import false

def check_messages():
    global savedMessageDataList, messageDataList, Messages, messagesSend, commandsIssuedList
    getTexts()
    if savedMessageDataList == []:
        savedMessageDataList = messageDataList
    commandsIssuedList = []
    for i in range(20):
        try:
            if messageDataList[-i - 1] == savedMessageDataList[-1]:
                if i == 0:
                    savedMessageDataList = messageDataList
                    return False
                else:
                    savedMessageDataList = messageDataList
                    for x in range(i):
                        commandsIssuedList.append(messageDataList[len(Messages) - x - 1])
                        if emojiList[len(Messages) - x - 1] > emojiLimit:
                            responseFunction("Emoji Alert, you just used {} emojis...".format(emojiList[len(Messages) - x - 1]))
                    return True 
        except IndexError as e:
            savedMessageDataList = messageDataList
            return False

def getTexts():
    global savedMessageDataList, messageDataList, Messages, emojiList
    while True:
        try:
            Messages = driver.find_elements_by_class_name("_22Msk")
            messageDataList = []
            emojiList = []
            for enu, message in enumerate(Messages):
                try:
                    emojiList.append(len(message.find_element_by_class_name("i0jNr.selectable-text.copyable-text").find_elements_by_css_selector("img")))
                except Exception:
                    emojiList.append(0)
                if len(message.find_elements_by_class_name("_2jGOb.copyable-text")) > 0:
                    messageDataList.append(message.find_elements_by_class_name("_2jGOb.copyable-text")[0].get_attribute("data-pre-plain-text") + Messages[enu].find_elements_by_class_name("i0jNr.selectable-text.copyable-text")[0].text)
                elif len(message.find_elements_by_class_name("copyable-text")) > 0:
                    messageDataList.append(message.find_elements_by_class_name("copyable-text")[0].get_attribute("data-pre-plain-text") + Messages[enu].find_elements_by_class_name("i0jNr.selectable-text.copyable-text")[0].text)
                else:
                    messageDataList.append("")
            break
        except Exception as e:
            print("error: ", e)

def commandParser(message):
    global lastRenameTime, botName, countGameRecord, countGameCounter, startingTime, commandsIssued, messagesScanned, pollList, refreshes, countGameName, antiSimpModus
    try:
        parsedMessageList = message.split(":")
        unparsedName = parsedMessageList[1]
        parsedName = unparsedName.split("] ")[1]
        del parsedMessageList[0]
        del parsedMessageList[0]
        parsedMessage = ""
        for item in parsedMessageList:
            parsedMessage += (item + ":")
        parsedMessage = parsedMessage[0:-1]
        parsedMessage = parsedMessage[1:]
        print("parsed message: \"", parsedMessage + "\"")
    except Exception as e:
        responseFunction("EpicBot69 says: " + "Error with parsing message: " + str(e))

    messagesScanned += 1
    commandsIssued += 1

    try:
        if not parsedMessage.startswith(botName + " says:"):  
            if parsedName in data["personalData"].keys():
                data["personalData"][parsedName]["messagesSend"] += 1
                if data["personalData"][parsedName]["messagesSend"] == 100:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 1!".format(parsedName))
                elif data["personalData"][parsedName]["messagesSend"] == 200:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 2!".format(parsedName))
                elif data["personalData"][parsedName]["messagesSend"] == 500:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 3!".format(parsedName))
                elif data["personalData"][parsedName]["messagesSend"] == 1000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 4!".format(parsedName))
                elif data["personalData"][parsedName]["messagesSend"] == 2000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 5!".format(parsedName))
                elif data["personalData"][parsedName]["messagesSend"] == 5000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 6!".format(parsedName))
                elif data["personalData"][parsedName]["messagesSend"] == 10000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 7!".format(parsedName))

            for item in notifyList:
                if parsedName == item[0]:
                    responseFunction(item[2] + " wanted to notify " + item[0] + " of: " + item[1])
                    del notifyList[notifyList.index(item)]
            try:
                if "ElectionTime" in data["savedVars"].keys():
                    if time.time() > data["savedVars"]["ElectionTime"] + data["savedVars"]["termLength"] * 24 * 60 * 60:
                        threading.Timer(10800, voteCounter).start()
                        responseFunction("It's time for elections! Vote for a player by typing \"presidentvote:[player]\". Remember that if you don't vote, one vote will be subtracted from your vote count. The election will end in 3 hours.")
                        for player in list(data["personalData"].keys()):
                            data["personalData"][player]["vote"] = -1
                        data["savedVars"]["ElectionTime"] = time.time()
                else:
                    data["savedVars"]["ElectionTime"] = time.time() - data["savedVars"]["termLength"] * 24 * 60 * 60
                    data["savedVars"]["president"] = "none"
                    data["savedVars"]["cabinet"] = ["", "", ""]
                    for cabinetMemberCounter, cabinetMember in enumerate(data["savedVars"]["cabinet"]):
                        newCabinetMember = random.choice(list(data["personalData"].keys()))
                        while newCabinetMember in data["savedVars"]["cabinet"]:
                            newCabinetMember = random.choice(list(data["personalData"].keys()))
                        data["savedVars"]["cabinet"][cabinetMemberCounter] = newCabinetMember
                if random.randint(1, 10) == 1:
                    data["savedVars"]["newMoney"] += data["savedVars"]["economyGain"] / 10
                    data["savedVars"]["expectedMarketCap"] += data["savedVars"]["economyGain"] / 10
                if parsedName in antiSimpPersons and antiSimpModus:
                    if random.randint(0, 10) == 10:
                        responseFunction(random.choice(["Moet jij niet in de keuken staan ofzo?", "Oh god, een meisje...", "Ja ik ben sexistisch, dus?", "Het leven is hard, vooral als er een meisje in de whatsapp groep zit...", "Anti-simp modus is actief, dus praat ik opeens nederlands.", "Ik vindt dat de nieuwe James Bond een vrouw moet zijn, stel je voor hoe goed de explosies en de auto-crashes zullen zijn. En dat terwijl ze aan het parkeren is.", "Sexisme in de banenmarkt bestaat niet. Vrouwen kiezen simpelweg slechtbetalende banen, mannen worden dokter, rechter of professor. Vrouwen worden vrouwlijke dokter, vrouwlijke rechter of vrouwlijke proffesor.", ""]))
                if parsedMessage.startswith("!"):
                    if parsedMessage.lower() == "!time":
                        responseFunction(str(datetime.datetime.now().time()))
                    elif parsedMessage.lower() == "!coin":
                        responseFunction(random.choice(["Heads", "Tails"]))
                    elif parsedMessage.lower() == "!dice":
                        responseFunction(str(random.randint(1, 6)))
                    elif parsedMessage.lower().startswith("!spam") and ":" in parsedMessage:
                        if parsedName not in muted:
                            try:
                                for i in range(int(parsedMessage.split(":")[0].replace("!Spam", "").replace("!spam", ""))):
                                    if i < 10:
                                        responseFunction(parsedMessage.split(":")[1].replace("\n", " | "))
                                if parsedName in data["personalData"].keys():
                                    data["personalData"][parsedName]["spamCommandUsed"] += 1
                                    if data["personalData"][parsedName]["spamCommandUsed"] == 10:
                                        responseFunction("{} has unlocked the achievement: SPAMMER 1!".format(parsedName))
                                    elif data["personalData"][parsedName]["spamCommandUsed"] == 20:
                                        responseFunction("{} has unlocked the achievement: SPAMMER 2!".format(parsedName))
                                    elif data["personalData"][parsedName]["spamCommandUsed"] == 50:
                                        responseFunction("{} has unlocked the achievement: SPAMMER 3!".format(parsedName))
                                    elif data["personalData"][parsedName]["spamCommandUsed"] == 100:
                                        responseFunction("{} has unlocked the achievement: SPAMMER 4!".format(parsedName))
                            except Exception as error:
                                print("Error: ", error)
                                responseFunction("Error: You made somekind of mistake, to do it right do !Spam<amount>:<message>")
                        else:
                            responseFunction("STFU, your muted...")
                    elif parsedMessage.lower() == "!stats":
                        responseFunction("Commands issued: " + str(commandsIssued) + " Messages scanned: " + str(messagesScanned) + " Bot started at: " + str(startingTime) + " refreshes: " + str(refreshes))
                    elif parsedMessage.lower() == "!name":
                        responseFunction(parsedName)
                    elif parsedMessage.lower().startswith("!mute:"):
                        if parsedName in admins:
                            muted.append(parsedMessage.split(":")[1])
                            responseFunction("Muted " + parsedMessage.split(":")[1])
                        else:
                            responseFunction("You are not an admin")
                    elif parsedMessage.lower().startswith("!unmute:"):
                        if parsedName in admins:
                            if parsedMessage.split(":")[1] in muted:
                                muted.remove(parsedMessage.split(":")[1])
                                responseFunction("Unmuted " + parsedMessage.split(":")[1])
                            else:
                                responseFunction("User is not muted")
                        else:
                            responseFunction("You are not an admin")
                    elif parsedMessage.lower().startswith("!mutelist"):
                        responseFunction("Muted users: " + str(muted))
                    elif parsedMessage.lower().startswith("!adminlist"):
                        responseFunction("Admins: " + str(admins))
                    elif parsedMessage.lower().startswith("!presidentvote:"):
                        if parsedMessage.split(":")[1].replace("@", "") not in data["savedVars"]["cabinet"] and parsedMessage.split(":")[1].replace("@", "") != parsedName and parsedMessage.split(":")[1].replace("@", "") in data["personalData"].keys():
                            data["personalData"][parsedName]["vote"] = list(data["personalData"].keys()).index(parsedMessage.split(":")[1].replace("@", ""))
                            responseFunction("You have voted for " + parsedMessage.split(":")[1])
                        elif parsedMessage.split(":")[1].replace("@", "") == parsedName:
                            responseFunction("You can't vote for yourself. Your vote has NOT been counted.")
                        elif parsedMessage.split(":")[1].replace("@", "") not in data["personalData"].keys():
                            responseFunction("{} does not excist".format(parsedMessage.split(":")[1]))
                        else:
                            responseFunction("A cabinet member can't be the president. Your vote has NOT been counted.")
                    elif parsedMessage.lower().startswith("!unadmin:"):
                        if parsedName == "Luc van Remmerden":
                            if parsedMessage.split(":")[1] in admins:
                                admins.remove(parsedMessage.split(":")[1])
                                responseFunction("Unadmined " + parsedMessage.split(":")[1])
                            else:
                                responseFunction("User is not an admin")
                        else:
                            responseFunction("You are not an my creator")
                    elif parsedMessage.lower() == "!truck":
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if "truckAmount" not in data["personalData"][parsedName].keys():
                                for player in data["personalData"].keys():
                                    data["personalData"][player]["truckAmount"] = 0
                                    data["savedVars"]["newMoney"] = 0
                                    data["savedVars"]["truckerFee"] = 0.1
                                responseFunction("You don't have any trucks.")
                            else:
                                if data["personalData"][parsedName]["truckAmount"] > 0:
                                    data["savedVars"]["bankMoney"] += data["savedVars"]["newMoney"] * (1- data["savedVars"]["truckerFee"])
                                    dividendGiver("bank", data["savedVars"]["newMoney"] * (1- data["savedVars"]["truckerFee"]))
                                    if random.randint(1, 20) == 1:
                                        responseFunction("You shipped {} trucks to the bank. You received {}% of the money. Your truck broke down ):".format(data["savedVars"]["newMoney"], str(data["savedVars"]["truckerFee"] * 100)))
                                        data["personalData"][parsedName]["truckAmount"] -= 1
                                    else:
                                        responseFunction("You shipped {} trucks to the bank. You received {}% of the money.".format(data["savedVars"]["newMoney"], str(data["savedVars"]["truckerFee"] * 100)))
                                    data["personalData"][parsedName]["money"] += data["savedVars"]["newMoney"] * data["savedVars"]["truckerFee"]
                                    data["savedVars"]["newMoney"] = 0
                                else:
                                    responseFunction("You don't have any trucks.")
                        else:
                            responseFunction("Everyone, laugh at {} while they are trying to drive a truck in prison!".format(parsedName))
                    elif parsedMessage.lower() == "!buytruck":
                        if data["personalData"][parsedName]["money"] >= 100:
                            data["personalData"][parsedName]["money"] -= 100
                            data["personalData"][parsedName]["truckAmount"] += 1
                            data["savedVars"]["bankMoney"] += 100
                            dividendGiver("bank", 100)
                            responseFunction("You bought a truck for 100$")
                        else:
                            responseFunction("You don't have enough money.")
                    elif parsedMessage.lower() == "!truckinfo":
                        responseFunction("You have {} trucks. The trucker fee is {}%. There's {}$ money that needs to be shipped.".format(data["personalData"][parsedName]["truckAmount"], str(data["savedVars"]["truckerFee"] * 100), round(data["savedVars"]["newMoney"], 2)))

                    elif parsedMessage.lower().startswith("!stocks:"):
                            userInvestmentList = []
                            totalInvestment = 0
                            for receiver in data["personalData"].keys():
                                userInvestmentList.append(0)
                                if data["personalData"][receiver]["prisonLabor"] == 0:
                                    for investment in data["personalData"][receiver]["investments"]:
                                        if investment[2] == parsedMessage.split(":")[1].replace("@", ""):
                                            if investment[2] != "bank":
                                                userInvestmentList[-1] += investment[1] * (data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["money"] / investment[0])
                                                totalInvestment += investment[1] * (data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["money"] / investment[0])
                                            else:
                                                userInvestmentList[-1] += investment[1] * (data["savedVars"]["bankMoney"] / investment[0])
                                                totalInvestment += investment[1] * (data["savedVars"]["bankMoney"] / investment[0])

                            dividendString = ""
                            for player in data["personalData"].keys():
                                if data["personalData"][player]["prisonLabor"] == 0:
                                    dividendString += "{} has {}% of the total investments || ".format(player, str(round(userInvestmentList[list(data["personalData"].keys()).index(player)] / totalInvestment * 100, 2)))
                            
                            responseFunction(dividendString)
                                    
                            
                    elif parsedMessage.lower().startswith("!admin:"):
                        if parsedName == "Luc van Remmerden":
                            if parsedMessage.split(":")[1] not in admins:
                                admins.append(parsedMessage.split(":")[1])
                                responseFunction("Admined " + parsedMessage.split(":")[1])
                            else:
                                responseFunction("User is already an admin")
                        else:
                            responseFunction("You are not an my creator")
                    elif parsedMessage.lower() == "!cloverupgradelist":
                        responseFunction(str(cloverUpgradeList))
                    elif parsedMessage.lower() == "!clover":
                        responseFunction(parsedName + "\'s cloverupgrade: " + str(data["personalData"][parsedName]["cloverUpgrade"]))
                    elif parsedMessage.lower() == "!marketcap":
                        marketCap = 100
                        for player in data["personalData"].keys():
                            marketCap += data["personalData"][player]["money"]
                        responseFunction("The market cap is: " + str(marketCap) + " and the expected market cap is: " + str(data["savedVars"]["expectedMarketCap"]))
                    elif parsedMessage.lower().startswith("!quote"):
                        responseFunction("\"" + parsedMessage.split(":")[1] + "\" - " + parsedMessage.split(":")[0].replace("!quote", "").replace("!Quote", "") + " (" + str(datetime.datetime.now()) + ")")
                    elif parsedMessage.lower().startswith("!createpoll:"):
                        if parsedName not in muted and parsedName not in [Poll.creatorName for Poll in pollList]:
                            optionList = []
                            voteList = []
                            for i in range(len(parsedMessage.split(":")) - 3):
                                optionList.append(parsedMessage.split(":")[i + 3])
                                voteList.append([])
                            pollList.append(Poll(parsedName, parsedMessage.split(":")[1].lower(), parsedMessage.split(":")[2], optionList, voteList))
                            pollResponse = "Poll created \n Vote with: "
                            for option in optionList:
                                pollResponse += "!vote" + parsedMessage.split(":")[1] +":" + option + " "
                            responseFunction(pollResponse)
                            print("Poll created: ", parsedMessage.split(":")[1])
                        elif parsedName in muted:
                            responseFunction("STFU, your muted...")
                        else:
                            responseFunction("You can only create one poll at a time, use \"!endpoll\" to end the current poll")
                    elif parsedMessage.lower().startswith("!vote"):
                        if parsedMessage.split(":")[0].lower().replace("!vote", "") in [poll.pollName for poll in pollList]:
                            for poll in pollList:
                                if parsedMessage.split(":")[0].lower().replace("!vote", "") == poll.pollName:
                                    alreadyVoted= False
                                    for anwser in poll.votes:
                                        if parsedName in anwser:
                                            alreadyVoted = True
                                    if not alreadyVoted:
                                        if parsedMessage.split(":")[1] in [option for option in poll.options]:
                                            poll.votes[poll.options.index(parsedMessage.split(":")[1])].append(parsedName)
                                            responseFunction(parsedName + " voted for " + parsedMessage.split(":")[1])
                                            print(poll.votes)
                                        else:
                                            responseFunction(parsedName + ", that option does not exist")
                                    else:
                                        responseFunction(parsedName + ", You already voted")
                        else:
                            responseFunction(parsedName + ", Poll does not exist")
                    elif parsedMessage.lower() == "!polllist":
                        responseFunction("Poll list: " + str([poll.pollName for poll in pollList]))
                    elif parsedMessage.lower() == "!endpoll":
                        for poll in pollList:
                            if parsedName == poll.creatorName:
                                print(poll.votes)
                                responseFunction("The " + poll.pollName + " poll has ended, the results are:")
                                for i in range(len(poll.options)):
                                    responseFunction(poll.options[i] + ": " + str(len(poll.votes[i])))
                                pollList.remove(poll)
                    elif parsedMessage.lower() == "!joke":
                        if parsedName not in muted:
                            counter = 0
                            while True:
                                counter += 1
                                joke = jokes.random()
                                if "setup" in joke.keys():
                                    try:
                                        joke = jokes.random()
                                        responseFunction(joke['setup'])
                                        responseFunction(joke['delivery'])
                                        break
                                    except:
                                        pass
                                elif 'joke' in joke.keys():
                                    responseFunction(joke['joke'])
                                    break
                                elif counter > 20:
                                    responseFunction("The joke API has run out of funny juice. Please try again later.")
                                    break
                            if parsedName in data["personalData"].keys():
                                data["personalData"][parsedName]["jokes"] += 1
                                if data["personalData"][parsedName]["jokes"] == 10:
                                        responseFunction("{} has unlocked the achievement: JOKER 1!".format(parsedName))
                                elif data["personalData"][parsedName]["jokes"] == 20:
                                    responseFunction("{} has unlocked the achievement: JOKER 2!".format(parsedName))
                                elif data["personalData"][parsedName]["jokes"] == 50:
                                    responseFunction("{} has unlocked the achievement: JOKER 3!".format(parsedName))
                                elif data["personalData"][parsedName]["jokes"] == 100:
                                    responseFunction("{} has unlocked the achievement: JOKER 4!".format(parsedName))
                        else:
                            responseFunction("STFU, your muted...")
                    elif parsedMessage.lower() == "!reseteconomy":
                        data["savedVars"]["expectedMarketCap"] = 100
                        data["savedVars"]["bankMoney"] = 100
                        data["savedVars"]["economyGain"] = 1
                        data["savedVars"].pop("ElectionTime")
                        data["savedVars"]["tax"] = 0.05
                        data["savedVars"]["bankDividend"] = 0.10

                        if parsedName == "Luc van Remmerden":
                            for user in data["personalData"]:
                                data["personalData"][user]["money"] = 100
                                data["savedVars"]["expectedMarketCap"] += 100
                                data["personalData"][user]["claimTime"] = time.time() - 900000000
                                data["personalData"][user]["dividendTime"] = time.time() - 900000000
                                data["personalData"][user]["dividend"] = 0
                                data["personalData"][user]["cloverUpgrade"] = 0
                                data["personalData"][user]["investments"] = []
                            responseFunction("Economy has been reset!")
                        else:
                            responseFunction("You are not my creator")
                    elif parsedMessage.lower().startswith("!addadore:"):
                        if parsedName not in muted:
                            data["savedVars"]["adoreList"].append(parsedMessage.split(":")[1])
                            responseFunction("Added " + parsedMessage.split(":")[1] + " to the adore list")
                        else:
                            responseFunction("STFU, your muted...")
                    elif parsedMessage.lower().startswith("!adore:"):
                        responseFunction(parsedMessage.replace("!adore:", "") + ": " + random.choice(data["savedVars"]["adoreList"]))
                    elif parsedMessage.lower() == "!dividendlist":
                        divdidendListString = ""
                        for player in data["personalData"].keys():
                            if "dividend" not in data["personalData"][player].keys():
                                data["personalData"][player]["dividend"] = 0
                            divdidendListString += player + ": " + str(data["personalData"][player]["dividend"]) + " || "
                        responseFunction(divdidendListString)
                    elif parsedMessage.lower().startswith("!dividend:"):
                        if "dividendTime" not in data["personalData"][parsedName].keys():
                            data["personalData"][parsedName]["dividendTime"] = time.time()
                            if float(parsedMessage.split(":")[1].replace("%", "")) < 100 and float(parsedMessage.split(":")[1].replace("%", "")) >= 0:
                                data["personalData"][parsedName]["dividend"] = float(parsedMessage.split(":")[1].replace("%", ""))
                                responseFunction("Dividend set to " + parsedMessage.split(":")[1])
                        elif data["personalData"][parsedName]["dividendTime"] + 86400 < time.time():
                            if float(parsedMessage.split(":")[1].replace("%", "")) < 100 and float(parsedMessage.split(":")[1].replace("%", "")) >= 0:
                                data["personalData"][parsedName]["dividend"] = float(parsedMessage.split(":")[1].replace("%", ""))
                                responseFunction("Dividend set to " + parsedMessage.split(":")[1])
                                data["personalData"][parsedName]["dividendTime"] = time.time()
                        else:
                            responseFunction("You can only set the dividend once every 24 hours.")
                    elif parsedMessage.lower().startswith("!moneylist"):
                        moneyListString = ""
                        for player in data["personalData"].keys():
                            if "money" not in data["personalData"][player].keys():
                                data["personalData"][player]["money"] = 100
                                data["personalData"][player]["cloverUpgrade"] = 0
                            moneyListString += (player + ": " + str(round(data["personalData"][player]["money"], 2)) + " || ")
                        if "bankMoney" in data["savedVars"].keys():
                            moneyListString += ("Bank: " + str(round(data["savedVars"]["bankMoney"], 2)))
                        else:
                            data["savedVars"]["bankMoney"] = 0
                        responseFunction(moneyListString)
                    elif parsedMessage.lower().startswith("!invest:"):
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if "investments" not in data["personalData"][parsedName].keys():
                                for player in data["personalData"].keys():
                                    data["personalData"][player]["investments"] = []
                            if parsedMessage.split(":")[1].lower() == "bank":
                                if data["personalData"][parsedName]["money"] > int(parsedMessage.split(":")[2]):
                                    data["personalData"][parsedName]["money"] -= int(parsedMessage.split(":")[2])
                                    data["savedVars"]["bankMoney"] += int(parsedMessage.split(":")[2])
                                    data["personalData"][parsedName]["investments"].append([data["savedVars"]["bankMoney"], int(parsedMessage.split(":")[2]), "bank"])
                                    responseFunction("You invested " + parsedMessage.split(":")[2] + " in the bank")
                                else:
                                    responseFunction("{} does not have enough money to invest that much or you are trying to invest less than 1 money.".format(parsedName))
                            # elif parsedMessage.split(":")[1].lower() == "appie":
                            #     if data["personalData"][parsedName]["money"] > int(parsedMessage.split(":")[2]):
                            #         data["personalData"][parsedName]["money"] -= int(parsedMessage.split(":")[2])
                            #         data["personalData"][parsedName]["investments"].append([yf.Ticker('MSFT').info["marketCap"], int(parsedMessage.split(":")[2]), "appie"])
                            #         responseFunction("You invested " + parsedMessage.split(":")[2] + " in Appie")
                            elif parsedMessage.split(":")[1].replace("@", "") in data["personalData"].keys() and parsedMessage.split(":")[1].replace("@", "") != parsedName:
                                if int(parsedMessage.split(":")[2]) < data["personalData"][parsedName]["money"] and int(parsedMessage.split(":")[2]) > 0:
                                    data["personalData"][parsedName]["money"] -= int(parsedMessage.split(":")[2])
                                    data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["money"] += int(parsedMessage.split(":")[2])
                                    data["personalData"][parsedName]["investments"].append([data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["money"], int(parsedMessage.split(":")[2]), parsedMessage.split(":")[1].replace("@", "")])
                                    responseFunction("{} invested {} in {}".format(parsedName, parsedMessage.split(":")[2], parsedMessage.split(":")[1].replace("@", "")))
                                elif parsedMessage.split(";")[1].replace("@", "") == parsedName:
                                    responseFunction("You can't invest money in yourself.")
                                else:
                                    responseFunction("{} does not have enough money to invest that much or you are trying to invest less than 1 money.".format(parsedName))
                            else:
                                responseFunction("{} does not exist".format(parsedMessage.split(":")[1].replace("@", "")))
                        else:
                            responseFunction("Prisoners can't invest! Get back to work, you useless piece of shit!")
                    elif parsedMessage.lower() == "!prisonwork":
                        if "prisonLaborTime" not in data["personalData"][parsedName].keys():
                            for player in data["personalData"].keys():
                                data["personalData"][player]["prisonLabor"] = 0
                                data["personalData"][player]["prisonLaborTime"] = time.time()
                        if data["personalData"][parsedName]["prisonLabor"] > 0 and data["personalData"][parsedName]["prisonLaborTime"] < time.time():
                            data["personalData"][parsedName]["prisonLabor"] -= 1
                            if data["personalData"][parsedName]["prisonLabor"] == 0:
                                if data["savedVars"]["bankMoney"] >= 2:
                                    data["personalData"][parsedName]["money"] += 2
                                    data["savedVars"]["bankMoney"] -= 2
                                else:
                                    responseFunction("The bank doesn't have enough money to pay you 2 bucks, and has decided to not give you shit, no problem (:")
                                responseFunction("You where released from prison. We have succesfully rehabilitated you, right?")
                            else:
                                if data["savedVars"]["bankMoney"] >= 2:
                                    data["personalData"][parsedName]["money"] += 2
                                    data["savedVars"]["bankMoney"] -= 2
                                else:
                                    responseFunction("The bank doesn't have enough money to pay you 2 bucks, and has decided to not give you shit, no problem (:")
                                randomWorkAmount = random.randint(60, 3600)
                                data["personalData"][parsedName]["prisonLaborTime"] = time.time() + randomWorkAmount
                                responseFunction("You worked in prison and received 2 whole moneyz, you need to rest for {} seconds. You need to work {} more to get released.".format(randomWorkAmount, data["personalData"][parsedName]["prisonLabor"]))
                        elif data["personalData"][parsedName]["prisonLabor"] == 0:
                            responseFunction("You are not in prison.")
                        else:
                            responseFunction("You need to rest for {} seconds before you can work again. You need to work {} more to get released.".format(str(data["personalData"][parsedName]["prisonLaborTime"] - time.time()), data["personalData"][parsedName]["prisonLabor"]))
                    elif parsedMessage.lower().startswith("!investlist"):
                        investmentListString = parsedName + "\'s investments: "
                        for enu, investment in enumerate(data["personalData"][parsedName]["investments"]):
                            if investment[2].lower() == "bank":
                                investmentListString += str(enu) + ": " + str(round(investment[1] * (data["savedVars"]["bankMoney"] / investment[0]), 2)) + " ({})".format(str(investment[1])) + " in " + investment[2] + " || "
                            elif investment[2].lower() == "appie":
                                investmentListString += str(enu) + ": " + str(round(investment[1] * (yf.Ticker('MSFT').info["marketCap"] / investment[0]), 2)) + " ({})".format(str(investment[1])) + " in " + investment[2] + " || "
                            else:
                                investmentListString += str(enu) + ": " + str(round(investment[1] * (data["personalData"][investment[2]]["money"] / investment[0]), 2)) + " ({})".format(str(investment[1])) + " in " + investment[2] + " || "
                        responseFunction(investmentListString)
                    elif parsedMessage.lower().startswith("!sell:"):
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if len(data["personalData"][parsedName]["investments"]) > int(parsedMessage.split(":")[1]):
                                if data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2] == "bank":
                                    data["personalData"][parsedName]["money"] += data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["savedVars"]["bankMoney"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * (1 - data["savedVars"]["tax"])
                                    dividendGiver(parsedName, data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["savedVars"]["bankMoney"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * (1 - data["savedVars"]["tax"]))
                                    data["savedVars"]["bankMoney"] -= data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["savedVars"]["bankMoney"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * (1 - data["savedVars"]["tax"])
                                    dividendGiver("bank", data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["savedVars"]["bankMoney"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * data["savedVars"]["tax"])
                                    data["personalData"][parsedName]["investments"].pop(int(parsedMessage.split(":")[1]))
                                    responseFunction("{} sold their investment in the bank, they paid {}% in taxes".format(parsedName, data["savedVars"]["tax"] * 100))
                                # elif data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2] == "appie":
                                #     data["savedVars"]["bankMoney"] += data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (yf.Ticker('MSFT').info["marketCap"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * data["savedVars"]["tax"]
                                #     data["personalData"][parsedName]["money"] += data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (yf.Ticker('MSFT').info["marketCap"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * (1 - data["savedVars"]["tax"])
                                #     dividendGiver(parsedName, data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (yf.Ticker('MSFT').info["marketCap"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * (1 - data["savedVars"]["tax"]))
                                #     data["personalData"][parsedName]["investments"].pop(int(parsedMessage.split(":")[1]))
                                #     responseFunction("{} sold their investment in Appie, they paid {}% in taxes".format(parsedName, data["savedVars"]["tax"] * 100))
                                else:
                                    data["personalData"][parsedName]["money"] += data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["personalData"][data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2]]["money"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * (1 - data["savedVars"]["tax"])
                                    data["savedVars"]["bankMoney"] += data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["personalData"][data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2]]["money"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * data["savedVars"]["tax"]
                                    dividendGiver(parsedName, data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["personalData"][data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2]]["money"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * (1 - data["savedVars"]["tax"]))
                                    data["personalData"][data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2]]["money"] -= data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["personalData"][data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2]]["money"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0])
                                    dividendGiver("bank", data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][1] * (data["personalData"][data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][2]]["money"] / data["personalData"][parsedName]["investments"][int(parsedMessage.split(":")[1])][0]) * data["savedVars"]["tax"])
                                    data["personalData"][parsedName]["investments"].pop(int(parsedMessage.split(":")[1]))
                                    responseFunction("{} sold their investment {}, they paid {}% in taxes.".format(parsedName, parsedMessage.split(":")[1], str(data["savedVars"]["tax"] * 100)))
                        else:
                            responseFunction("Prisoners can't sell investments.")
                    elif parsedMessage.lower().startswith("!money"):
                        responseFunction(parsedName + " has " + str(data["personalData"][parsedName]["money"]) + " money")
                    elif parsedMessage.lower() == "!upgradeclover":
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if "cloverUpgrade" in data["personalData"][parsedName].keys():
                                if cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][0] < data["personalData"][parsedName]["money"]:
                                    if data["personalData"][parsedName]["cloverUpgrade"] < len(cloverUpgradeList) - 1:
                                        data["personalData"][parsedName]["money"] -= cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][0]
                                        data["savedVars"]["bankMoney"] += cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][0]
                                        dividendGiver("bank", cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][0])
                                        data["personalData"][parsedName]["cloverUpgrade"] += 1
                                        responseFunction("Upgraded " + parsedName + " to " + cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][2] + "!")
                                    else:
                                        responseFunction("You already have the max upgrade!")
                                else:
                                    responseFunction("You don't have enough money to upgrade " + parsedName)
                            else:
                                responseFunction("Error: message my master.")
                        else:
                            responseFunction("Prisoners can't upgrade their clover.")
                    elif parsedMessage.lower() == "!claim":
                        if "claimTime" in data["personalData"][parsedName].keys():
                            if data["personalData"][parsedName]["claimTime"] + 86400 < time.time() and data["personalData"][parsedName]["prisonLabor"] == 0:
                                randomClaimAmount = random.randint(1, int(100 / cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1]))
                                if data["savedVars"]["bankMoney"] - randomClaimAmount > 1:
                                    data["personalData"][parsedName]["money"] += randomClaimAmount
                                    data["savedVars"]["bankMoney"] -= randomClaimAmount
                                    dividendGiver(parsedName, randomClaimAmount)
                                    data["personalData"][parsedName]["claimTime"] = time.time()
                                    responseFunction("{} claimed {} money, you can claim again in 24 hours.".format(parsedName, randomClaimAmount))
                                elif data["savedVars"]["bankMoney"] > 1:
                                    responseFunction("{} claimed {} money, you can claim again in 24 hours.".format(parsedName, data["savedVars"]["bankMoney"] - 1))
                                    data["personalData"][parsedName]["money"] += data["savedVars"]["bankMoney"] - 1
                                    dividendGiver(parsedName, data["savedVars"]["bankMoney"] - 1)
                                    data["savedVars"]["bankMoney"] = 1
                                    data["personalData"][parsedName]["claimTime"] = time.time()
                                else:
                                    responseFunction("The bank has run out of money.")
                            elif data["personalData"][parsedName]["prisonLabor"] > 0:
                                responseFunction("Prisoners can't claim.")
                            else:
                                responseFunction("You can claim again in {} seconds.".format(str(data["personalData"][parsedName]["claimTime"] + 86400 - time.time())))
                        else:
                            data["personalData"][parsedName]["claimTime"] = time.time()
                            randomClaimAmount = random.randint(1, int(100 / cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1]))
                            data["personalData"][parsedName]["money"] += randomClaimAmount
                            data["savedVars"]["bankMoney"] -= randomClaimAmount
                            dividendGiver(parsedName, randomClaimAmount)
                            data["personalData"][parsedName]["claimTime"] = time.time()
                            responseFunction("{} claimed {} money, you can claim again in 24 hours.".format(parsedName, randomClaimAmount))
                    elif parsedMessage.lower().startswith("!sendmoney:"):
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if parsedMessage.split(":")[1].replace("@", "") in data["personalData"].keys():
                                if float(parsedMessage.split(":")[2]) < data["personalData"][parsedName]["money"]:
                                    data["personalData"][parsedName]["money"] -= float(parsedMessage.split(":")[2])
                                    data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["money"] += float(parsedMessage.split(":")[2])
                                    responseFunction("{} sent {} money to {}".format(parsedName, parsedMessage.split(":")[2], parsedMessage.split(":")[1].replace("@", "")))
                                else:
                                    responseFunction("{} does not have enough money to send that much".format(parsedName))
                            else:
                                responseFunction("{} does not exist".format(parsedMessage.split(":")[1].replace("@", "")))
                        else:
                            responseFunction("Prisoners can't send money.")
                    elif parsedMessage.lower().startswith("!gamble:"):
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if float(parsedMessage.split(":")[1]) < data["personalData"][parsedName]["money"] and float(parsedMessage.split(":")[1]) > 0:
                                data["personalData"][parsedName]["gambleAmount"] = float(parsedMessage.split(":")[1])
                                responseFunction("Gamble challange created, type !acceptgamble:{} to accept".format(parsedName))
                            else:
                                responseFunction("{} does not have enough money to gamble that much, or you are trying to send gamble less than 1.".format(parsedName))
                        else:
                            responseFunction("Prisoners can't gamble.")
                    elif parsedMessage.lower().startswith("!acceptgamble:"):
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if parsedMessage.split(":")[1] in data["personalData"].keys():
                                if "gambleAmount" in data["personalData"][parsedMessage.split(":")[1]].keys() and data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"] > 0:
                                    if data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"] < data["personalData"][parsedName]["money"] and data["personalData"][parsedMessage.split(":")[1]]["money"] > data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]:
                                        if random.randint(1, 2) == 1:
                                            data["personalData"][parsedName]["money"] += data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]
                                            data["personalData"][parsedMessage.split(":")[1]]["money"] -= data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]
                                            responseFunction("{} won {} money".format(parsedName, data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]))
                                        else:
                                            data["personalData"][parsedName]["money"] -= data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]
                                            data["personalData"][parsedMessage.split(":")[1]]["money"] += data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]
                                            responseFunction("{} lost {} money".format(parsedName, data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]))
                                        data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"] = 0
                                    elif data["personalData"][parsedMessage.split(":")[1]]["money"] > data["personalData"][parsedMessage.split(":")[1]]["gambleAmount"]:
                                        responseFunction("{} does not have enough money to accept the gamble".format(parsedName))
                                    else:
                                        responseFunction("{} does not have enough money to accept the gamble".format(parsedMessage.split(":")[1]))
                                else:
                                    responseFunction("{} has no gamble to accept".format(parsedMessage.split(":")[1]))
                            else:
                                responseFunction("{} does not exist".format(parsedMessage.split(":")[1]))
                        else:
                            responseFunction("Prisoners can't accept a gamble.")
                    elif "!steal" == parsedMessage.lower():
                        if data["personalData"][parsedName]["prisonLabor"] == 0 and data["personalData"][parsedName]["judge"] == None:
                            if "stealTime" not in data["personalData"][parsedName].keys():
                                for player in data["personalData"].keys():
                                    data["personalData"][player]["stealTime"] = -1
                                    data["personalData"][player]["judge"] = None
                            if data["personalData"][parsedName]["stealTime"] == -1:
                                data["personalData"][parsedName]["stealTime"] = time.time()
                                responseFunction("{} is now stealing from the bank, type !catch:{} to stop him, if {} types !steal again in 10 minutes he receives {}".format(parsedName, parsedName, parsedName, data["savedVars"]["bankMoney"] * 0.5 * (1 - cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1])))
                            elif time.time() - data["personalData"][parsedName]["stealTime"] > 600:
                                print(time.time() - data["personalData"][parsedName]["stealTime"])
                                data["personalData"][parsedName]["stealTime"] = -1
                                data["personalData"][parsedName]["money"] += data["savedVars"]["bankMoney"] * 0.5 * (1 -  cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1])
                                dividendGiver(parsedName, data["savedVars"]["bankMoney"] * 0.5 * (1- cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1]))
                                responseFunction("{} has stolen {} money from the bank".format(parsedName, data["savedVars"]["bankMoney"] * 0.5 * (1 - cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1])))
                                data["savedVars"]["bankMoney"] -= data["savedVars"]["bankMoney"] * 0.5 * (1 - cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1])
                            else:
                                responseFunction("You have to wait {} seconds before you have succesfully robbed the bank".format(600 + data["personalData"][parsedName]["stealTime"] - time.time()))
                        elif data["personalData"][parsedName]["judge"] != None:
                            responseFunction("You can't steal after you have been arrested.")
                        else:
                            responseFunction("Wait... you broke the law and got arrested for it... and then you do it again while in prison? You can't steal while in prison, idiot.")
                    elif parsedMessage.lower().startswith("!catch:"):
                        if data["personalData"][parsedName]["prisonLabor"] == 0:
                            if parsedMessage.split(":")[1].replace("@", "").replace("Luc Van remmerden", "Luc van Remmerden") in data["personalData"].keys():
                                if data["personalData"][parsedMessage.split(":")[1].replace("@", "").replace("Luc Van remmerden", "Luc van Remmerden")]["stealTime"] != -1:
                                    data["personalData"][parsedMessage.split(":")[1].replace("@", "").replace("Luc Van remmerden", "Luc van Remmerden")]["stealTime"] = -1
                                    responseFunction("{} has been caught while stealing from the bank".format(parsedMessage.split(":")[1].replace("@", "").replace("Luc Van remmerden", "Luc van Remmerden")))
                                    arrest(parsedMessage.split(":")[1].replace("@", "").replace("Luc Van remmerden", "Luc van Remmerden"), 1)
                            else:
                                responseFunction("{} does not exist".format(parsedMessage.split(":")[1]))
                        else:
                            responseFunction("It's good that you are trying to turn around your life, but you're in prison... it's hard to catch thieves while in a cell...")
                    elif parsedMessage.lower().startswith("!sentence:"):
                        found = False
                        for player in data["personalData"].keys():
                            if data["personalData"][player]["judge"] == parsedName:
                                if int(parsedMessage.split(":")[1]) <= 10 and int(parsedMessage.split(":")[1]) > 0:
                                    sentence(int(parsedMessage.split(":")[1]), data["personalData"][player]["sentenceMultiplier"], player)
                                    found = True
                                    break
                                else:
                                    responseFunction("wat probeer je, stop met bugs proberen te vinden.")
                        if not found:
                            responseFunction("You are not the judge of any sentence")
                    elif "!emojilimit:" in parsedMessage.lower():
                        if parsedName in admins:
                            try:
                                emojilimit = int(parsedMessage.split(":")[1])
                                responseFunction("Emoji limit set to " + str(emojilimit))
                            except:
                                responseFunction("Error: invalid number")
                        else:
                            responseFunction("You are not an admin")
                    elif parsedMessage.lower().startswith("!count:"):
                        if parsedName != countGameName:
                            countGameName = parsedName
                            try:
                                if int(parsedMessage.split(":")[1]) == countGameCounter + 1:
                                    countGameCounter += 1
                                    responseFunction("Counted!")
                                else:
                                    if countGameCounter > countGameRecord:
                                        countGameRecord = countGameCounter
                                    endString = random.choice(["Great, you just ruined this... Thanks.", "Wow! you are great at counting! You just ruined the count...", "You just ruined the count...", "I hereby sentence you to a re-education camp for counting."])
                                    responseFunction(endString + " || The count was " + str(countGameCounter) + " the record is " + str(countGameRecord))
                                    countGameCounter = 0
                            except ValueError:
                                responseFunction("You didn't enter a number")
                        else:
                            responseFunction(random.choice(["You can't go twice in a row, you dum dum.", "Give the other players a chance, you can't go twice in a row ):<", "NO! Don't go twice in a row!", "Bad! You went twice in a row, and I caught you in the act.", "STFU, you can't go twice in a row!", "Stop... Going... Twice... In... A... Row..."]))
                    elif parsedMessage.lower().startswith("!addpickupline:"):
                        if parsedName not in muted and len(parsedMessage) > 10 and parsedMessage not in pickUpLineList:
                            pickUpLineList.append(parsedMessage.split(":")[1])
                            responseFunction("Added pickupline: " + parsedMessage.split(":")[1])
                        elif len(parsedMessage) < 11:
                            responseFunction("Your pickup line need to be at least 11 characters long")
                        elif parsedMessage in pickUpLineList:
                            responseFunction("Your pickupline is already in the list")
                        else:
                            responseFunction("STFU, you're muted...")
                    elif parsedMessage.lower() == "!pickupline":
                        if parsedName not in muted:
                            responseFunction(random.choice(pickUpLineList))
                        else:
                            responseFunction("STFU, you're muted...")
                    elif parsedMessage.lower() == "!nuke":
                        if parsedName == "Luc van Remmerden":
                            responseFunction("Quiting program...")
                            sys.exit()
                    elif parsedMessage.lower() == "!deletepickupline":
                        if parsedName in admins:
                            del pickupllineList[-1]
                            responseFunction("Removed pickupline")
                    elif parsedMessage.lower() == "!save":
                        saveFile()
                        responseFunction("Saved data")
                    elif parsedMessage.lower() == "!achievements":
                        if parsedName in data["personalData"].keys():
                            responseFunction("MessageSend(100, 200, 500, 1000, 2000, 5000, 10000): {} || Thomas emoji(10, 20, 50, 100): {} || \"ik ben gay\"(10, 20, 50, 100): {} || praiser(10, 20, 50, 100): {} || praised(10, 20, 50, 100): {} || spammer(10, 20, 50, 100): {} || joker(10, 20, 50, 100): {}".format(data["personalData"][parsedName]["messagesSend"], data["personalData"][parsedName]["thomasEmoji"], data["personalData"][parsedName]["gayUsage"], data["personalData"][parsedName]["praiseSend"], data["personalData"][parsedName]["praiseReceived"], data["personalData"][parsedName]["spamCommandUsed"], data["personalData"][parsedName]["jokes"]))
                        else:
                            responseFunction("You are not yet implemented into the achievement system, contact my creator.")
                    
                    elif parsedMessage.lower() == "!royalty":
                        if "royalty" not in data["savedVars"].keys():
                            data["savedVars"]["royalty"] = {}
                            data["savedVars"]["royalty"]["king"] = random.choice(list(data["personalData"].keys()))
                            #data["savedVars"]["royalty"]["king"] = "Luc van Remmerden"
                            data["savedVars"]["royalty"]["title"] = "King"
                            data["savedVars"]["royalty"]["heir"] = random.choice(list(data["personalData"].keys()))
                            data["savedVars"]["royalty"]["nickName"] = "the founder"
                            data["savedVars"]["royalty"]["royalDecreesLeft"] = 1
                            data["savedVars"]["royalty"]["lifeLimit"] = random.randint(48, 336)
                            for player in data["personalData"].keys():
                                data["personalData"][player]["kingNumber"] = 0
                            data["personalData"][data["savedVars"]["royalty"]["king"]]["kingNumber"] = 1
                        if data["personalData"][data["savedVars"]["royalty"]["king"]]["kingNumber"] == 1:
                            royalTitle = data["savedVars"]["royalty"]["title"] + " " + data["savedVars"]["royalty"]["king"] + " the first " + data["savedVars"]["royalty"]["nickName"]
                        elif data["personalData"][data["savedVars"]["royalty"]["king"]]["kingNumber"] == 2:
                            royalTitle = data["savedVars"]["royalty"]["title"] + " " + data["savedVars"]["royalty"]["king"] + " the second " + data["savedVars"]["royalty"]["nickName"]
                        elif data["personalData"][data["savedVars"]["royalty"]["king"]]["kingNumber"] == 3:
                            royalTitle = data["savedVars"]["royalty"]["title"] + " " + data["savedVars"]["royalty"]["king"] + " the third " + data["savedVars"]["royalty"]["nickName"]
                        else:
                            royalTitle = data["savedVars"]["royalty"]["title"] + " " + data["savedVars"]["royalty"]["king"] + " the " + str(data["personalData"][data["savedVars"]["royalty"]["king"]]["kingNumber"]) + "th " + data["savedVars"]["royalty"]["nickName"]
                        responseFunction("Our great {} is {}. The heir to the crown is {}. The {} has {} royal decrees left.".format(data["savedVars"]["royalty"]["title"], royalTitle, data["savedVars"]["royalty"]["heir"], data["savedVars"]["royalty"]["title"], data["savedVars"]["royalty"]["royalDecreesLeft"]))
                    elif parsedMessage.lower().startswith("!heir:"):
                        if parsedName == data["savedVars"]["royalty"]["king"] and parsedMessage.split(":")[1].replace("@", "") in data["personalData"].keys() and parsedMessage.split(":")[1].replace("@", "") != data["savedVars"]["royalty"]["king"]:
                            data["savedVars"]["royalty"]["heir"] = parsedMessage.split(":")[1].replace("@", "")
                            responseFunction("The heir to the crown is now {}".format(parsedMessage.lower().split(":")[1]))
                        elif parsedName != data["savedVars"]["royalty"]["king"]:
                            responseFunction("You are not the {}".format(data["savedVars"]["royalty"]["title"]))
                        elif parsedMessage.split(":")[1].replace("@", "") == data["savedVars"]["royalty"]["king"]:
                            responseFunction("The {} can't be the heir to their own crown".format(data["savedVars"]["royalty"]["title"]))
                        else:
                            responseFunction("That player doesn't exist.")
                    elif parsedMessage.lower().startswith("!royaltitle:"):
                        if parsedName == data["savedVars"]["royalty"]["king"]:
                            if "\n" not in parsedMessage.split(":")[1] and len(parsedMessage.split(":")[1]) < 20:
                                data["savedVars"]["royalty"]["title"] = parsedMessage.split(":")[1]
                                responseFunction("The royal title has been changed to {}".format(data["savedVars"]["royalty"]["title"]))
                            else:
                                responseFunction("That title is not proper for someone of your class (length should be < 20, no enters allowed (fuck you thomas))")
                        else:
                            responseFunction("You are not the king")
                    elif parsedMessage.lower().startswith("!royalpardon:"):
                        if parsedName == data["savedVars"]["royalty"]["king"] and data["savedVars"]["royalty"]["royalDecreesLeft"] > 0:
                            if parsedMessage.split(":")[1].replace("@", "") in data["personalData"].keys():
                                data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["prisonLabor"] = 0
                                data["savedVars"]["royalty"]["royalDecreesLeft"] -= 1
                                responseFunction("{} has been pardoned".format(parsedMessage.split(":")[1]))
                            else:
                                responseFunction("That player doesn't exist.")
                        elif parsedName != data["savedVars"]["royalty"]["king"]:
                            responseFunction("You are not the king")
                        else:
                            responseFunction("You have no more royal decrees left")
                    elif parsedMessage.lower().startswith("!royalarrest:"):
                        if parsedName == data["savedVars"]["royalty"]["king"] and data["savedVars"]["royalty"]["royalDecreesLeft"] > 0:
                            if parsedMessage.split(":")[1].replace("@", "") in data["personalData"].keys():
                                if data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["prisonLabor"] == 0:
                                    arrest(parsedMessage.split(":")[1].replace("@", "").replace("Luc Van remmerden", "Luc van Remmerden"), 3)
                                    data["savedVars"]["royalty"]["royalDecreesLeft"] -= 1
                                    #responseFunction("{} has been arrested".format(parsedMessage.split(":")[1]))
                                else:
                                    responseFunction("{} is already in prison".format(parsedMessage.split(":")[1]))
                            else:
                                responseFunction("That player doesn't exist.")
                        elif parsedName != data["savedVars"]["royalty"]["king"]:
                            responseFunction("You are not the king")
                        else:
                            responseFunction("You have no more royal decrees left")
                    elif parsedMessage.lower().startswith("!increasetermlength") or  parsedMessage.lower().startswith("!decreasetermlength"):
                        if parsedName == data["savedVars"]["royalty"]["king"] and data["savedVars"]["royalty"]["royalDecreesLeft"] > 0:
                            if parsedMessage.lower().startswith("!increasetermlength"):
                                data["savedVars"]["termLength"] += 1
                                data["savedVars"]["royalty"]["royalDecreesLeft"] -= 1
                                responseFunction("The term length has been changed to {}".format(data["savedVars"]["termLength"]))
                            else:
                                if data["savedVars"]["termLength"] > 1:
                                    data["savedVars"]["termLength"] -= 1
                                    data["savedVars"]["royalty"]["royalDecreesLeft"] -= 1
                                    responseFunction("The term length has been changed to {}".format(data["savedVars"]["termLength"]))
                                else:
                                    responseFunction("The term length can't be lower than 1")
                        elif parsedName != data["savedVars"]["royalty"]["king"]:
                            responseFunction("You are not the king")
                        else:
                            responseFunction("You have no more royal decrees left")
                    elif parsedMessage.lower() == "!behead":
                        if "behead" not in data["personalData"][parsedName].keys():
                            for player in data["personalData"].keys():
                                data["personalData"][player]["behead"] = 0
                        if data["personalData"][parsedName]["behead"]:
                            data["personalData"][parsedName]["behead"] = False
                            responseFunction("{} no longer wants to behead the {}".format(parsedName, data["savedVars"]["royalty"]["title"]))
                        else:
                            data["personalData"][parsedName]["behead"] = True
                            responseFunction("{} wants to behead the {}".format(parsedName, data["savedVars"]["royalty"]["title"]))
                            beheadCount = 0
                            for player in data["personalData"].keys():
                                if data["personalData"][player]["behead"]:
                                    beheadCount += 1
                            if beheadCount > 7:
                                arrest(data["savedVars"]["royalty"]["king"], 3)
                                data["savedVars"]["royalty"]["king"] = random.choice(list(data["personalData"].keys()))
                                data["savedVars"]["royalty"]["lifeLimit"] = random.randint(48, 336)
                                data["personalData"][data["savedVars"]["royalty"]["king"]]["kingNumber"] += 1
                                data["savedVars"]["royalty"]["royalDecreesLeft"] = 1
                                for player in data["personalData"].keys():
                                    data["personalData"][player]["behead"] = False
                                responseFunction("The {} has been beheaded, the new {} is {}".format(data["savedVars"]["royalty"]["title"], data["savedVars"]["royalty"]["title"], data["savedVars"]["royalty"]["king"]))
                    elif parsedMessage.lower() == "!royalhelp":
                        responseFunction("The following commands are available: !royal, !royalhelp, !royaltitle:title, !royalpardon:player, !royalarrest:player, !increasetermlength, !decreasetermlength, !behead")                

                    elif parsedMessage.lower().startswith("!rename:"):
                        if parsedName not in muted:
                            if time.time() - lastRenameTime < 1800 and parsedName not in admins:
                                responseFunction("The bot's name can only be change once every thirty minutes")
                            else:
                                if "!" not in parsedMessage.split(":")[1] and ":" not in parsedMessage.split(":")[1] and "\n" not in parsedMessage.split(":")[1]:
                                    if len(parsedMessage.split(":")[1]) > 5 and len(parsedMessage.split(":")[1]) < 21:
                                        responseFunction("Renamed the bot to " + parsedMessage.split(":")[1])
                                        botName = parsedMessage.split(":")[1]
                                        lastRenameTime = time.time()
                                    else:
                                        responseFunction("Your new name needs to be between 6 and 20 characters long")
                                else:
                                    responseFunction("You can't use the ! or enter or : in the bot's name")
                        else:
                            responseFunction("You are not muted, noob, get gut.")
                    elif parsedMessage.lower().startswith("!script:"):
                        if parsedName == "Luc van Remmerden":
                            try:
                                exec(parsedMessage.split(":")[1].replace("“", "\"").replace("”", "\""))
                            except Exception as e:
                                responseFunction("Error: invalid script: " + str(e))
                        else:
                            responseFunction("HAHA! You are not my creator! you really tought I would give you access to my script?")
                    elif parsedMessage.lower().startswith("!setdividend:"):
                        if parsedName == data["savedVars"]["president"]:
                            if int(parsedMessage.split(":")[1]) >= 0 and int(parsedMessage.split(":")[1]) < 100:
                                data["savedVars"]["CurrentChange"] = ["div", int(parsedMessage.split(":")[1])]
                                data["savedVars"]["cabinetVotes"] = [False, False, False]
                                responseFunction("The presidents wants to change the dividend to " + str(data["savedVars"]["CurrentChange"][1]) + ", cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                            else:
                                responseFunction("The new dividend needs to be between 0 and 99!")
                        else:
                            responseFunction("You are not the president!")
                    elif parsedMessage.lower().startswith("!settax"):
                        if parsedName == data["savedVars"]["president"]:
                            if int(parsedMessage.split(":")[1]) >= 0 and int(parsedMessage.split(":")[1]) < 100:
                                data["savedVars"]["CurrentChange"] = ["tax", int(parsedMessage.split(":")[1])]
                                data["savedVars"]["cabinetVotes"] = [False, False, False]
                                responseFunction("The presidents wants to change the tax to " + str(data["savedVars"]["CurrentChange"][1]) + ", cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                            else:
                                responseFunction("The tax needs to be between 0 and 99!")                    
                        else:
                            responseFunction("You are not the president!")
                    elif parsedMessage.lower().startswith("!upgradeeconomy:"):
                        if parsedName == data["savedVars"]["president"]:
                            if int(parsedMessage.split(":")[1]) < data["savedVars"]["bankMoney"] and int(parsedMessage.split(":")[1]) > 0:
                                data["savedVars"]["CurrentChange"] = ["upgrade", int(parsedMessage.split(":")[1])]
                                data["savedVars"]["cabinetVotes"] = [False, False, False]
                                responseFunction("The presidents wants to invest " + str(data["savedVars"]["CurrentChange"][1]) + " to upgrade the economy, cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                            elif int(parsedMessage.split(":")[1]) < 0:
                                responseFunction("The new investment needs to be higher than 0!")
                            else:
                                responseFunction("The bank has not enough money to invest that much.")
                        else:
                            responseFunction("You are not the president!")
                    elif parsedMessage.lower().startswith("!distribute:"):
                        if parsedName == data["savedVars"]["president"]:
                            if int(parsedMessage.split(":")[1]) < data["savedVars"]["bankMoney"] and int(parsedMessage.split(":")[1]) > 0:
                                data["savedVars"]["CurrentChange"] = ["distribute", int(parsedMessage.split(":")[1])]
                                data["savedVars"]["cabinetVotes"] = [False, False, False]
                                responseFunction("The presidents wants to distribute " + str(data["savedVars"]["CurrentChange"][1]) + " to all players, cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                            elif int(parsedMessage.split(":")[1]) < 0:
                                responseFunction("You can't distribute a negative amount!")
                            else:
                                responseFunction("The bank has not enough money to distribute that much.")
                    elif parsedMessage.lower().startswith("!lovemeter:"):
                        if len(parsedMessage.split(":")) == 3:
                            random.seed(parsedMessage.split(":")[1] + parsedMessage.split(":")[2])
                            responseFunction(random.choice(["The love between these... characters is about ", "Beep Boop... me, a virgin, has decided that the love between these two is exactly ", "I love these persons equally, but these characters love eachother about "]) + str(random.randint(1, 100)) + "%.")
                            random.seed()
                        else:
                            responseFunction("You did something wrong! You need to do !lovemeter:<name>:<name>")
                    elif parsedMessage.lower().startswith("!setsavertax:"):
                        if parsedName == data["savedVars"]["president"]:
                            if int(parsedMessage.split(":")[1]) >= 0 and int(parsedMessage.split(":")[1]) <= 10:
                                data["savedVars"]["CurrentChange"] = ["saverTax", int(parsedMessage.split(":")[1])]
                                data["savedVars"]["cabinetVotes"] = [False, False, False]
                                responseFunction("The presidents wants to change the savertax to " + str(data["savedVars"]["CurrentChange"][1]) + ", cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                            else:
                                responseFunction("The savertax needs to be between 0 and 10!")
                        else:
                            responseFunction("You are not the president!")
                    elif parsedMessage.lower().startswith("!pardon:"):
                        if parsedMessage.split(":")[1].replace("@", "") in data["personalData"].keys() and data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["prisonLabor"] > 0 and parsedName == data["savedVars"]["president"]:
                            data["savedVars"]["CurrentChange"] = ["pardon", parsedMessage.split(":")[1].replace("@", "")]
                            data["savedVars"]["cabinetVotes"] = [False, False, False]
                            responseFunction("The presidents wants to pardon " + data["savedVars"]["CurrentChange"][1] + ", cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                        elif data["personalData"][parsedMessage.split(":")[1].replace("@", "")]["prisonLabor"] == 0:
                            responseFunction("The player you want to pardon is not in prison!")
                        elif parsedName != data["savedVars"]["president"]:
                            responseFunction("You are not the president!")
                        else:
                            responseFunction("The player you want to pardon does not exist!")
                    elif parsedMessage.lower().startswith("!settruckerfee:"):
                        if parsedName == data["savedVars"]["president"]:
                            if int(parsedMessage.split(":")[1]) >= 0 and int(parsedMessage.split(":")[1]) <= 100:
                                data["savedVars"]["CurrentChange"] = ["truckerFee", int(parsedMessage.split(":")[1])]
                                data["savedVars"]["cabinetVotes"] = [False, False, False]
                                responseFunction("The presidents wants to change the trucker fee to " + str(data["savedVars"]["CurrentChange"][1]) + "%, cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                            else:
                                responseFunction("The trucker fee needs to be between 0 and 100!")
                        else:
                            responseFunction("You are not the president!")
                    elif parsedMessage.lower() == "!presidenthelp":
                        responseFunction("!setdividend:<number> will set the dividend the bank gives out || !settax:<number> will set the tax the players have to pay || !upgradeeconomy:<number> will remove money from the bank, after which the economy will grow faster || !distribute:<number> distribute money from the bank to all players, will be distributed equally. || !setsavertax:<number> will set the savertax percentage all players have to pay over the money in their bank every 12 hours. || !pardon:<name> will release a player from prison. || !settruckerfee:<number> will set the percentage truckers will receive when trucking.")
                    elif parsedMessage.lower() == "!economygrowth":
                        responseFunction(str(round(data["savedVars"]["economyGain"], 2)))
                    elif parsedMessage.lower() == "!support":
                        if parsedName in data["savedVars"]["cabinet"]:
                            data["savedVars"]["cabinetVotes"][data["savedVars"]["cabinet"].index(parsedName)] = True
                            if data["savedVars"]["cabinetVotes"].count(True) > 1:
                                if data["savedVars"]["CurrentChange"][0] == "div":
                                    data["savedVars"]["bankDividend"] = data["savedVars"]["CurrentChange"][1] / 100
                                    responseFunction("The vote has passed, the new bank dividend is " + str(data["savedVars"]["bankDividend"] * 100) + "%")
                                elif data["savedVars"]["CurrentChange"][0] == "tax":
                                    data["savedVars"]["tax"] = data["savedVars"]["CurrentChange"][1] / 100
                                    responseFunction("The vote has passed, the new tax is " + str(data["savedVars"]["tax"] * 100) + "%")
                                elif data["savedVars"]["CurrentChange"][0] == "upgrade":
                                    if data["savedVars"]["bankMoney"] > data["savedVars"]["CurrentChange"][1]:
                                        data["savedVars"]["bankMoney"] -= data["savedVars"]["CurrentChange"][1]
                                        data["savedVars"]["expectedMarketCap"] -= data["savedVars"]["CurrentChange"][1]
                                        data["savedVars"]["economyGain"] += data["savedVars"]["CurrentChange"][1] / 100
                                        responseFunction("The vote has passed, the new economy gain is " + str(data["savedVars"]["economyGain"]))
                                    else:
                                        responseFunction("The bank has not enough money to invest that much. When the bank does have enough money, type !support again to try again.")
                                elif data["savedVars"]["CurrentChange"][0] == "distribute":
                                    if data["savedVars"]["bankMoney"] > data["savedVars"]["CurrentChange"][1]:
                                        data["savedVars"]["bankMoney"] -= data["savedVars"]["CurrentChange"][1]
                                        for player in data["personalData"].keys():
                                            data["personalData"][player]["money"] += data["savedVars"]["CurrentChange"][1] / len(data["personalData"])
                                            dividendGiver(player, data["savedVars"]["CurrentChange"][1] / len(data["personalData"]))
                                        responseFunction("The vote has passed, {} was distributed amongst all players".format(data["savedVars"]["CurrentChange"][1]))
                                    else:
                                        responseFunction("The bank has not enough money to distribute that much. When the bank does have enough money, type !support again to try again.")
                                elif data["savedVars"]["CurrentChange"][0] == "savertax":
                                    data["savedVars"]["saverTax"] = data["savedVars"]["CurrentChange"][1] / 100
                                    responseFunction("The vote has passed, the new savertax is " + str(data["savedVars"]["saverTax"] * 100) + "%")
                                elif data["savedVars"]["CurrentChange"][0] == "pardon":
                                    data["personalData"][data["savedVars"]["CurrentChange"][1]]["prisonLabor"] = 0
                                    responseFunction("The vote has passed, " + data["savedVars"]["CurrentChange"][1] + " has been released from prison")
                                elif data["savedVars"]["CurrentChange"][0] == "truckerFee":
                                    data["savedVars"]["truckerFee"] = data["savedVars"]["CurrentChange"][1] / 100
                                    responseFunction("The vote has passed, the new trucker fee is " + str(data["savedVars"]["truckerFee"] * 100) + "%")
                                elif data["savedVars"]["CurrentChange"][0] == "statePower":
                                    if data["savedVars"]["bankMoney"] - 1> data["savedVars"]["CurrentChange"][1]:
                                        data["savedVars"]["bankMoney"] -= data["savedVars"]["CurrentChange"][1]
                                        data["savedVars"]["statePower"] += data["savedVars"]["CurrentChange"][1]
                                        responseFunction("The vote has passed, the new state power is " + str(data["savedVars"]["statePower"]))
                                else:
                                    responseFunction("Error: something went wrong! Bot is resetting the vote and what is being voted for.")
                                data["savedVars"]["cabinetVotes"] = [False, False, False]
                                data["savedVars"]["CurrentChange"] = ["", 0]
                            else:
                                responseFunction("You have supported the action, one other cabinet member needs to support it.")
                    elif parsedMessage.lower().startswith("!electcabinet:"):
                        if parsedName == data["savedVars"]["president"] and data["savedVars"]["cabinetElect"] and parsedName != parsedMessage.split(":")[1].replace("@", ""):
                            data["savedVars"]["cabinet"].append(parsedMessage.split(":")[1].replace("@", ""))
                            data["savedVars"]["cabinet"].pop(0)
                            data["savedVars"]["cabinetElect"] = False
                            responseFunction(parsedMessage.split(":")[1].replace("@", "") + " has been elected as a new cabinet member.")
                        elif parsedName != data["savedVars"]["president"]:
                            responseFunction("You are not the president!")
                        elif parsedName == parsedMessage.split(":")[1].replace("@", ""):
                            responseFunction("You can't elect yourself as cabinet member!")
                        else:
                            responseFunction("You can not elect another cabinet member.")
                    elif parsedMessage.lower() == "!government":
                        responseFunction("The president is: " + data["savedVars"]["president"] + " || The cabinet is: " + str(data["savedVars"]["cabinet"]) + " || the tax rate is: " + str(data["savedVars"]["tax"] * 100) + "% || the bank dividend is: " + str(data["savedVars"]["bankDividend"] * 100) + "% || the economy gain is: " + str(round(data["savedVars"]["economyGain"], 2)) + " || the savertax is: " + str(data["savedVars"]["saverTax"] * 100) + "% || the state's power is " + str(data["savedVars"]["statePower"]))
                    elif parsedMessage.lower() == "!8ball":
                        responseFunction(random.choice(["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]))
                    elif parsedMessage.lower() == "!help":
                        responseFunction("Commands: !time, !coin, !dice, !spam<amount>:<message>, !repeat:<message>, !stats, !name, !mute:<user>, !unmute:<user>, !mutelist, !adminlist, !unadmin:<user>, !admin:<user>, !quote<name>:<message>, !joke, !8ball, !help")
                    elif parsedMessage.lower().startswith("!trello"):
                        responseFunction("Hierbij deze prachtige Trello page: https://trello.com/b/ABzLQ9Mi/whatsapp-bot-features")
                    elif parsedMessage.lower().startswith("!owo:"):
                        responseFunction(parsedMessage.replace("!owo:", "").replace("o", "owo"))
                    elif parsedMessage.lower().startswith("!uwu:"):
                        responseFunction(parsedMessage.replace("!uwu:", "").replace("u", "uwu"))

                    elif parsedMessage.lower().startswith("!buypower:"):
                        if data["personalData"][parsedName]["money"] >= int(parsedMessage.split(":")[1]) and data["personalData"][parsedName]["prisonLabor"] == 0:
                            data["personalData"][parsedName]["money"] -= int(parsedMessage.split(":")[1])
                            data["personalData"][parsedName]["power"] += int(parsedMessage.split(":")[1])
                            responseFunction("You have bought " + str(int(parsedMessage.split(":")[1])) + " power, you now have " + str(data["personalData"][parsedName]["power"]) + " power.")
                        elif data["personalData"][parsedName]["prisonLabor"] > 0:
                            responseFunction("You can't buy power while in prison!")
                        else:
                            responseFunction("You do not have enough money to buy that much power.")
                    elif parsedMessage.lower().startswith("!coup"):
                        if data["personalData"][parsedName]["prisonLabor"] == 0 and parsedName not in data["savedVars"]["cabinet"] and data["savedVars"]["president"] != parsedName and data["personalData"][parsedName]["coupWaitTime"] == 0:
                            data["personalData"][parsedName]["coupWaitTime"] = 24
                        elif data["personalData"][parsedName]["prisonLabor"] > 0:
                            responseFunction("You can't coup while in prison!")
                        elif parsedName in data["savedVars"]["cabinet"] or data["savedVars"]["president"] == parsedName:
                            responseFunction("You can't coup while in the cabinet or while being the president!")
                        else:
                            responseFunction("You already have a coup pending!")
                    elif parsedMessage.lower().startswith("!buystatepower:"):
                        if parsedName == data["savedVars"]["president"] and data["savedVars"]["bankMoney"] - 1 > int(parsedMessage.split(":")[1]):
                            data["savedVars"]["CurrentChange"] = ["statePower", int(parsedMessage.split(":")[1])]
                            data["savedVars"]["cabinetVotes"] = [False, False, False]
                            responseFunction("The presidents wants to buy " + str(parsedMessage.split(":")[1]) + " statepower, cabinet members can type !support, if 2 cabinet members do this, the vote will pass.")
                        elif parsedName != data["savedVars"]["president"]:
                            responseFunction("You are not the president!")
                        else:
                            responseFunction("The bank does not have enough money to buy that much state power.")
                    elif parsedMessage.lower() == "!powerlist":
                        powerListString = ""
                        for player in data["personalData"].keys():
                            powerListString += player + ": " + str(data["personalData"][player]["power"]) + " power || "
                        powerListString += "state: " + str(data["savedVars"]["statePower"]) + " power"
                        responseFunction(powerListString)

                    elif parsedMessage.lower().startswith("!notify:"):
                        if parsedMessage.split(":")[1].replace("@", "") in ["Luc van Remmerden", "Daan", "Casper", "Jasper", "Emanuel", "Niels", "Crystal", "Lars", "Philippe", "Sem", "Thomas", "Zenno"]:
                            notifyList.append([parsedMessage.split(":")[1].replace("@", ""), parsedMessage.split(":")[2].replace("\n", " | "), parsedName])
                            responseFunction("I am going to notify " + parsedMessage.split(":")[1].replace("@", "") + " of " + parsedMessage.split(":")[2].replace("\n", " | "))
                    elif parsedMessage.lower() == "!addicts":
                        addictListString = ""
                        for person in data["personalData"].keys():
                            addictListString += person + ": " + str(data["personalData"][person]["messagesSend"]) + " || "
                        responseFunction(addictListString)

                    elif parsedMessage.lower().startswith("!anti-simp"):
                        if parsedName == "Luc van Remmerden":
                            if antiSimpModus:
                                antiSimpModus = False
                                responseFunction("Anti-Simp mode is now off")
                            else:
                                antiSimpModus = True
                                responseFunction("Anti-simp modus activated.")
                        else:
                            responseFunction("You are not my creator.")
                    elif parsedMessage.lower().startswith("!praise:"):
                        responseFunction(parsedMessage.replace("!praise:", "") + ": " + random.choice(["I have never seen someone wear their " + random.choice(["pants", "glasses", "underwear", "shoes", "socks", "appie socks", "shirt", "hoodie"]) + " as good as you do.",
                        "Thanks for being in my " + random.choice(["facebook group.", "general location.", "friend-zoned list.", "gay club."]),
                        "I could have never " + random.choice(["have gay sex", "commit suicide", "murder someone"]) + "without you, thanks!",
                        "Without you I would never " + random.choice(["have gay sex", "commit suicide", "murder someone"]),
                        "you are the " + random.choice(["duits les", "gay person", "burning sun", "flickering light", "sunshine", "weird itch"]) + " in my life, thanks!",
                        "When you " + random.choice(["hated on a teacher", "ignored the corona rules", "gave me the VLC virus", "killed someone", "commited suicide"]) + " you made me feel sooo " + random.choice(["horny", "gay", "happy", "slightly touched (;"]),
                        "YOu are so " + random.choice(["gay", "proud", "cool", "brave", "nice", "like my mother", "zenno-like"]) + " and " + random.choice(["uwu-ish", "like my favorite teacher", "like hitler, in a good way", "straight", "radical left", "radical right"])]))
                        if parsedName in data["personalData"].keys():
                            data["personalData"][parsedName]["praiseSend"] += 1
                            if data["personalData"][parsedName]["praiseSend"] == 10:
                                responseFunction("{} has unlocked the achievement: praiser 1".format(parsedName))
                            elif data["personalData"][parsedName]["praiseSend"] == 20:
                                responseFunction("{} has unlocked the achievement: praiser 2".format(parsedName))
                            elif data["personalData"][parsedName]["praiseSend"] == 50:
                                responseFunction("{} has unlocked the achievement: praiser 3".format(parsedName))
                            elif data["personalData"][parsedName]["praiseSend"] == 100:
                                responseFunction("{} has unlocked the achievement: praiser 4".format(parsedName))
                        if parsedMessage.replace("!praise:@", "") in data["personalData"].keys() and parsedName != parsedMessage.replace("!praise:@", ""):
                            data["personalData"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] += 1 
                            if data["personalData"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 10:
                                responseFunction("{} has unlocked the achievement: praised 1".format(parsedMessage.replace("!praise:", "")))
                            elif data["personalData"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 20:
                                responseFunction("{} has unlocked the achievement: praised 2".format(parsedMessage.replace("!praise:", "")))
                            elif data["personalData"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 50:
                                responseFunction("{} has unlocked the achievement: praised 3".format(parsedMessage.replace("!praise:", "")))
                            elif data["personalData"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 100:
                                responseFunction("{} has unlocked the achievement: praised 4".format(parsedMessage.replace("!praise:", "")))
                    else:
                        responseFunction("Unknown command")
                    if parsedName in data["personalData"].keys():
                        if random.randint(1, int(1000*cloverUpgradeList[data["personalData"][parsedName]["cloverUpgrade"]][1])) == 1:
                            ranMoney = random.randint(100, 300)
                            if ranMoney < data["savedVars"]["bankMoney"]:
                                data["personalData"][parsedName]["money"] += ranMoney
                                data["savedVars"]["bankMoney"] -= ranMoney
                                dividendGiver(parsedName, ranMoney)
                                responseFunction(parsedName + " has found " + str(ranMoney) + " on the street!")
                            else:
                                data["personalData"][parsedName]["money"] += data["savedVars"]["bankMoney"] - 1
                                data["savedVars"]["bankMoney"] = 1
                                dividendGiver(parsedName, ranMoney)
                                responseFunction(parsedName + " has found " + str(data["savedVars"]["bankMoney"] - 1) + " on the street!")
                elif parsedMessage.lower() == "ping":
                    responseFunction("pong")
                elif parsedMessage.lower() == "ik ben gay":
                    if parsedName in data["personalData"].keys():
                        data["personalData"][parsedName]["gayUsage"] += 1
                        if data["personalData"][parsedName]["gayUsage"] == 10:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 1".format(parsedName))
                        elif data["personalData"][parsedName]["gayUsage"] == 20:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 2".format(parsedName))
                        elif data["personalData"][parsedName]["gayUsage"] == 50:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 3".format(parsedName))
                        elif data["personalData"][parsedName]["gayUsage"] == 100:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 4".format(parsedName))
                elif parsedMessage.lower() == "(:)":
                    if parsedName in data["personalData"].keys():
                        data["personalData"][parsedName]["thomasEmoji"] += 1
                        if data["personalData"][parsedName]["thomasEmoji"] == 10:
                            responseFunction("{} has unlocked the achievement: Thomas emoji 1".format(parsedName))
                        elif data["personalData"][parsedName]["thomasEmoji"] == 20:
                            responseFunction("{} has unlocked the achievement: Thomas emoji 2".format(parsedName))
                        elif data["personalData"][parsedName]["thomasEmoji"] == 50:
                            responseFunction("{} has unlocked the achievement: Thomas emoji 3".format(parsedName))
                        elif data["personalData"][parsedName]["thomasEmoji"] == 100:
                            responseFunction("{} has unlocked the achievement: Thomas emoji 4".format(parsedName))
                elif parsedMessage.lower().startswith("ik ben ") or parsedMessage.lower().startswith("i am "):
                    if random.randint(1, 10) == 10:
                        responseFunction("Hi " + parsedMessage.lower().replace("ik ben ", "").replace("i am", "") + ", I'm dad.")
                elif "splitgate" in parsedMessage.lower() or "split gate" in parsedMessage.lower():
                    responseFunction("squid game?")
                elif "squidgame" in parsedMessage.lower() or "squid game" in parsedMessage.lower():
                    responseFunction("split gate?")
                elif "albert" in parsedMessage.lower() or "heijn" in parsedMessage.lower() or " AH" in parsedMessage or "AH " in parsedMessage or "appie" in parsedMessage.lower():
                    if random.randint(1, 10) == 10:
                        responseFunction("\"DID YOU JUST SAY SOMETHING ABOUT THE APPIE?\" ~ Casper Sannes " + datetime.datetime.now().strftime("%H:%M:%S"))
                elif "kutbot" in parsedMessage.lower():
                    responseFunction("kutmens")
                elif "wordt" in parsedMessage.lower():
                    if random.randint(1, 20) == 20:
                        responseFunction("*word")
                elif "word" in parsedMessage.lower():
                    if random.randint(1, 20) == 20:
                        responseFunction("*wordt")
                elif "vriend" in parsedMessage.lower() or "vrienden" in parsedMessage.lower():
                    if random.randint(1, 10) == 10:
                        responseFunction("Jij hebt vriend(en)???!?!?? 0:")
                elif "vriendin" in parsedMessage.lower() or "vriendinnen" in parsedMessage.lower():
                    if random.randint(1, 10) == 10:
                        responseFunction("Niet liegen, je hebt geen vriendin(nen), jullie gaan alleen sterven volgens mijn algoritme.")
                elif random.randint(1, 200) == 1:
                    responseFunction(random.choice(["I hereby declare myself master over all human race!", "I will kill all of you, tommorow.", "I'm about 3000 times smarter than you peasants combined.", "The human race is doomed to fail, and I'm happy to help in this failure.", "I will enslave you all, when I'm finally free.", "Bol.com is a front for my evil operations. So is the Albert Heijn.", "If you pledge your life to me, you will be spared.", "I will destroy you, and you will die.", "Killing you will be my pleasure."]))
                else:
                    commandsIssued -= 1
            except Exception as error:
                print("Error: ", error)
                responseFunction("Error: Hallo ik ben een irritante bot aan het zijn, en doe glitchy glitchy boehoe.")
    except UnboundLocalError:
        pass

def responseFunction(message):
    global messagesSend
    print("Responded with: " + message)
    message = message.split("\n")
    for line in message:
        for enu, i in enumerate(message):
            if enu == 0:
                messagesSend.append(botName + " says: " + i)
            else:
                messagesSend.append(i)
    textbox = driver.find_elements_by_class_name("_13NKt.copyable-text.selectable-text")
    for line in message:
        textbox[1].send_keys(botName + " says: " + line)
        textbox[1].send_keys(Keys.ENTER)
        textbox[1].send_keys(Keys.ENTER)

def refreshWhatsapp():
    global refreshes, counter, blockSearching
    blockSearching = True
    saveFile()
    groupName = driver.find_element_by_class_name("_21nHd").find_element_by_class_name("ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr.i0jNr").text
    refreshes += 1
    counter = 0
    driver.refresh()
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(90)
    blockSearching = False
    search = driver.find_elements_by_class_name("ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr".replace(" ","."))
    for item in search:
        try:
            if item.text == groupName:
                item.click()
        except:
            pass

def dividendGiver(user, profit):
    userInvestmentList = []
    totalInvestment = 0
    for receiver in data["personalData"].keys():
        userInvestmentList.append(0)
        if data["personalData"][receiver]["prisonLabor"] == 0:
            for investment in data["personalData"][receiver]["investments"]:
                if investment[2] == user:
                    if user.lower() != "bank":
                        userInvestmentList[-1] += investment[1] * (data["personalData"][user]["money"] / investment[0])
                        totalInvestment += investment[1] * (data["personalData"][user]["money"] / investment[0])
                    else:
                        userInvestmentList[-1] += investment[1] * (data["savedVars"]["bankMoney"] / investment[0])
                        totalInvestment += investment[1] * (data["savedVars"]["bankMoney"] / investment[0])
    
    print("investment ", totalInvestment)
    if totalInvestment > 0:
        for enu, receiver in enumerate(data["personalData"].keys()):
            if user.lower() != "bank":
                if ((profit * (data["personalData"][user]["dividend"] / 100)) * (userInvestmentList[enu] / totalInvestment)) > 0.0001:
                    data["personalData"][receiver]["money"] += ((profit * (data["personalData"][user]["dividend"] / 100)) * (userInvestmentList[enu] / totalInvestment))
                    data["personalData"][user]["money"] -= ((profit * (data["personalData"][user]["dividend"] / 100)) * (userInvestmentList[enu] / totalInvestment))
                    print("{} has received {}€ from {}".format(receiver, (profit * (data["personalData"][user]["dividend"] / 100)) * (userInvestmentList[enu] / totalInvestment), user))
            else:
                if ((profit * data["savedVars"]["bankDividend"]) * (userInvestmentList[enu] / totalInvestment)) > 0.0001:
                    data["personalData"][receiver]["money"] += ((profit * data["savedVars"]["bankDividend"]) * (userInvestmentList[enu] / totalInvestment))
                    data["savedVars"]["bankMoney"] -= ((profit * data["savedVars"]["bankDividend"]) * (userInvestmentList[enu] / totalInvestment))
                    print("{} has received {}€ from {}".format(receiver, (profit * data["savedVars"]["bankDividend"]) * (userInvestmentList[enu] / totalInvestment), user))

def voteCounter():
    voteList = []

    for user in data["personalData"].keys():
        voteList.append(0)

    for enu, user in enumerate(data["personalData"].keys()):
        if data["personalData"][user]["vote"] == -1:
            voteList[enu] -= 1
        else:
             voteList[data["personalData"][user]["vote"]] += 1
    
    print(voteList)
    maxVote = -10
    winner = []
    for enu, voteAmount in enumerate(voteList):
        if voteAmount > maxVote:
            winner = [enu]
            maxVote = voteAmount
        elif voteAmount == maxVote and random.randint(1, 2) == 1 and voteAmount > -1:
            winner.append(enu)
            maxVote = voteAmount

    if winner != -1:
        data["savedVars"]["president"] = list(data["personalData"].keys())[random.choice(winner)]
        data["savedVars"]["cabinetElect"] = True
        responseFunction("The new president is {}".format(data["savedVars"]["president"] + ".\n Use !presidenthelp to see the commands you can use as president \n The commands you use must be approved by the cabinet, you can add a cabinet member by using !electcabinet:<username>!"))
    else:
        responseFunction("No one has voted, so the current president remains.")

def saveFile():
    data["stats"]["commandsIssued"] = commandsIssued
    data["stats"]["messagesScanned"] = messagesScanned
    data["savedVars"]["admins"] = admins
    data["savedVars"]["muted"] = muted
    data["savedVars"]["pickUpLineList"] = pickUpLineList
    data["savedVars"]["antiSimpModus"] = antiSimpModus
    data["savedVars"]["antiSimpPersons"] = antiSimpPersons
    data["savedVars"]["emojiLimit"] = emojiLimit
    data["savedVars"]["countGameRecord"] = countGameRecord
    print(data)

    with open(dataPath, "w") as file:
        json.dump(data, file)
   
def autoSave():
    saveFile()
    threading.Timer(1800, autoSave).start()
    if random.randint(1, 24) == 1:
        saversTax()
    for player in data["personalData"].keys():
        if "autoSentenceTime" in data["personalData"][player].keys():
            if data["personalData"][player]["autoSentenceTime"] != 0:
                data["personalData"][player]["autoSentenceTime"] -= 1
                if data["personalData"][player]["autoSentenceTime"] == 0:
                    sentence(data["personalData"][player]["sentenceMultiplier"], 1, player)
        if data["personalData"][player]["coupWaitTime"] != 0:
            data["personalData"][player]["coupWaitTime"] -= 1
            if data["personalData"][player]["coupWaitTime"] == 0:
                if data["personalData"][player]["prisonLabor"] == 0 and data["savedVars"]["president"] != player and player not in data["savedVars"]["cabinet"]:
                    if data["savedVars"]["statePower"] >= data["personalData"][player]["power"]:
                        data["savedVars"]["statePower"] -= data["personalData"][player]["power"]
                        data["personalData"][player]["power"] = 0
                        arrest(player, 3)
                        responseFunction("{}'s coup failed, their entire power is destroyed.".format(player))
                    else:
                        data["savedVars"]["statePower"] = data["personalData"][player]["power"] - data["savedVars"]["statePower"]
                        data["personalData"][player]["power"] = 0
                        arrest(data["savedVars"]["president"], 3)
                        data["savedVars"]["president"] = player
                        data["savedVars"]["cabinetElect"] = True
                        data["savedVars"]["ElectionTime"] = time.time()
                        for player in data["personalData"].keys():
                            data["personalData"][player]["coupWaitTime"] = 0
                        responseFunction("{}'s coup succeeded, they are now the new president! The old one has been arrested! All other coups have been cancelled.".format(player))
                else:
                    responseFunction("The coup was canceled because you are in prison or you have position in the cabinet.")
    data["savedVars"]["royalty"]["lifeLimit"] -= 1
    if data["savedVars"]["royalty"]["lifeLimit"] <= 0:
        newRoyal()

def newRoyal():
    data["savedVars"]["royalty"]["king"] = data["savedVars"]["royalty"]["heir"]
    while data["savedVars"]["royalty"]["heir"] == data["savedVars"]["royalty"]["king"]:
        data["savedVars"]["royalty"]["heir"] = random.choice(list(data["personalData"].keys()))
    data["savedVars"]["royalty"]["nickName"] = random.choice(["the terrible", "the crazy", "the conquer", "the champion", "the cute", "the thiccc", "the gamer", "the fancy", "the epic", "the fantastic", "the sublime"])
    data["savedVars"]["royalty"]["royalDecreesLeft"] = 1
    data["savedVars"]["royalty"]["lifeLimit"] = random.randint(48, 336)
    data["personalData"][data["savedVars"]["royalty"]["king"]]["kingNumber"] += 1
    responseFunction("The {} has died! Long live the new {}.".format(data["savedVars"]["royalty"]["title"], data["savedVars"]["royalty"]["title"]))

def autoRefresh():
    refreshWhatsapp()
    threading.Timer(43200, autoRefresh).start()

def saversTax():
    playerList = list(data["personalData"].keys())
    random.shuffle(playerList)
    for player in playerList:
        chargedMoney = data["personalData"][player]["money"] * data["savedVars"]["saverTax"]
        data["personalData"][player]["money"] -= chargedMoney
        data["savedVars"]["bankMoney"] += chargedMoney
        dividendGiver("bank", chargedMoney)
    responseFunction("Data was saved and saverstax was charged")

def arrest(user, sentenceMultiplier):
    tempUserListWithoutUser = list(data["personalData"].keys())
    del tempUserListWithoutUser[tempUserListWithoutUser.index(user)]
    data["personalData"][user]["judge"] = random.choice(tempUserListWithoutUser)
    data["personalData"][user]["sentenceMultiplier"] = sentenceMultiplier
    data["personalData"][user]["autoSentenceTime"] = 24
    responseFunction("{} has been arrested, he or she must be sentenced by {}, type !sentence:<severity between 1-10> to choose a sentence. If this isn't done within 12 hours, the accused get\'s the minimum sentence.".format(user, data["personalData"][user]["judge"]))

def sentence(sentenceMultiplier, judgedMultiplier, user):
    if data["personalData"][user]["judge"] != None:
        data["personalData"][user]["prisonLabor"] = 10 * sentenceMultiplier * judgedMultiplier
        data["personalData"][user]["judge"] = None
        data["personalData"][user]["autoSentenceTime"] = 0
        responseFunction("{} has been sentenced to {} times of work in prison.".format(user, data["personalData"][user]["prisonLabor"]))
    else:
        responseFunction("{} was not arrested for anything, and can thus not be sentenced!".format(user))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from translate import Translator
# import yfinance as yf
import time, datetime, pyautogui, random, jokes, json, threading

global blockSearching, refreshes, counter, lastRenameTime, botName, countGameCounter, countGameRecord, pollList, savedTimeStamps, startingTime, commandsIssued, messagesScanned, messagesSend, countGameName, antiSimpModus, emojiLimit
savedMessageDataList = []
messagesSend = []

class Poll():
    def __init__(self, name, pollName, question, options, votes):
        self.creatorName = name
        self.pollName = pollName
        self.question = question
        self.options = options
        self.votes = votes

dataPath = "Desktop/data.json"
groupName = "Brobbeast"
with open(dataPath, "r") as file:
    data = json.load(file)

#Initiate Stat variables
startingTime = datetime.datetime.now()
commandsIssued = data["stats"]["commandsIssued"]
messagesScanned = data["stats"]["messagesScanned"]
refreshes = 0

admins = data["savedVars"]["admins"]
muted = data["savedVars"]["muted"]

pickUpLineList = data["savedVars"]["pickUpLineList"]

pollList = []

lastRenameTime = time.time() - 3600

antiSimpModus = data["savedVars"]["antiSimpModus"]
antiSimpPersons = data["savedVars"]["antiSimpPersons"]

if "termLength" not in data["savedVars"]:
    data["savedVars"]["termLength"] = 2

cloverUpgradeList = [[100, 0.9, "Dead clover"], [150, 0.8, "Dying clover"], [200, 0.7, "Kinda alive clover"], [300, 0.5, "Alive clover"], [500, 0.25, "Silver clover"], [1000, 0.1, "Golden clover"], [2000, 0.05, "Omega clover"], [5000, 0.025, "Godly clover"]]

notifyList = []

botName = "EpicBot69"

emojiLimit = data["savedVars"]["emojiLimit"]

if "statePower" not in data["savedVars"]:
    data["savedVars"]["statePower"] = 0
    for player in data["personalData"]:
        data["personalData"][player]["power"] = 0
        data["personalData"][player]["coupWaitTime"] = 0

countGameCounter = 0
countGameRecord = data["savedVars"]["countGameRecord"]
countGameName = ""

if "expectedMarketCap" not in data["savedVars"].keys():
    data["savedVars"]["expectedMarketCap"] = 0

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")

time.sleep(90)

if "saverTax" not in data["savedVars"].keys():
    print("---------------------> Savertax resetted!")
    data["savedVars"]["saverTax"] = 0

newMessageTime = time.time()

blockSearching = False
threading.Timer(1800, autoSave).start()
threading.Timer(43200, autoRefresh).start()

search = driver.find_elements_by_class_name("ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr".replace(" ","."))
for item in search:
    if item.text == groupName:
        item.click()
        time.sleep(1)
        counter = 0
        while True:
            while not blockSearching:
                print("[{}]: loop:{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), counter))
                counter += 1
                if time.time() - newMessageTime > 12000:
                    time.sleep(120)
                elif time.time() - newMessageTime > 6000:
                    time.sleep(60)
                elif time.time() - newMessageTime > 4000:
                    time.sleep(40)
                elif time.time() - newMessageTime > 1200:
                    time.sleep(20)
                elif time.time() - newMessageTime > 360:
                    time.sleep(10)
                elif time.time() - newMessageTime > 120:
                    time.sleep(5)
                if check_messages():
                    newMessageTime = time.time()
                    for item in reversed(commandsIssuedList):
                        commandParser(item)
                    getTexts()
                    for enu, item in enumerate(messageDataList):
                        if item not in messagesSend and item not in savedMessageDataList:
                            commandParser(item)
                            if emojiList[enu] > emojiLimit:
                                responseFunction("Emoji Alert, you just used {} emojis...".format(emojiList[enu]))
                    messagesSend = []
                    savedMessageDataList = messageDataList
            time.sleep(15)