# translator
Translates rows of text messages to English.

# Setup

1. Clone the repository:

```bash
git clone https://github.com/tjdaley/translator.git
```

2. Navigate to the project folder and create a virtual environment

```bash
cd translator
python -m venv venv
```

4. Activate the environment

*Windows*
```
venv\scripts\activate.bat
```

*Linux*
```
source venv/bin/activate
```

6. Install dependencies

```
pip install -r requirements.txt
```

7. Google Cloud Console
   A. Create a Project
   B. Set up a billing account
   B. Authorize the Google-Cloud APIs
   C. Create a service account
   D. Add a JSON key to the service account (which will automatically download)
9. Save the Service Account.json
    Save the service account to a file called ".serviceaccount.json
11. Run the Program
