import os

TAG_WEBHOOK_FILE = "TagsWebhooks.txt"
REPLACE_WEBHOOK_LINE = "Replace with Discord Webhook URL. New line for every new webhook.\n"
global isFileEmpty


def checkFile():
    global isFileEmpty, TAG_WEBHOOK_FILE
    try:
        isFileEmpty = os.stat(TAG_WEBHOOK_FILE).st_size == 0
        contents = readFile()
        return setStage(contents)
    except FileNotFoundError:
        print("Danbooru file not found. Creating " + TAG_WEBHOOK_FILE + ". Make sure to edit it.\n")
        create_Tag_Webhook_File()
        contents = readFile()
        return setStage(contents)


def create_Tag_Webhook_File():
    textToWrite = ''
    textToWrite += "Replace this line with Danbooru Syntax'd Tags! \n"
    textToWrite += REPLACE_WEBHOOK_LINE
    textToWrite += "END\n"
    consumerFileWrite = open(TAG_WEBHOOK_FILE, "a")
    consumerFileWrite.write(textToWrite)
    consumerFileWrite.close()
    input("Edit the generated file. Instructions are in the README text file. Hit any key to continue")


# Iterate throughout the Friend.txt in a specific order. Add the userid as a key, and a LIST of discord webhooks as
# its value. Since python sets are referenced, make a unique copy at key assignment so its value are assigned properly.
def setStage(contents):
    cursor = 0
    queryDict = dict()
    tags = ''
    webhooks = set()
    try:
        while cursor < len(contents):
            tags = contents[cursor]
            cursor += 1
            while contents[cursor] != "END":
                webhooks.add(contents[cursor])
                cursor += 1
            queryDict[tags] = webhooks.copy()
            tags = ''
            webhooks.clear()
            cursor += 2
    except IndexError:
        return queryDict
    return queryDict


def readFile():
    cfr = open(TAG_WEBHOOK_FILE, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck