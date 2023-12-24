from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import say_hello, say_no

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        res1 =  await workflow.execute_activity(
            activity=say_hello, arg=name, start_to_close_timeout=timedelta(seconds=5)
        )
        
        res2 = await workflow.execute_activity(
            activity=say_no, arg=name, start_to_close_timeout=timedelta(seconds=5)
        )
        
        return f"{res1} and {res2}"
    
WORKFLOWS = [SayHello]