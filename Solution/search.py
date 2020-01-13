#importing libraries

from googleapiclient.discovery import build
import pandas as pd

DEVELOPER_KEY = 'AIzaSyAZJV-FojaQihvawLbLxagR-LoIlPaLisk'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

#search function using youtube api v3
def youtube_search(term):
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    # Call the search.list method to retrieve results matching the specified
    # query term
    search_response = youtube.search().list(
        q=term,
        type='video',
        pageToken=None,
        part='id,snippet',
        maxResults=50,
        order="relevance"
          ).execute()
    
    title = []
    videoId = []
    pub_date = []
    channel = []
    player=[]

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            title.append(search_result['snippet']['title']) 
            videoId.append(search_result['id']['videoId'])
            pub_date.append(search_result['snippet']['publishedAt'])
            channel.append(search_result['snippet']['channelTitle'])
    
    youtube_dict = {'title':title,'videoId':videoId,'publishedAt':pub_date, 'channel':channel}
    df=pd.DataFrame(data=youtube_dict)
    df = df[['videoId','title','publishedAt','channel']]
    df.columns = ['Video Link','Title','Published Date','Channel']
    df['Video Link']=df['Video Link'].apply(lambda x: str("https://www.youtube.com/watch?v="+str(x)))
    str_dtype = ['Video Link','Title','Channel']
    for i in str_dtype:
        df[i] = df[i].astype(str)
    df['Published Date']=pd.to_datetime(df['Published Date'])
    df=df.sort_values(ascending=True,by=['Title','Published Date'])
    df=df.reset_index(drop=True)
    return df