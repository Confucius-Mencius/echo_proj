#include "msg_handler_mgr.h"

namespace work
{
MsgHandlerMgr::MsgHandlerMgr()
{
}

MsgHandlerMgr::~MsgHandlerMgr()
{
}

int MsgHandlerMgr::Initialize(const void* ctx)
{
    if (nullptr == ctx)
    {
        return -1;
    }

    LogicCtx* logic_ctx = (LogicCtx*) ctx;
    msg_dispatcher_ = logic_ctx->msg_dispatcher;

    if (::proto::MsgHandlerMgrTemplate<MsgHandler>::Initialize(ctx) != 0)
    {
        return -1;
    }

//    for (MsgHandlerVec::iterator it = msg_handler_vec_.begin(); it != msg_handler_vec_.end(); ++it)
//    {
//    }

    return 0;
}

void MsgHandlerMgr::SetGlobalLogic(global::TheLogicInterface* global_logic)
{
    for (MsgHandlerVec::iterator it = msg_handler_vec_.begin(); it != msg_handler_vec_.end(); ++it)
    {
        (*it)->SetGlobalLogic(global_logic);
    }
}

void MsgHandlerMgr::SetLogic(Logic* logic)
{
    for (MsgHandlerVec::iterator it = msg_handler_vec_.begin(); it != msg_handler_vec_.end(); ++it)
    {
        (*it)->SetLogic(logic);
    }
}

int MsgHandlerMgr::InitializeMsgHandlerVec()
{
    msg_handler_vec_.push_back(&demo5_nfy_handler_);
    msg_handler_vec_.push_back(&demo4_req_handler_);
    msg_handler_vec_.push_back(&demo6_req_handler_);
    msg_handler_vec_.push_back(&demo50_req_handler_);
    msg_handler_vec_.push_back(&demo200_req_handler_);
    msg_handler_vec_.push_back(&demo1005_nfy_handler_);
    msg_handler_vec_.push_back(&demo1004_req_handler_);
    msg_handler_vec_.push_back(&demo1006_req_handler_);
    msg_handler_vec_.push_back(&demo1050_req_handler_);
    msg_handler_vec_.push_back(&demo300_req_handler_);
    msg_handler_vec_.push_back(&demo301_nfy_handler_);

    return 0;
}

void MsgHandlerMgr::FinalizeMsgHandlerVec()
{
    msg_handler_vec_.clear();
}
}
