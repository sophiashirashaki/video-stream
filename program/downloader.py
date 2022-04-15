# Copyright (C) 2021 By Veez Music-Project

from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import yt_dlp
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from config import BOT_USERNAME as bn
from driver.decorators import humanbytes
from driver.filters import command, other_filters


@Client.on_message(command(["lyric", f"lyric@{bn}", "lyrics", f"lyrics@{bn}"]))
@check_blacklist()
async def get_lyric_genius(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**usage:**\n\n/lyrics (song name)")
    m = await message.reply_text("🔍 Searching lyrics...")
    query = message.text.split(None, 1)[1]
    api = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    data = lyricsgenius.Genius(api)
    data.verbose = False
    result = data.search_song(query, get_full_info=False)
    if result is None:
        return await m.edit("❌ `404` lyrics not found")
    xxx = f"""
**Title song:** {query}
**Artist name:** {result.artist}
**Lyrics:**
{result.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`attached lyrics text`",
            quote=False,
        )
        remove_if_exists(filename)
    else:
        await m.edit(xxx)
