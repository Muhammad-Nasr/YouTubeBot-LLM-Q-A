# YouTubeBot LLM Q&A


**Chat with your Video using a large language model (LLM)!**

***YouTubeBot LLM Q&A*** Imagine, uploading any YouTube video, regardless of *language* or subject matter. Then, chatting with the video transcript itself, powered by a powerful language model. Ask questions, seek clarifications, and explore hidden knowledge within the video. Get answers in your own *language*, making complex content accessible and insightful. It's powered by OpenAI's LLM, LangChain's vectorstore technology, and Streamlit's user-friendly interface.

## Features

- **Upload Youtube Video Url:** Easily upload Video from Youtube.
- **AI-powered conversations:** Chat with your Video using a large language model, capable of generating informative and insightful responses.
- **Knowledge extraction:** Uncover hidden knowledge and insights from your Video through natural language conversations.
- **File chunking:** Optimizes processing and retrieval by splitting large documents into smaller chunks.
- **Vectorstore technology:** Leverages LangChain's vectorstore for efficient document storage and retrieval.
- **User-friendly interface:** Streamlit provides a simple and intuitive interface for easy interaction.

## Requirements

- **Python 10.0.0:** This app uses Python 10.0.0 to ensure compatibility with some packages.


## Getting Started

1. Clone this repository:

   ```bash
   git clone [https://github.com/Muhammad-Nasr/YouTubeBot-LLM-Q-A.git](https://github.com/Muhammad-Nasr/YouTubeBot-LLM-Q-A.git)
   ```
    > Use code with caution. Learn more

2. **Create a virtual environment:**

   It's highly recommended to create a virtual environment to isolate project dependencies:

   ```bash
   python -m venv env
   source env/bin/activate

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain an OpenAI API key**:

   - Sign up for a free OpenAI account: https://beta.openai.com/
   Create a new API key and copy it.
   - Sign up for a free OpenAI account: https://beta.openai.com/
   Create a new API key and copy it.
   - Set your OpenAI API key as an environment variable:

   ``` Bash
   export OPENAI_API_KEY=your_api_key
   OPENAI_API_KEY=your key       # in .env file
   ```

5. **Run the app**:

   ```Bash
   streamlit run main.py
   ```

### Usage

1. Put your open api key in input.
2. Put Video Urlt in input.
3. Click the "Process" button to process the Video.
4. Start chatting with your Video in the chat box.
5. The app will respond with insights and answers based on the  content of the Video.

### References

* LangChain Documentation: https://langchain.readthedocs.io/
* Streamlit Documentation: https://docs.streamlit.io/

## Functionality

YouTubeBot LLM Q&A supports a range of tasks, including:

- **Question answering:** Ask specific questions about the content of your Video, and the app will provide concise and informative answers.
- **Summarization:** Get a summary of key information and insights from your Video, saving you time and effort in reading through lengthy documents.
- **Conversational In Your Prefered Language:** Engage in natural language conversations with the app to uncover hidden insights, explore connections between ideas, and deepen your understanding of the content.

## Examples

Here are some examples of how you can use YouTubeBot LLM Q&A:

1. **Summarization:**
   - Upload a lengthy Video on Productivit.
   - Ask: "Summarize the main findings and recommendations of the video."
   - The app might provide a succinct summary of the key points, saving you time in reading the entire video.

2. **Conversational exploration:**
   - Upload a historical Video about the American Revolution.
   - Engage in a conversation with the app to explore different perspectives, ask follow-up questions, and gain a deeper understanding of the events and motivations behind the revolution.

## Contact

For any inquiries or feedback, please reach out to:

- **Phone (Egypt):** (0020-11562-88555)
- **Email:** muhammadnasr.elsaid@gmail.com
- **LinkedIn:** [www.linkedin.com/in/muhmmad-nasr-8a2119236](www.linkedin.com/in/muhmmad-nasr-8a2119236)
- **Website:** [muhammadnasr.website](muhammadnasr.website)
- **GitHub:** [https://github.com/Muhammad-Nasr](https://github.com/Muhammad-Nasr)
