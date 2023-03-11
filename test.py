import tools

'''
测试接口连通性
'''
if __name__ == '__main__':
    args = tools.get_args()
    nics = tools.get_nics(args)

    for net in nics:
        print(f'>>>>>>>>>>>>>{net}')
        tools.prepare_request(net,
                              lambda session:
                              print(tools.remove_blank_line(session.get("http://test.ipw.cn", timeout=1).text)))
