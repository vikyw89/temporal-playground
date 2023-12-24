from temporalio import activity

@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@activity.defn
async def say_no(name: str) -> str:
    return f"No, {name}!"


ACTIVITIES = [say_hello, say_no]