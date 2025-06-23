# Simple Chatbot

A basic chatbot built with Python Flask that answers common questions.

## What it does

- Answers frequently asked questions
- Responds to greetings and basic conversations
- Has a web chat interface
- Gives helpful responses when it doesn't understand something

## How to run it

1. **Install Flask:**
   ```bash
   pip install flask
   ```

2. **Create folders:**
   ```
   chatbot/
   ├── app.py
   └── templates/
       └── index.html
   ```

3. **Save the files:**
   - Put the Python code in `app.py`
   - Put the HTML code in `templates/index.html`

4. **Run it:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Go to `http://localhost:5000`

## Try these questions

- "Hello"
- "What are your hours?"
- "How do I contact support?"
- "Who are you?"

## How to add more responses

Edit the `chatbot_responses` dictionary in `app.py`:

```python
chatbot_responses = {
    "new question": "new answer",
    "hello": "Hello! How can I help you today?",
    # ... add more here
}
```

## Files

- `app.py` - The main chatbot code
- `templates/index.html` - The chat webpage

That's it! Your chatbot is ready to use.
