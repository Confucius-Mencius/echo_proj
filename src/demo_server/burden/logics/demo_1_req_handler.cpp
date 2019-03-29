#include "demo_1_req_handler.h"
#include "burden_scheduler_interface.h"
#include "cs_msg.pb.h"
#include "cs_msg_id.pb.h"
#include "err_code.h"
#include "log_util.h"
#include "protobuf_util.h"

using namespace com::moon::demo;

namespace burden
{
Demo1ReqHandler::Demo1ReqHandler()
{

}

Demo1ReqHandler::~Demo1ReqHandler()
{

}

MsgId Demo1ReqHandler::GetMsgId()
{
    return cs::MSG_ID_DEMO_1_REQ;
}

void Demo1ReqHandler::OnMsg(const ConnGUID* conn_guid, const ::proto::MsgHead& msg_head, const void* msg_body,
                            size_t msg_body_len)
{
    LOG_TRACE("burden::Demo1ReqHandler::OnMsg, " << conn_guid << ", " << msg_head << ", msg body len: " << msg_body_len);

    cs::Demo1Req demo_1_req;
    if (ParseProtobufMsg(&demo_1_req, msg_body, msg_body_len) != 0)
    {
        LOG_ERROR("failed to parse msg, msg id: " << msg_head.msg_id << ", msg body len: " << msg_body_len);
        SendErrRsp(conn_guid, msg_head, ERR_INVALID_PARAM);
        return;
    }

    LOG_TRACE("a: " << demo_1_req.a());

    ::proto::MsgHead rsp_msg_head = msg_head;
    rsp_msg_head.msg_id = cs::MSG_ID_DEMO_1_RSP;

    cs::Demo1Rsp demo_1_rsp;
    demo_1_rsp.mutable_err_ctx()->set_err_code(ERR_OK);

    if (!demo_1_req.udp())
    {
//        if (SendToTcpClient(logic_ctx_->scheduler, conn_guid, rsp_msg_head, &demo_1_rsp) != 0)
//        {
//            LOG_ERROR("failed to send to " << conn_guid);
//            return;
//        }
    }
    else
    {
//        if (SendToUdpClient(logic_ctx_->scheduler, conn_guid, rsp_msg_head, &demo_1_rsp) != 0)
//        {
//            LOG_ERROR("failed to send to " << conn_guid);
//            return;
//        }
    }
}
}
