import os

DAN_FILE_TO_ACCESS = 'Danbooru.txt'
TIMINGS_AND_POSTS = 'FrequencyandAmount.txt'
DAN_TEXT_TO_WRITE = "Replace the next line with the donbooru username!\nReplace me with your donbooru username!\nReplace the next " \
                    "line with the api key!\nReplace me with your api key!"
TIMINGS_TEXT_TO_WRITE = "Replace the next line with how frequently you want posts to appear in seconds!\n60\nReplace the next " \
                        "line with how many images per tag query shall be recieved!\n15"
global fileEmpty


# If the file exists, do nothing. If it doesn't catch the error resulting from no file found and create it!
def check_files():
    global fileEmpty
    try:
        fileEmpty = os.stat(DAN_FILE_TO_ACCESS).st_size == 0
    except OSError:
        print("File not found. Creating " + DAN_FILE_TO_ACCESS + ".Write down the info within the file. File "
                                                                 "location=program was run.\n")
        consumerFileWrite = open(DAN_FILE_TO_ACCESS, "w")
        consumerFileWrite.close()
        consumerFileWrite = open(DAN_FILE_TO_ACCESS, "a")
        consumerFileWrite.write(DAN_TEXT_TO_WRITE)
        consumerFileWrite.close()
        print("File not found. Creating " + TIMINGS_AND_POSTS + ".Write down the info within the file. File "
                                                                "location=program was run.\n")
    try:
        fileEmpty = os.stat(TIMINGS_AND_POSTS).st_size == 0
    except OSError:
        consumerFileWrite = open(TIMINGS_AND_POSTS, "w")
        consumerFileWrite.close()
        consumerFileWrite = open(TIMINGS_AND_POSTS, "a")
        consumerFileWrite.write(TIMINGS_TEXT_TO_WRITE)
        consumerFileWrite.close()
        input("Edit the generated text file " + TIMINGS_AND_POSTS + " , then hit enter to continue.")


def get_api_variables():
    cfr = open(DAN_FILE_TO_ACCESS, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck


def get_timing_variables():
    cfr = open(TIMINGS_AND_POSTS, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck
