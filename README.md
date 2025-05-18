# youtube-summary-automation
An AI-powered n8n workflow to transcribe and summarize YouTube videos with delivery to Telegram.

This project helps **busy professionals** extract meaningful summaries from long YouTube videos using **AI and automation**.

---

## 📌 What It Does

Converts YouTube videos into concise, readable summaries delivered via Telegram. Ideal for those who want to save time and still get the key points.

---

## 🛠 Tech Stack

| Tool            | Purpose                                |
|-----------------|----------------------------------------|
| `n8n`           | Orchestrates the automation workflow   |
| `yt-dlp`        | Extracts audio from YouTube videos     |
| `Whisper`       | Transcribes the audio (Docker hosted)  |
| `Groq LLM`      | Summarizes the transcribed text        |
| `Telegram Bot`  | Delivers the final summary to user     |

---

## 🧠 How It Works

1. Extract audio from YouTube video via `yt-dlp`.
2. Transcribe the audio using self-hosted `Whisper`.
3. Chunk long transcripts into smaller parts.
4. Pass each chunk to `Groq LLM` for summarization.
5. Merge summaries and send them to Telegram bot.

---

---

## 🧰 Prerequisites

- **Docker** (for Whisper)
- **n8n account** or self-hosted instance
- **Telegram Bot API token**
- Free account with [Groq](https://groq.com) (or any LLM of your choice)
- `yt-dlp` installed (or available via CLI)

---

## 🚀 How to Use

1. **Import `Youtube_to_Text_Original.json`** into your n8n instance.
2. Set environment variables or credentials for:
   - Telegram Bot
   - Groq API
3. Make sure Whisper is running via Docker.
4. Trigger the workflow with a YouTube video URL.
5. Wait for your Telegram bot to send you the final summary!

---

## 📌 Use Cases

- Entrepreneurs looking to save time
- Students summarizing educational content
- Researchers doing video reviews
- Podcast and content repurposing

---

## 💡 Limitations

- Groq token limits (can be handled with chunking)
- Works best on English-speaking videos (Whisper default)

---

## 🔓 License

MIT License – Free to use, adapt, and improve.

---

## 🙌 Author

Created by **Damilare Ayoola**

- 💼 [LinkedIn]([https://linkedin.com/in/yourusername](https://www.linkedin.com/in/damilareayoola/))
- 🛠️ [Portfolio]([https://yourportfolio.site](https://www.notion.so/ayooladamilare/AI-Automation-Portfolio-1d465a28349a80bd8224ee71de0ad6c7))
- ☕ Let’s connect!

---

## 🤝 Contributions

Pull requests are welcome! Feel free to open an issue or fork this project.

---



