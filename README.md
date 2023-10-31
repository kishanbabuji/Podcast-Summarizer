# Podcast Summarizer Tool

The Podcast Summarizer is a web application that allows users to quickly and easily obtain summaries of their favorite podcast episodes. This app leverages the ListenNotes API for fetching episode data and Assembly AI for generating summarized chapter transcriptions. Whether you're a podcast enthusiast looking to save time or a content creator searching for episode highlights, this app simplifies the process of extracting key information.

 Certainly! Below is an example README file for a Podcast Summarizer web app. You can use this as a template and customize it to fit your specific application and requirements.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Features

- **Podcast Episode Summarization:** Retrieve concise summaries of podcast episodes, highlighting the main topics and key points.

- **Easy to Use:** A user-friendly interface makes it simple for both casual listeners and content creators to generate episode summaries.

- **ListenNotes API Integration:** Utilizes the ListenNotes API to obtain podcast episode details.

- **Assembly AI Integration:** Employs Assembly AI to generate the transcript and summarized chapters from the podcast audio.

## Demo

[[LINK TO DEMO]
](https://podcast-summarizer2023.streamlit.app/)
- #### Please avoid misusing the tool as there are only a limited number of requests that can be made each month

## Getting Started

To run this web app locally or deploy it on your preferred cloud platform, follow these steps:

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/podcast-summarizer.git
   cd podcast-summarizer
   ```

2. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Configure API Keys:**

   - You will need API keys for ListenNotes and Assembly AI. Add these keys to the appropriate configuration files or environment variables.

4. **Run the App:**

   ```sh
   streamlit run app.py
   ```

5. **Access the App:**

   Open your web browser and navigate to `http://localhost:8501` to use the web app locally.

## Usage

1. Input the podcast episode ID you want to summarize from https://www.listennotes.com/api/. If you would like to simply test out the capabilities of the web app, use this sample episoe ID: **"e0c8a6e3525c4b1a8d06f1d3bf4f9ed6"**
3. Click the "Summarize" button.
4. The app will retrieve the episode details, summarize the chapter transcriptions, and display the results.


