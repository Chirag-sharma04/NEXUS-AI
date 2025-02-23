# Nexus AI - Virtual Assistant

## Overview
Nexus AI is a Python-based virtual assistant that can perform various tasks, including web searches, opening applications, providing news updates, and sending emails via voice commands. The assistant uses speech recognition and text-to-speech technology to interact with users.

## Features
- Greets users based on the time of the day.
- Listens to voice commands and processes queries.
- Searches Wikipedia for information.
- Opens commonly used websites (Google, YouTube, Wikipedia, etc.).
- Tells the current time.
- Opens applications like VS Code, Notepad, and Python.
- Plays music from a specified directory.
- Sends emails using SMTP.
- Fetches top news headlines using the NewsAPI.

## Requirements
Ensure you have the following dependencies installed:
```sh
pip install pyttsx3 SpeechRecognition wikipedia requests
```

## Setup Instructions
1. Clone the repository or copy the script.
2. Install dependencies using the command above.
3. Replace the placeholders in the script:
   - `your-email@gmail.com` and `app-password` with your email credentials.
   - `reciever-email` with the recipient's email address.
   - `path-vs-code`, `path//`, `music_dir`, etc., with the correct file paths on your system.
   - `Your-news-api` with your valid NewsAPI key.
4. Run the script using:
```sh
python main.py
```

## Usage
- Run the script and start speaking commands.
- Say "open Google," "open YouTube," or "open Wikipedia" to launch these sites.
- Ask "the time" to get the current time.
- Say "play music" to play a song from the specified directory.
- Use "email" to send an email after dictating the message.
- Say "news" to get the latest headlines.
- Say "quit" to exit the assistant.

## Notes
- Ensure your microphone is working correctly.
- The script requires an internet connection for web-based tasks.
- The email function requires enabling "Less secure apps" or an app password in your Gmail settings.

## Future Enhancements
- Adding more integrations like weather updates, calendar events, and smart home controls.
- Implementing a GUI for easier interaction.
- Enhancing natural language understanding for better query recognition.

## License
This project is open-source and available for use and modification under the MIT License.

