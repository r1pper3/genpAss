# coding=utf-8
from __future__ import print_function
import re
import time
import argparse
from genpass.lib.person import Person


def email(string):
    if not re.match(r'^[\w\d.-_]+@[\w\d.-]+\.[\w]{2,8}$', string):
        raise ValueError(string)
    return string


def date(date_string):
    if not date_string:
        return None
    return time.strptime(date_string, '%Y-%m-%d')


def cmd_parser():
    parser = argparse.ArgumentParser(description='User information')

    parser.add_argument('-n', '--name', dest='name', action='store',
                        help='real name of target', nargs='*', default=[])
    parser.add_argument('-u', '--username', dest='username', action='store',
                        help='usernames of target, English only', nargs='*', default=[])
    parser.add_argument('-q', '--qq', dest='qq', action='store',
                        help='QQ numbers of target', nargs='*', type=int, default=[])
    parser.add_argument('-e', '--email', dest='email', action='store',
                        help='email addresses of target', nargs='*', type=email, default=[])
    parser.add_argument('-m', '--mobile', dest='mobile', action='store',
                        help='mobile phone/phone numbers of target', nargs='*', type=int, default=[])
    parser.add_argument('-b', '--birthday', dest='birthday', action='store',
                        help='birthday of target, format: %%Y-%%m-%%d', type=date, default=None)
    parser.add_argument('-c', '--company', dest='company', nargs='*', action='store',
                        help='company / website domain of target', type=str, default=[])
    parser.add_argument('--with-dict', dest='with_dict', action='store_true',
                        help='generate passwords with weak password dictionary')
    parser.add_argument('-o', '--output', dest='output_file', action='store',
                        help='output result to a json file', type=argparse.FileType('w'))

    args = parser.parse_args()
    if not any(args.__dict__.values()):
        parser.print_help()
        raise SystemExit

    person_list = []
    person_list.append(Person(information=args.__dict__))

    return (args, person_list)
