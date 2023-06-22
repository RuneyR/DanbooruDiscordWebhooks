import time
import logging


def start_loop_query(tags_webhooks: dict, DANBOORU_USERNAME: str, API_KEY: str, Timings: list):
    TIME_BETWEEN_POSTS = int(Timings[1])
    TIME_BETWEEN_WEBHOOK_POSTS = 1
    TEST_TIME = 0
    POSTS_PER_QUERY = Timings[3]
    logger = logging.getLogger()

    from pybooru import Danbooru
    from discord_webhook import DiscordWebhook
    client = Danbooru('danbooru', username=DANBOORU_USERNAME, api_key=API_KEY)
    print("We are now posting!")
    # Continue this forever, with the tags supplied at launch. We work on the images as they get qeued
    while True:
        try:
            # Queue Danbooru using the given tags in file.
            for tags in tags_webhooks.keys():
                postList = client.post_list(tags=tags, limit=POSTS_PER_QUERY)
                # Work on the returned postList. We want to trickle the posts slowly, not all at once.
                for posts in postList:
                    # Finally, post the proper tags to the proper Discord Webhooks.
                    for webhooksSet in tags_webhooks.get(tags):
                        if "file_url" in posts:
                            webhook = DiscordWebhook(url=webhooksSet, content=posts['file_url'])
                            webhook.execute()
                            time.sleep(TIME_BETWEEN_WEBHOOK_POSTS)
                        elif "large_file_url" in posts:
                            webhook = DiscordWebhook(url=webhooksSet, content=posts['large_file_url'])
                            webhook.execute()
                            time.sleep(TIME_BETWEEN_WEBHOOK_POSTS)
                        else:
                            print("We got problem, look below.")
                            print(posts)
                    time.sleep(TIME_BETWEEN_POSTS)
            time.sleep(TEST_TIME)
            print("We are cycling now!")
        except Exception as e:
            logger.exception("We have an issue here!: " + str(e))
            print(e)
            continue
