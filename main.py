import streamlit as st
from dotenv import load_dotenv
from helper import (
    get_api_key, process_video_data,
    get_vectorstoredb, split_transcript_chunks,
    get_qa_chain, handle_userinput
)
import time


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = {}

    if "thumbnail" not in st.session_state:
        st.session_state.thumbnail = None

    if "uploded_video" not in st.session_state:
        st.session_state.uploded_video = False

    # print("session", st.session_state)

    st.header("Chat with Your Video :books:")

    if st.session_state.thumbnail:
        st.image(st.session_state.thumbnail)

    # print(st.session_state.messages)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # create user input prompt
    if prompt := st.chat_input("Chat with your video?"):
        if not st.session_state.uploded_video:
            st.warning("You Should Upload File First", icon="🤖")

        else:
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            handle_userinput(prompt)

    with st.sidebar:
        openai_api_key = get_api_key()

        if not openai_api_key:
            st.warning(
                'Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
            st.stop()
        st.subheader("Your Youtube Video Url")

        # select type of document source

        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
        )

        if youtube_url:
            if not openai_api_key:
                st.warning(
                    "File uploaded, But You should add open api key to chat with file!",
                    icon="⚠️")
                return

            if st.button("Upload"):
                with st.spinner("Uploading"):
                     # Delete all the items in session state if no files are uploaded or the user removed the files.
                    for key in st.session_state.keys():
                        del st.session_state[key]

                    # get transcript, and metadata
                    transcript, metadata = process_video_data(youtube_url)
                    # split document
                    chunks = split_transcript_chunks(transcript)

                    # vectorstore chunks
                    vectorestore = get_vectorstoredb(chunks, openai_api_key)

                    # get conversation chain
                    st.session_state.qa_chain = get_qa_chain(
                        vectorestore, openai_api_key
                    )

                    time.sleep(2)

                    st.session_state.thumbnail = metadata["thumbnail_url"]
                    st.session_state.uploded_video = True

                    # force the app to rerun to display the thumbnail
                    st.rerun()

      
           


if __name__ == '__main__':
    main()
