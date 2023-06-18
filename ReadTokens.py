import os

DAN_FILE_TO_ACCESS = 'Danbooru.txt'
DAN_TEXT_TO_WRITE = "Replace the next line with the donbooru username!\nReplace me with your donbooru username!\nReplace the next " \
                    "line with the api key!\nReplace me with your api key!"
global fileEmpty


# If the file exists, do nothing. If it doesn't catch the error resulting from no file found and create it!
def check_files():
    global fileEmpty
    try:
        fileEmpty = os.stat(DAN_FILE_TO_ACCESS).st_size == 0
    except OSError:
        print("File not found.Creating " + DAN_FILE_TO_ACCESS + ".Write down the info within the file. File "
                                                                "location=program was run.\n")
        consumerFileWrite = open(DAN_FILE_TO_ACCESS, "w")
        consumerFileWrite.close()
        consumerFileWrite = open(DAN_FILE_TO_ACCESS, "a")
        consumerFileWrite.write(DAN_TEXT_TO_WRITE)
        consumerFileWrite.close()
        input("Edit the generated text file " + DAN_FILE_TO_ACCESS + " , then hit enter to continue.")


def get_api_variables():
    cfr = open(DAN_FILE_TO_ACCESS, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck
