#ifndef DEMO_SERVER_WORK_LOGICS_MSG_HANDLER_MGR_H_
#define DEMO_SERVER_WORK_LOGICS_MSG_HANDLER_MGR_H_

#include "proto_msg_handler_mgr_template.h"
#include "demo_1_req_handler.h"
#include "global_req_handler.h"

namespace work
{
class Logic;

class MsgHandlerMgr : public ::proto::MsgHandlerMgrTemplate<MsgHandler>
{
public:
    MsgHandlerMgr();
    virtual ~MsgHandlerMgr();

    ///////////////////////// MsgHandlerMgrInterface /////////////////////////
    int Initialize(const void* ctx) override;

public:
    void SetGlobalLogic(global::TheLogicInterface* global_logic);
    void SetLogic(Logic* logic);

private:
    ///////////////////////// MsgHandlerMgrTemplate /////////////////////////
    int InitializeMsgHandlerVec() override;
    void FinalizeMsgHandlerVec() override;

private:
    Demo1ReqHandler demo_1_req_handler_;
    GlobalReqHandler global_req_handler_;
};
}

#endif // DEMO_SERVER_WORK_LOGICS_MSG_HANDLER_MGR_H_
