import requests
import hashlib
import sys


def request_api_data(query_char):
    '''
    Acceses the API to recieve the list of hashedpasswords
    query_char -> string -> YOUR hashedpassword
    '''
    # This API will never know our full pasword because we are only passing the first 5 hash password letter
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    ans = requests.get(url)
    if ans.status_code != 200:
        raise RuntimeError(f'Error fetching {ans.status_code}, check the API.')
    return ans


def get_response(respons, hashpassword):
    '''
    Matches YOUR password if has been leaked on to a database
    response -> list_object -> list or hashedpassword found with same 5 starting characters
    hashpassword -> string -> remaining charcaters from YOUR password
    '''
    respons = (line.split(':') for line in respons.text.splitlines())
    for hashed, count in respons:
        if(hashed == hashpassword):
            return count
    return 0


def check_pwned_api(password):
    '''
    This hashes your password so it can be secured when run through pwend
    password -> string -> YOUR raw password, not hahsed
    '''
    # Check password if it exist in API response
    # Returns a heximal digit double the language to fit the standard
    hashed_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    first5_char, end = hashed_password[:5], hashed_password[5:]
    response = request_api_data(first5_char)
    return get_response(response, end)


def main(args):
    for password in args:
        count = check_pwned_api(password)
        if count:
            print(
                f'The {password} has been found {count} times. You might want to change your password.')
        else:
            print(
                f'The {password} has not been found. Good job thats a nice password!')
    return 'All Done!!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
