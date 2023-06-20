import sys

import ReadTokens as rT
import ReadTagsWebhooks as tW
import QueryDanbooru as qD

DANBOORU_USERNAME = None
API_KEY = None


def set_client_info():
    global DANBOORU_USERNAME, API_KEY
    rT.check_files()
    info = rT.get_api_variables()
    DANBOORU_USERNAME = info[1]
    API_KEY = info[3]


def set_tag_webhook_info():
    tagsWebhooks = tW.readFile()


if __name__ == '__main__':

    set_client_info()
    qD.start_loop_query(tW.checkFile(), DANBOORU_USERNAME, API_KEY, rT.get_timing_variables())
    sys.exit(0)

    # from pybooru import Danbooru
    #
    # client = Danbooru('danbooru', username=DANBOORU_USERNAME, api_key=API_KEY)
    # for x in this_contains_tags.keys():
    #     posts = client.post_list(tags=x, limit=4)
    # # posts = client.post_list(tags='Pink_hair -shota -loli -guro -furry -vore', limit=4)
    # for post in posts:
    #     print(post['file_url'])
    # print("End of testing.")
