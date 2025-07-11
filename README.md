# Streamlit Chat Application

This is a simple Streamlit application that provides a chat interface, likely powered by an OpenAI model.

## 🔗 Live Demo

[👉 Try the Chatbot on Streamlit](https://qnachatbotapplication.streamlit.app/)

## Features

- Interactive chat interface.
- Model selection (e.g., GPT-3.5, GPT-4).
- Temperature control for response creativity.
- Clear chat history functionality.
- Asynchronous communication with the OpenAI API.
- Enhanced UI with custom CSS for a professional look.

## Setup

Follow these steps to set up and run the application locally.

### Prerequisites

- Python 3.8+
- An OpenAI API key

### Installation

1.  **Clone the repository (if applicable)**:

    ```bash
    git clone <https://github.com/Mahfujul-01726/QnA-Chatbot>
    cd <QnA-Chatbot>
    ```

2.  **Create a virtual environment (recommended)**:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your OpenAI API Key**:

    Create a `.env` file in the root directory of your project and add your OpenAI API key:

    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    ```

    Replace `"your_openai_api_key_here"` with your actual OpenAI API key.

## Usage

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will open the application in your web browser, usually at `http://localhost:8501`.

## Project Structure

- `app.py`: The main Streamlit application file containing the UI and logic.
- `requirements.txt`: Lists all Python dependencies required to run the application.
- `.env`: Stores environment variables, such as your OpenAI API key.
- `chat.py`, `qachat.py`, `vision.py`: (Optional) These files might contain additional functionalities related to chat, Q&A, or vision processing, depending on the full scope of the project.

## Customization

You can customize the application by modifying `app.py`:

- **Model**: Change the default OpenAI model in the sidebar settings.
- **Temperature**: Adjust the temperature slider to control the creativity of the AI's responses.
- **UI/CSS**: Modify the custom CSS within `app.py` to change the application's appearance.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.
