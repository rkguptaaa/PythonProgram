import requests
import hashlib


class CheckPassword:
    _api_url = 'https://api.pwnedpasswords.com/range/'

    def __init__(self, *args):
        self.passwords = args

    def hit_api(self, hash_five, rest_hash):
        url = CheckPassword._api_url + hash_five  # '70ccd9007338d6d81dd3b6271621b9cf9a97ea00'
        res = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f'Error Fetching: {res.status_code}  ')
        return self.checkIfPasswordPwned(res, rest_hash)

    def checkIfPasswordPwned(self, response, rest_hash):
        responseText = (line.split(':') for line in response.text.splitlines())
        for h, count in responseText:
            if h == rest_hash:
                print(h, rest_hash)
                return count
        return 0

    def is_password_pwned(self):
        for password in self.passwords:
            hash_password = hashlib.sha1(password.encode(encoding='UTF-8')).hexdigest()
            first5_char, restHash = hash_password[:5], hash_password[5:]
            print(first5_char, restHash)
            return self.hit_api(first5_char, restHash)


chkPwd = CheckPassword('password@123', 'bye', 'hello')
count = chkPwd.is_password_pwned()
if count:
    print(f'Password is pawned for {count} times')
else:
    print('Password is not pawned')
