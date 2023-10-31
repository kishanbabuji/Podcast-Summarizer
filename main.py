import streamlit as st
import glob
import json
from podcast_summarizer import save_transcript

st.title("Podcast Summarizer")
with st.expander("How To Use"):
    st.markdown(
    """
    To use our Podcast Summarizer web app, follow these simple steps:
    - **Retrieve Episode ID:** To get started, you'll need the Episode ID of the podcast episode you want to summarize. 
                            If you have the ListenNotes API, you can easily obtain this ID by searching for the desired episode.
    - **Input Episode ID:** Enter the Episode ID into the text box to the left and the web app will begin summarizing the content. Please allow a few minutes for the script to complete, especially for longer podcasts. 
    - **Review and Share:** After the summarization process is complete, you can review the generated summary. The summary contains chapter titles and summaries as well as timestamps for easy reference. 

    By following these steps, you can quickly and efficiently generate episode summaries for your favorite podcasts, saving you time and helping you to grasp the main takeaways from the content you love. Enjoy using our Podcast Summarizer web app!
    """
    )

json_files = glob.glob('*.json')

episode_id = st.sidebar.text_input("Enter A Valid Episode ID")
button = st.sidebar.button("Download Episode summary", on_click=save_transcript, args=(episode_id,))

def get_clean_time_MS(start_ms):
    seconds = int((start_ms / 1000) % 60)
    minutes = int((start_ms / (1000 * 60)) % 60)
    hours = int((start_ms / (1000 * 60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
        
    return start_t

def get_clean_time_S(start_s):
    seconds = int(start_s % 60)
    minutes = int((start_s / 60) % 60)
    hours = int((start_s / (60 * 60)) % 24)
    if hours > 0:
        start_t = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_t = f'{minutes:02d}:{seconds:02d}'
        
    return start_t


if button:
    filename = episode_id + '_chapters.json'
    print(filename)
    with open(filename, 'r') as f:
        data = json.load(f)

    chapters = data['chapters']
    episode_title = data['episode_title']
    thumbnail = data['thumbnail']
    podcast_title = data['podcast_title']
    audio = data['audio_url']

    st.header(f"{podcast_title} - {episode_title}")
    st.image(thumbnail, width=200)
    st.markdown(f'#### {episode_title}')
    if data['explicit_content']:
        st.markdown(f'##### :red[Explicit Content]')
    st.markdown(f'##### Episode Duration: ' + get_clean_time_S(data['episode_duration']))

    for chp in chapters:
        with st.expander(chp['gist'] + ' - ' + get_clean_time_MS(chp['start'])):
            chp['summary']