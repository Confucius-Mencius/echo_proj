# -*- coding: utf-8 -*-

###############################################################################
# author: BrentHuang (guang11cheng@qq.com)
###############################################################################

import httplib
from util.log_util import *


def test001():
    ret = 0

    try:
        http_conn = httplib.HTTPConnection(conf.demo_server_addr, conf.demo_server_http_port)
        http_conn.request('GET', '/echo')

        http_rsp = http_conn.getresponse()
        LOG_DEBUG('rsp code: %d(%s)' % (http_rsp.status, http_rsp.reason))
        assert http_rsp.status == httplib.OK

        rsp_headers = http_rsp.getheaders()
        for h in rsp_headers:
            LOG_DEBUG('%s: %s' % (h[0], h[1]))

        rsp_body = http_rsp.read()
        LOG_DEBUG('rsp body: %s' % rsp_body)

        http_conn.close()
    except Exception as e:
        LOG_ERROR('exception: %s' % e)
        ret = -1

    assert ret == 0


def test002():
    ret = 0

    try:
        http_conn = httplib.HTTPConnection(conf.demo_server_addr, conf.demo_server_http_port)
        http_conn.request('POST', '/echo', 'x' * 10240)

        http_rsp = http_conn.getresponse()
        LOG_DEBUG('rsp code: %d(%s)' % (http_rsp.status, http_rsp.reason if http_rsp.reason else ''))
        assert http_rsp.status == httplib.OK

        rsp_headers = http_rsp.getheaders()
        for h in rsp_headers:
            LOG_DEBUG('%s: %s' % (h[0], h[1]))

        rsp_body = http_rsp.read()
        LOG_DEBUG('rsp body: %s' % rsp_body)

        http_conn.close()
    except Exception as e:
        LOG_ERROR('exception: %s' % e)
        ret = -1

    assert ret == 0


if __name__ == '__main__':
    test001()
    test002()
