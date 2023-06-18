import time


def start_loop_query(tags_webhooks: dict, DANBOORU_USERNAME: str, API_KEY: str):

    TIME_BETWEEN_POSTS = 49
    TIME_BETWEEN_WEBHOOK_POSTS = 1
    TEST_TIME = 0
    POSTS_PER_QUERY = 25
    from pybooru import Danbooru
    from discord_webhook import DiscordWebhook
    client = Danbooru('danbooru', username=DANBOORU_USERNAME, api_key=API_KEY)
    # Continue this forever, with the tags supplied at launch. We work on the images as they get qeued
    while True:
        # Queue Danbooru using the given tags in file.
        for tags in tags_webhooks.keys():
            postList = client.post_list(tags=tags, limit=POSTS_PER_QUERY)
            # Work on the returned postList. We want to trickle the posts slowly, not all at once.
            for posts in postList:
                # Finally, post the proper tags to the proper Discord Webhooks.
                for webhooksSet in tags_webhooks.get(tags):
                    webhook = DiscordWebhook(url=webhooksSet, content=posts['file_url'])
                    webhook.execute()
                    # print(posts['file_url'] + " 1:1 " + webhooksSet + "\n")
                    time.sleep(TIME_BETWEEN_WEBHOOK_POSTS)
                time.sleep(TIME_BETWEEN_POSTS)
        time.sleep(TEST_TIME)
        print("We are cycling now!")
