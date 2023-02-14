import asyncio
from TikTokApi import TikTokApi

class TikTokWrapper:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
           
    def get_video(self, video_id):
        verify_fp = 'verify_le4j0oq7_rfWhr2n3_m8tJ_4bMB_80w0_VH7pMVZYnxyO'
        with TikTokApi(asyncio=asyncio.set_event_loop(self.loop), custom_verify_fp=verify_fp, use_test_endpoints=True) as api:
            video_data = api.video(id=video_id)
            return video_data.bytes()
