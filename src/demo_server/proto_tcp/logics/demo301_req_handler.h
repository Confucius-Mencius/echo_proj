#ifndef DEMO_SERVER_PROTO_TCP_LOGICS_DEMO301_REQ_HANDLER_H_
#define DEMO_SERVER_PROTO_TCP_LOGICS_DEMO301_REQ_HANDLER_H_

#include "msg_handler.h"

namespace tcp
{
namespace proto
{
class Demo301ReqHandler : public MsgHandler
{
public:
    Demo301ReqHandler();
    virtual ~Demo301ReqHandler();

    ///////////////////////// MsgHandlerInterface /////////////////////////
    ::proto::MsgID GetMsgID() override;
    void OnMsg(const ConnGUID* conn_guid, const ::proto::MsgHead& msg_head,
               const void* msg_body, size_t msg_body_len) override;

private:
    void SendErrRsp(const ConnGUID* conn_guid, const ::proto::MsgHead& req_msg_head, int err_code) const;
};
}
}

#endif // DEMO_SERVER_PROTO_TCP_LOGICS_DEMO301_REQ_HANDLER_H_
