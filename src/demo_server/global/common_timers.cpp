#include "common_timers.h"
#include "log_util.h"
#include "the_global_logic_interface.h"

namespace global
{
enum
{
    DEMO_TIMER_ID = 1,
};

CommonTimers::CommonTimers()
{
    logic_ctx_ = nullptr;
}

CommonTimers::~CommonTimers()
{
}

int CommonTimers::Initialize(const void* ctx)
{
    logic_ctx_ = (LogicCtx*) ctx;
    return 0;
}

void CommonTimers::Finalize()
{
}

int CommonTimers::Activate()
{
    global::TheLogicInterface* global_logic = static_cast<global::TheLogicInterface*>(logic_ctx_->global_logic);

    if (global_logic->GetConfMgr()->TestMode())
    {
        struct timeval tv = { 0, 1000 }; // 1毫秒打一次日志

        if (logic_ctx_->timer_axis->SetTimer(this, DEMO_TIMER_ID, tv, nullptr, 0) != 0)
        {
            LOG_ERROR("failed to add timer");
            return -1;
        }
    }

    return 0;
}

void CommonTimers::Freeze()
{
    logic_ctx_->timer_axis->KillTimer(this, DEMO_TIMER_ID);
}

void CommonTimers::OnTimer(TimerID timer_id, void* data, size_t len, int times)
{
//    LOG_ERROR("in common timers");
//    LOG_ALWAYS("in common timers");
}

void CommonTimers::OnReload()
{
    global::TheLogicInterface* global_logic = static_cast<global::TheLogicInterface*>(logic_ctx_->global_logic);

    if (!logic_ctx_->timer_axis->TimerExist(this, DEMO_TIMER_ID))
    {
        if (global_logic->GetConfMgr()->TestMode())
        {
            struct timeval tv = { 0, 1000 }; // 1毫秒打一次日志

            if (logic_ctx_->timer_axis->SetTimer(this, DEMO_TIMER_ID, tv, nullptr, 0) != 0)
            {
                LOG_ERROR("failed to add timer");
                return;
            }
        }
    }
    else
    {
        if (!global_logic->GetConfMgr()->TestMode())
        {
            logic_ctx_->timer_axis->KillTimer(this, DEMO_TIMER_ID);
        }
    }
}
}
