import asyncio
from TikTokApi import TikTokApi

class TikTokWrapper:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
           
    def get_video(self, video_id):
        with TikTokApi(asyncio=asyncio.set_event_loop(self.loop)) as api:
            video_data = api.video(id=video_id)
            return video_data.bytes()
