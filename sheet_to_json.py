import json
import tomli
import gspread
from google.oauth2.service_account import Credentials

SECRETS_FILE = ".streamlit/secrets.toml"
SHEET_NAME = "finetune_data"   # nom exact de ta Google Sheet
OUTPUT_FILE = "data.json"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]

with open(SECRETS_FILE, "rb") as f:
    secrets = tomli.load(f)

creds = Credentials.from_service_account_info(
    secrets["gcp_service_account"], scopes=SCOPES
)
sheet = gspread.authorize(creds).open(SHEET_NAME).sheet1

data = []
for row in sheet.get_all_records():
    question = str(row.get("input", "")).strip()
    reponse = str(row.get("output", "")).strip()
    if question and reponse:   # ignore les lignes incomplètes
        data.append({"input": question, "output": reponse})

if not data:
    raise SystemExit("Aucune ligne valide trouvée : data.json n'a pas été modifié.")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"{len(data)} exemples écrits dans {OUTPUT_FILE}")