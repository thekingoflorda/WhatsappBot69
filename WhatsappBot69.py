def check_messages():
    global savedMessageDataList, messageDataList, Messages, messagesSend, commandsIssuedList
    getTexts()
    if savedMessageDataList == []:
        savedMessageDataList = messageDataList
    commandsIssuedList = []
    for i in range(30):
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
            if parsedName in data["achievements"].keys():
                data["achievements"][parsedName]["messagesSend"] += 1
                if data["achievements"][parsedName]["messagesSend"] == 100:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 1!".format(parsedName))
                elif data["achievements"][parsedName]["messagesSend"] == 200:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 2!".format(parsedName))
                elif data["achievements"][parsedName]["messagesSend"] == 500:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 3!".format(parsedName))
                elif data["achievements"][parsedName]["messagesSend"] == 1000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 4!".format(parsedName))
                elif data["achievements"][parsedName]["messagesSend"] == 2000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 5!".format(parsedName))
                elif data["achievements"][parsedName]["messagesSend"] == 5000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 6!".format(parsedName))
                elif data["achievements"][parsedName]["messagesSend"] == 10000:
                    responseFunction("{} has unlocked the achievement: Whatsapp adict 7!".format(parsedName))

            try:
                for item in notifyList:
                    if parsedName == item[0]:
                        responseFunction(item[2] + " wanted to notify " + item[0] + " of: " + item[1])
                        del notifyList[notifyList.index(item)]

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
                                if parsedName in data["achievements"].keys():
                                    data["achievements"][parsedName]["spamCommandUsed"] += 1
                                    if data["achievements"][parsedName]["spamCommandUsed"] == 10:
                                        responseFunction("{} has unlocked the achievement: SPAMMER 1!".format(parsedName))
                                    elif data["achievements"][parsedName]["spamCommandUsed"] == 20:
                                        responseFunction("{} has unlocked the achievement: SPAMMER 2!".format(parsedName))
                                    elif data["achievements"][parsedName]["spamCommandUsed"] == 50:
                                        responseFunction("{} has unlocked the achievement: SPAMMER 3!".format(parsedName))
                                    elif data["achievements"][parsedName]["spamCommandUsed"] == 100:
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
                    elif parsedMessage.lower().startswith("!unadmin:"):
                        if parsedName == "Luc van Remmerden":
                            if parsedMessage.split(":")[1] in admins:
                                admins.remove(parsedMessage.split(":")[1])
                                responseFunction("Unadmined " + parsedMessage.split(":")[1])
                            else:
                                responseFunction("User is not an admin")
                        else:
                            responseFunction("You are not an my creator")
                    elif parsedMessage.lower().startswith("!admin:"):
                        if parsedName == "Luc van Remmerden":
                            if parsedMessage.split(":")[1] not in admins:
                                admins.append(parsedMessage.split(":")[1])
                                responseFunction("Admined " + parsedMessage.split(":")[1])
                            else:
                                responseFunction("User is already an admin")
                        else:
                            responseFunction("You are not an my creator")
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
                            if parsedName in data["achievements"].keys():
                                data["achievements"][parsedName]["jokes"] += 1
                                if data["achievements"][parsedName]["jokes"] == 10:
                                        responseFunction("{} has unlocked the achievement: JOKER 1!".format(parsedName))
                                elif data["achievements"][parsedName]["jokes"] == 20:
                                    responseFunction("{} has unlocked the achievement: JOKER 2!".format(parsedName))
                                elif data["achievements"][parsedName]["jokes"] == 50:
                                    responseFunction("{} has unlocked the achievement: JOKER 3!".format(parsedName))
                                elif data["achievements"][parsedName]["jokes"] == 100:
                                    responseFunction("{} has unlocked the achievement: JOKER 4!".format(parsedName))
                        else:
                            responseFunction("STFU, your muted...")
                    elif parsedMessage.lower().startswith("!addadore:"):
                        if parsedName not in muted:
                            data["savedVars"]["adoreList"].append(parsedMessage.split(":")[1])
                            responseFunction("Added " + parsedMessage.split(":")[1] + " to the adore list")
                        else:
                            responseFunction("STFU, your muted...")
                    elif parsedMessage.lower().startswith("!adore:"):
                        responseFunction(parsedMessage.replace("!adore:", "") + ": " + random.choice(data["savedVars"]["adoreList"]))
                    elif parsedMessage.lower().startswith("!deutsch:"):
                        translator= Translator(to_lang="de")
                        translation = translator.translate(parsedMessage.split(":")[1])
                        responseFunction(translation)
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
                    elif parsedMessage.lower() == "!achievements":
                        if parsedName in data["achievements"].keys():
                            responseFunction("MessageSend(100, 200, 500, 1000, 2000, 5000, 10000): {} || Thomas emoji(10, 20, 50, 100): {} || \"ik ben gay\"(10, 20, 50, 100): {} || praiser(10, 20, 50, 100): {} || praised(10, 20, 50, 100): {} || spammer(10, 20, 50, 100): {} || joker(10, 20, 50, 100): {}".format(data["achievements"][parsedName]["messagesSend"], data["achievements"][parsedName]["thomasEmoji"], data["achievements"][parsedName]["gayUsage"], data["achievements"][parsedName]["praiseSend"], data["achievements"][parsedName]["praiseReceived"], data["achievements"][parsedName]["spamCommandUsed"], data["achievements"][parsedName]["jokes"]))
                        else:
                            responseFunction("You are not yet implemented into the achievement system, contact my creator.")
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
                            responseFunction("You are not an admin, noob, get gut.")
                    elif parsedMessage.lower().startswith("!script:"):
                        if parsedName == "Luc van Remmerden":
                            try:
                                exec(parsedMessage.split(":")[1].replace("“", "\"").replace("”", "\""))
                            except Exception as e:
                                responseFunction("Error: invalid script: " + str(e))
                        else:
                            responseFunction("HAHA! You are not my creator! you really tought I would give you access to my script?")
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
                    elif parsedMessage.lower().startswith("!notify:"):
                        if parsedMessage.split(":")[1].replace("@", "") in ["Luc van Remmerden", "Daan", "Casper", "Jasper", "Emanuel", "Niels", "Crystal", "Lars", "Philippe", "Sem", "Thomas", "Zenno"]:
                            notifyList.append([parsedMessage.split(":")[1].replace("@", ""), parsedMessage.split(":")[2].replace("\n", " | "), parsedName])
                            responseFunction("I am going to notify " + parsedMessage.split(":")[1].replace("@", "") + " of " + parsedMessage.split(":")[2].replace("\n", " | "))
                    elif parsedMessage.lower().startswith("!addicts:"):
                        tempList = []
                        for person in data["achievements"].keys():
                            tempList.append(data["achievements"][person]["messagesSend"])

                        #Get the three persons who send the most messages
                        addictString = ""

                        people = int(parsedMessage.split(":")[1])

                        if parsedName in muted and people > 3:
                            responseFunction("You are muted, you have a limit of 3 (:)")
                            people = 3

                        if people <= len(tempList):
                            for i in range(people):
                                maxValue = max(tempList)
                                index = tempList.index(maxValue)
                                tempList[index] = 0
                                addictString += list(data["achievements"].keys())[index] + ": " + str(maxValue) + " messages\n"
                                tempList[index] = -99
                            responseFunction(addictString)
                        else:
                            responseFunction("Error: there are only " + str(len(tempList)) + " people in the list!")
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
                        if parsedName in data["achievements"].keys():
                            data["achievements"][parsedName]["praiseSend"] += 1
                            if data["achievements"][parsedName]["praiseSend"] == 10:
                                responseFunction("{} has unlocked the achievement: praiser 1".format(parsedName))
                            elif data["achievements"][parsedName]["praiseSend"] == 20:
                                responseFunction("{} has unlocked the achievement: praiser 2".format(parsedName))
                            elif data["achievements"][parsedName]["praiseSend"] == 50:
                                responseFunction("{} has unlocked the achievement: praiser 3".format(parsedName))
                            elif data["achievements"][parsedName]["praiseSend"] == 100:
                                responseFunction("{} has unlocked the achievement: praiser 4".format(parsedName))
                        if parsedMessage.replace("!praise:@", "") in data["achievements"].keys() and parsedName != parsedMessage.replace("!praise:@", ""):
                            data["achievements"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] += 1 
                            if data["achievements"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 10:
                                responseFunction("{} has unlocked the achievement: praised 1".format(parsedMessage.replace("!praise:", "")))
                            elif data["achievements"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 20:
                                responseFunction("{} has unlocked the achievement: praised 2".format(parsedMessage.replace("!praise:", "")))
                            elif data["achievements"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 50:
                                responseFunction("{} has unlocked the achievement: praised 3".format(parsedMessage.replace("!praise:", "")))
                            elif data["achievements"][parsedMessage.replace("!praise:@", "")]["praiseReceived"] == 100:
                                responseFunction("{} has unlocked the achievement: praised 4".format(parsedMessage.replace("!praise:", "")))
                    else:
                        responseFunction("Unknown command")
                elif parsedMessage.lower() == "ping":
                    responseFunction("pong")
                elif parsedMessage.lower() == "ik ben gay":
                    if parsedName in data["achievements"].keys():
                        data["achievements"][parsedName]["gayUsage"] += 1
                        if data["achievements"][parsedName]["gayUsage"] == 10:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 1".format(parsedName))
                        elif data["achievements"][parsedName]["gayUsage"] == 20:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 2".format(parsedName))
                        elif data["achievements"][parsedName]["gayUsage"] == 50:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 3".format(parsedName))
                        elif data["achievements"][parsedName]["gayUsage"] == 100:
                            responseFunction("{} has unlocked the achievement: nothing special to see here 4".format(parsedName))
                elif parsedMessage.lower() == "(:)":
                    if parsedName in data["achievements"].keys():
                        data["achievements"][parsedName]["thomasEmoji"] += 1
                        if data["achievements"][parsedName]["thomasEmoji"] == 10:
                            responseFunction("{} has unlocked the achievement: Thomas emoji 1".format(parsedName))
                        elif data["achievements"][parsedName]["thomasEmoji"] == 20:
                            responseFunction("{} has unlocked the achievement: Thomas emoji 2".format(parsedName))
                        elif data["achievements"][parsedName]["thomasEmoji"] == 50:
                            responseFunction("{} has unlocked the achievement: Thomas emoji 3".format(parsedName))
                        elif data["achievements"][parsedName]["thomasEmoji"] == 100:
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
                #responseFunction("Error: Hallo ik ben een irritante bot aan het zijn, en doe glitchy glitchy boehoe.")
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
    global refreshes, counter
    saveFile()
    groupName = driver.find_element_by_class_name("_21nHd").find_element_by_class_name("ggj6brxn.gfz4du6o.r7fjleex.g0rxnol2.lhj4utae.le5p0ye3.l7jjieqr.i0jNr").text
    refreshes += 1
    counter = 0
    driver.refresh()
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(90)
    search = driver.find_elements_by_class_name("ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr".replace(" ","."))
    for item in search:
        try:
            if item.text == groupName:
                item.click()
        except:
            pass

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
    
    responseFunction("Saved data")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from translate import Translator
import time, datetime, pyautogui, random, jokes, json

global refreshes, counter, lastRenameTime, botName, countGameCounter, countGameRecord, pollList, savedTimeStamps, startingTime, commandsIssued, messagesScanned, messagesSend, countGameName, antiSimpModus, emojiLimit
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
groupName = "Niet veranderen ):<"
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

notifyList = []

botName = "EpicBot69"

emojiLimit = data["savedVars"]["emojiLimit"]

countGameCounter = 0
countGameRecord = data["savedVars"]["countGameRecord"]
countGameName = ""

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")

time.sleep(90)

search = driver.find_elements_by_class_name("ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr".replace(" ","."))
for item in search:
    if item.text == groupName:
        item.click()
        time.sleep(1)
        counter = 0
        while True:
            print("----->loop:{}<-----".format(counter))
            counter += 1
            if counter > 20000:
                refreshWhatsapp()
            
            if check_messages():
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