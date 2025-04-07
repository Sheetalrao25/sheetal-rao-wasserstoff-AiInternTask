# sheetal-rao-wasserstoff-AiInternTask


📬 AI Email Reply Assistant
An intelligent, user-friendly email assistant that automatically drafts professional replies using a Large Language Model (LLM) based on a given email summary and intent — with an option to send the email via Gmail.

🚀 Features
🤖 Uses LLM (like Cohere) to generate natural-sounding email replies

📄 Auto-drafts based on email summary & intent

🧑‍💻 Interacts via command line for simplicity

📤 Sends emails via SMTP securely

✅ Confirmation before sending

🗂️ Project Structure
bash
Copy
Edit
.
├── main.py                # Main script for running the assistant
├── reply_generator.py     # Handles communication with the Cohere API
├── email_sender.py        # Handles sending emails through SMTP
├── .env                   # Environment variables (email summary, intent, credentials)
├── requirements.txt       # List of required Python packages
⚙️ Setup Instructions
1. 🔧 Clone the project
bash
Copy
Edit
git clone https://github.com/your-repo/ai-email-assistant.git
cd ai-email-assistant


3. 🐍 Create virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows


4. 📦 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt


6. 📝 Create a .env file
env
Copy
Edit
EMAIL_SUMMARY=Let's schedule a call with the client next Tuesday at 3 PM to review the design mockups.
EMAIL_INTENT=Set up a client meeting

EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=your_app_password  # Use App Password (not your Gmail password)
COHERE_API_KEY=your_cohere_api_key
💡 Enable 2FA & App Passwords in Gmail

▶️ How to Run
bash
Copy
Edit
python main.py
