# EZ-Watcher 🕵️‍♂️📁

**Tired of checking folders manually like it's 2005?**  
Did your monthly report vanish again and your boss already scheduled a “quick sync”?  
Don’t worry. *EZ-Watcher* is here to keep you from rage-quitting your job.

> ⚠️ **NOTICE**: Currently, the project is in Alpha phase and is considered super unstable.

<a href="https://ko-fi.com/mostazaniikkkk" target="_blank"><img src="https://www.ko-fi.com/img/githubbutton_sm.svg"></a>

This tiny library does just enough to make you look like you have your life together:

- 📄 Reads a `.json` file to know what files should exist (and silently judges them if they don’t).
- 🔍 Checks if they exist, how big they are, when they were born, and when they last got touched.
- 💌 Generates a perfectly average HTML email with a table of the results.
- 🧠 Works with `email.message.EmailMessage`, so you can plug it into your own mail-sending logic without crying.

> It’s not pretty. It’s not overengineered. But it works. And that’s more than we can say about most things.

---

### ✨ What it actually does

- ✅ Monitors files listed in a simple JSON structure.
- ✅ Supports dynamic filenames using `{now.year}`, `{now.month}`, etc.
- ✅ Extracts basic metadata: exists, size, created, modified.
- ✅ Generates an HTML report (okayish table included) you can drop into an email.

---

### 🧪 Demo (a.k.a. “you’ll get it in 10 seconds”)

```json
[
  {
    "folder": "C:/MyDeadFolder",
    "files": [
      "'report_{now.year}_{now.month:02}.xlsx'",
      "'logs_{now.strftime(\"%Y%m%d\")}.txt'",
      "'hope_is_gone.txt'"
    ]
  }
]
```
### 🧪 Get files
```python
from ezwatcher.file import check_json_file

files = check_json_file("example.json")

for f in files: print(f)
```
### 🧪 Create email
```python
from ezwatcher import Email
from email.message import EmailMessage
from ezwatcher.config import EmailConfig

msg = EmailMessage()
config = EmailConfig(
    smtp_server="smtp.gmail.com",
    smtp_port=465,
    from_email="me@gmail.com",
    password="your_gmail_app_password",
    to=["ops@company.com"]
)

email = Email("example.json", msg, config)
email.send(
    title="Daily File Check",
    body="Hey team,\nHere's today's file status report. Fingers crossed."
)
```
---

### 🐧 Linux support

> 🚫 **Linux support is currently not available.**  
> The file metadata logic uses Windows-specific creation timestamps.  
> If you're on Linux... well, good luck. (Or make a PR, hero.)

---

### 🚧 Planned features

These are not implemented (yet), but might show up if I survive work:

- 🎨 Custom HTML templates (so you can stop blaming me for ugly tables)
- 📄 PDF export of the report
- 📊 Excel export with clean columns
- 📎 Email attachments (instead of just inline content)
- 🧪 Better error reporting/logging (maybe, don't get your hopes up)

