# DanbooruDiscordWebhooks
This requires the pip installation of pybooru and discord_webhook onto the host PC. 

pip install discord-webhook

pip install Pybooru

When first booting the program, it will generate a file named Danbooru.txt. Follow the instructions, here's a copy of what a final copy should look like.

Replace the next line with the donbooru username!

YourDonbooruUsernameHere

Replace the next line with the api key!

YourAPIKeyHere

Hit the enter key to continue the program. It will now generate a TagsWebhooks.txt. Formatting is especially important and must be followed. Here's an example of how a final product should look like.

pink_hairs -vtubers 
https://discord.com/api/webhooks/111111111222222222233333333/3456425252a34252-234234
END

-pink_hairs vtubers 
https://discord.com/api/webhooks/111111111222222222233333333/3456425252a34252-234234
END

-pink_hairs -vtubers 
https://discord.com/api/webhooks/73567635733/32673657537563
https://discord.com/api/webhooks/2nd3245324134/45134513414124
END

The general format is as follows.

Only one line of tags here. They follow the Danbooru style, so you can do a search on the actual website and copy the search.
Your Discord Webhook Linkers go here. You can have 1 or more. 
I would put a 2nd Webhook here, or simply delete this entire line if its only 1.
END

Discord Webhooks fit between the tags and the END. So long as you can follow this format, you can add as many tags as you wish.

Keep in mind, the program does NOT mix and match. Our first set of tags will slowly post only to the webhooks given, then move onto the next set of tags, following that. 
