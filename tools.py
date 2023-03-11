import psutil
import requests
from requests_toolbelt.adapters.source import SourceAddressAdapter
import argparse


def check_ip4(ip: str):
    if ip.startswith('255.') or ip.startswith('127.'):
        return False

    import re
    compile_ip = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
    if compile_ip.match(ip):
        return True
    else:
        return False


def get_nic_ip(prefix=''):
    net_if_addrs = psutil.net_if_addrs()
    arr = [el for sub in list(net_if_addrs.values()) for el in sub]
    arr = [el for sub in arr for el in sub]
    arr = [ip if check_ip4(str(ip)) else None for ip in arr]
    arr = list(filter(lambda x: x is not None, set(arr)))
    if prefix != '':
        arr = list(filter(lambda x: x.startswith(prefix), set(arr)))
    return arr


def prepare_request(sip, req_fun):
    if sip is not None:
        session = requests.Session()
        for prefix in ('http://', 'https://'):
            session.mount(prefix, SourceAddressAdapter(sip))
        try:
            req_fun(session)
        except requests.exceptions.RequestException as e:
            print(f'err: {sip}')
    else:
        req_fun(requests)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help='校园网账号名')
    parser.add_argument('-m', '--pwd', help='校园网账号密码')
    parser.add_argument('-i', '--interface', help='指定接口的ip地址')
    parser.add_argument('-p', '--prefix', help='前缀')
    args = parser.parse_args()
    return args


def get_nics(args):
    nics = []
    if args.interface is not None:
        nics = str(args.interface).split(',')

    if args.prefix is not None:
        nics = get_nic_ip(str(args.prefix))
    return nics


def remove_blank_line(s):
    return s if s is None else s.replace("\n", '').replace("\r", '')
