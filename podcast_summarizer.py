import requests
import json
import time
import pprint
import os
import streamlit as st

os.environ['API_KEY_ASSEMBLYAI'] = st.secrets['API_KEY_ASSEMBLYAI']
os.environ['API_KEY_LISTENNOTES'] = st.secrets['API_KEY_LISTENNOTES']

transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
headers_assemblyai = {
    "authorization": st.secrets['API_KEY_ASSEMBLYAI'],
    "content-type": "application/json"
}

listennotes_episode_endpoint = 'https://listen-api.listennotes.com/api/v2/episodes'
headers_listennotes = {
  'X-ListenAPI-Key': st.secrets['API_KEY_ASSEMBLYAI'],
}

# Function to get the url with podcast audio for transcribing as well as key information about the podcast
def get_episode_audio_url(episode_id):
    url = listennotes_episode_endpoint + '/' + episode_id
    data = requests.request('GET', url, headers=headers_listennotes).json()

    st.write(data)
    # pprint.pprint(data)

    episode_title = data['title']
    thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    audio_url = data['audio']
    explicit_content = data['explicit_content']
    episode_duration = data['audio_length_sec']
    return audio_url, thumbnail, podcast_title, episode_title, explicit_content, episode_duration

# Function to transcribe the podcast using Assembly AI
def transcribe(audio_url, auto_chapters):
    transcript_request = {
        'audio_url': audio_url,
        'auto_chapters': auto_chapters
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers_assemblyai)
    pprint.pprint(transcript_response.json())
    return transcript_response.json()['id']


def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers_assemblyai)
    return polling_response.json()
    

#Function to report on the status of transcription as AssemblyAI is processing the data 
def get_transcription_result_url(url, auto_chapters):
    transcribe_id = transcribe(url, auto_chapters)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']

        print("waiting for 60 seconds")
        time.sleep(60)
            
# Function to save key podcast info, chapter summaries and transcript 
def save_transcript(episode_id):
    audio_url, thumbnail, podcast_title, episode_title, explicit_content, episode_duration = get_episode_audio_url(episode_id)
    data, error = get_transcription_result_url(audio_url, auto_chapters=True)
    if data:
        filename = episode_id + '.txt'
        with open(filename, 'w') as f:
            f.write(data['text'])

        chapters_filename = episode_id + '_chapters.json'
        with open(chapters_filename, 'w') as f:
            chapters = data['chapters']

            data = {'chapters': chapters}
            data['audio_url']=audio_url
            data['thumbnail']=thumbnail
            data['podcast_title']=podcast_title
            data['episode_title']=episode_title
            data['explicit_content'] = explicit_content
            data['episode_duration'] = episode_duration
            # for key, value in kwargs.items():
            #     data[key] = value

            json.dump(data, f, indent=4)
            print('Transcript saved')
            return True
    elif error:
        print("Error!!!", error)
        return False