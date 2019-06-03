from os_handling_module import *

print(return_logged_in_user())

print(encode_file('README.md'))
secret_encoded_file = encode_file('README.md')

decoded_secret_files = decode_file(secret_encoded_file)
print(decoded_secret_files)

