#include "demo1_req_handler.h"
#include "cs_msg.pb.h"
#include "cs_msg_id.pb.h"
#include "err_code.h"
#include "proto_tcp_protobuf_util.h"

using namespace com::moon::demo;

namespace tcp
{
namespace proto
{
Demo1ReqHandler::Demo1ReqHandler()
{
}

Demo1ReqHandler::~Demo1ReqHandler()
{
}

::proto::MsgID Demo1ReqHandler::GetMsgID()
{
    return cs::MSG_ID_DEMO1_REQ;
}

void Demo1ReqHandler::OnMsg(const ConnGUID* conn_guid, const ::proto::MsgHead& msg_head, const void* msg_body, size_t msg_body_len)
{
    LOG_TRACE("Demo1ReqHandler::OnMsg");

    cs::Demo1Req demo1_req;
    if (ParseProtobufMsg(&demo1_req, msg_body, msg_body_len) != 0)
    {
        LOG_ERROR("failed to parse msg, msg id: " << msg_head.msg_id << ", msg body len: " << msg_body_len);
        SendErrRsp(conn_guid, msg_head, ERR_INVALID_PARAM);
        return;
    }

    // TODO

    ////////////////////////////////////////////////////////////////////////////////
    ::proto::MsgHead rsp_msg_head = msg_head;
    rsp_msg_head.msg_id = cs::MSG_ID_DEMO1_RSP;

    cs::Demo1Rsp demo1_rsp;
    demo1_rsp.mutable_err_ctx()->set_err_code(ERR_OK);

    if (SendToClient(logic_ctx_->scheduler, conn_guid, rsp_msg_head, &demo1_rsp) != 0)
    {
        LOG_ERROR("failed to send to " << conn_guid << ", msg id: " << rsp_msg_head.msg_id);
        return;
    }
}

void Demo1ReqHandler::SendErrRsp(const ConnGUID* conn_guid, const ::proto::MsgHead& req_msg_head, int err_code) const
{
    ::proto::MsgHead rsp_msg_head = req_msg_head;
    rsp_msg_head.msg_id = cs::MSG_ID_DEMO1_RSP;

    cs::Demo1Rsp demo1_rsp;
    demo1_rsp.mutable_err_ctx()->set_err_code(err_code);

    SendToClient(logic_ctx_->scheduler, conn_guid, rsp_msg_head, &demo1_rsp);
}
}
}