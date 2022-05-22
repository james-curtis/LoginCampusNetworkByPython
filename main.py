import re
import requests
import sys

'''
使用方法：
第一种方法：python3 main.py 你的学号 你身份证后六位
第二种方法：先修改第11行和第12行的代码，然后直接运行python3 main.py
'''
if __name__ == '__main__':
    username = "学号"
    passwd = "身份证后六位"

    if len(sys.argv) == 3:
        username = sys.argv[1]
        passwd = sys.argv[2]

    extPortal = "http://1.1.1.1:8000/ext_portal.magi?url=http://1.1.1.1/&radnum=664343&a.magi"
    r = requests.get(extPortal)
    # 取得mac
    matchR = re.search('mac=(.*?)&', r.text, re.I)
    if matchR is None:
        exit(11)
    mac = matchR.group(1)
    # 获取ip
    matchR = re.search('wlanuserip=(.*?)&', r.text, re.I)
    if matchR is None:
        exit(11)
    ip = matchR.group(1)

    refererTuple = f"http://59.71.0.49/portal.do?wlanuserip={ip}&wlanacname=amnon2&mac={mac}&vlan=0&rand=6289b972",
    referer = refererTuple[0]
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    commonHeaders = {
        "referer": referer,
        "User-Agent": ua,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    r = requests.post("http://59.71.0.49/portalAuthAction.do", data={
        "wlanuserip": ip,
        "wlanacname": "amnon2",
        "chal_id": "",
        "chal_vector": "",
        "auth_type": "PAP",
        "seq_id": "",
        "req_id": "",
        "wlanacIp": "59.71.0.47",
        "ssid": "",
        "vlan": 0,
        "mac": mac,
        "message": "",
        "bank_acct": "",
        "isCookies": "",
        "version": 0,
        "authkey": "amnoon",
        "url": "",
        "usertime": 0,
        "listpasscode": 0,
        "listgetpass": 0,
        "getpasstype": 0,
        "randstr": "6758",
        "domain": "",
        "isRadiusProxy": "false",
        "usertype": 0,
        "isHaveNotice": 0,
        "times": 12,
        "weizhi": 0,
        "smsid": 1,
        "freeuser": "",
        "freepasswd": "",
        "listwxauth": 0,
        "templatetype": 1,
        "tname": 1,
        "logintype": 0,
        "act": "",
        "is189": "false",
        "terminalType": "",
        "checkterminal": "true",
        "portalpageid": 1,
        "listfreeauth": 0,
        "viewlogin": 1,
        "userid": username,
        "wisprpasswd": "",
        "twocode": 0,
        "authGroupId": "",
        "alipayappid": "",
        "wlanstalocation": "",
        "wlanstamac": "",
        "wlanstaos": "",
        "wlanstahardtype": "",
        "smsoperatorsflat": 3,
        "reason": "",
        "res": "",
        "userurl": "",
        "challenge": "",
        "uamip": "",
        "uamport": "",
        "useridtemp": username,
        "passwd": passwd,
        "wxuser": "",
    }, headers=commonHeaders)

    if r.text.find("成功登陆") != -1:
        print("success")
        exit(0)
    print(r.text)
