import codecs
import os
import random

from cloudbot import hook

@hook.on_start()
def load_femquotes(bot):

    global femquotes

    with codecs.open(os.path.join(bot.data_dir, "fem.txt"), encoding="utf-8") as f:
        femquotes = [line.strip() for line in f.readlines() if not line.startswith("//")]


@hook.command("fem", "feminism", "feminist", "femquote", autohelp=False)
def fem(message):
    """prints an inspirational feminist quote or statement"""
    message(random.choice(femquotes))
