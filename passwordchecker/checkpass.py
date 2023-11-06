import requests as req
import hashlib as hash
import sys


def api_call_response(password="CBFDA"):
    url = f'https://api.pwnedpasswords.com/range/{password}'
    response = req.api.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}')
    return response

def get_password_leak_count(response_hashes, hash_to_check):
    hashes = (line.split(':') for line in response_hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count
        return 0


def pwned_api(password):
    sha1_password = hash.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char, tail = sha1_password[:5],sha1_password[5:]
    response = api_call_response(first_5char)
    return get_password_leak_count(response, tail)


def main():
    input_password = str(sys.argv[1])
    count = pwned_api(input_password)
    if count:
        print(f'Password: {input_password} was found {count} times. Change your password!')
    else:
        print(f'Password: {input_password} was NOT found.')
    
    print('done')

if __name__ == '__main__':
    sys.exit(main())