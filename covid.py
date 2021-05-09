import requests
import json

OTP_URL = 'https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP'
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


token = ""
# find_center(token)


def get_token():
    headers = {
        'accept': 'application/json',
        'Content-type': 'application/json',
    }

    data = '{"mobile":"1234122411"}'

    r = requests.post(OTP_URL, headers=headers, data=data)
    print(r.status_code)
    print(r.json())


get_token()
