class Config():
    # Bot 
    api_key = 'ZTZhZmJiNWMtNjg5NS00NTIyLWE0OGEtYWNmNTYxNzU0NTQ5MGRkODhiNzgtODQy_PF84_b1f87407-8a6e-4299-bcb0-d65305c2ce82'
    room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMWUzNjJkN2MtMzE1NS0zYTM2LWEzMDgtOGYyMGEyZjE5YzM2'
    max_items = 3
    base_url = f'https://api.ciscospark.com/v1/messages?roomId={room_id}&max={max_items}'

    def __init__(self):
        pass