# import requests
# import time
# import uuid

# timestamp = int(time.time() * 1000)
# guid = uuid.uuid4()
# guid = guid.hex


# upload = {
#     'image' : open('./01.jpg', 'rb')
# }

# headers = {
#     'Accept' : 'application/json, text/plain, */*',
# }

# r = requests.post(
#     url = f"https://clova.ai/ocr/api/general/ja/recognition?ts={timestamp}&s={guid}",
#     headers = headers,
#     files = upload
# )

# print(r.text)

import json
import codecs
with codecs.open("./t.json", 'r', encoding='utf-8') as f:
    json_data = json.load(f)

    d = json.dumps(json_data, indent=2, ensure_ascii=False)

codecs.open('prettify.json', 'w', encoding='utf-8').write(str(d))