import requests
import json

OTP_URL = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
VALIDATE_OTP_URL = ""
SLOTS_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode=313001&date=09-05-2021"


def clean_center(center):
    center.pop('lat')
    center.pop('long')
    center.pop('fee_type')
    center.pop('district_name')
    center.pop('state_name')
    print(json.dumps(center, sort_keys=True, indent=4))


def find_center(token):

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        "Authorization": f"Bearer {token}"
    }

    r = requests.get(SLOTS_URL, headers=HEADERS)
    print(r.status_code)

    result = r.json()['centers']

    if result:
        for center in result:
            sessions = center['sessions']
            for session in sessions:
                if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
                    clean_center(center)


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJjMGU2ZTBkNS1kYTFjLTRhM2UtODJkZS0xMmFhMGFlYjU5ODciLCJ1c2VyX2lkIjoiYzBlNmUwZDUtZGExYy00YTNlLTgyZGUtMTJhYTBhZWI1OTg3IiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo3OTc2MDQzNjA3LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjQwMTg5NzY0OTI1NTIwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MC4wLjQ0MzAuOTMgU2FmYXJpLzUzNy4zNiIsImRhdGVfbW9kaWZpZWQiOiIyMDIxLTA1LTA5VDExOjQyOjQ5LjA4MloiLCJpYXQiOjE2MjA1NjA1NjksImV4cCI6MTYyMDU2MTQ2OX0.XGmKWQxwDANp_R21w8aXbU-nup_NUQDEJtrebt2qVNI"

# find_center(token)


def get_token():
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Content-type': 'application/json'
    }

    number = "8112274755"
    body = {
        "mobile": (number)
    }

    r = requests.post(OTP_URL, data=body, headers=HEADERS)
    print(r.status_code)
    print(r.json())


get_token()
