from fastapi import FastAPI,Request
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()

class SearchRequest(BaseModel):
    variables: dict
    search_key: str

baseurl = 'https://www.googleapis.com/customsearch/v1'
google_search_key = '你自己的google search key'
google_cx_id = '你自己的cx_id'

@app.post('/search')
async def search_google(search_request: SearchRequest):
    print("search_google 开始")
    cTime = search_request.variables.get("cTime")
    search_key = search_request.search_key
    print(search_key)
    print(cTime)
    if not search_key:
        return {
            'prompt': ''
        }

    try:
        params = {
            'q': search_key,
            'cx': google_cx_id,
            'key': google_search_key,
            'c2coff': 1,
            'start': 1,
            'end': 5,
            'dateRestrict': 'm[1]'
        }
        response = requests.get(baseurl, params=params)
        data = response.json()
        result = '\n'.join(item['snippet'] for item in data['items'])
        print(result)
        return {'prompt': f'搜索词: {search_key};google 搜索结果: {result}'}
    except Exception as err:
        print(err)
        return {'prompt': ''}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=6000)
