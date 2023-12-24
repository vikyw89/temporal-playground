import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from activities import ACTIVITIES
from workflows import SayHello

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, task_queue="hello-task-queue", workflows=[SayHello], activities=ACTIVITIES
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())