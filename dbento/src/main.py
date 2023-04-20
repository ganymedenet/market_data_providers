import asyncio
import databento as db
import requests

class DataFeed:
    """
    https://docs.databento.com/api-reference-live/basics/schemas-and-conventions?historical=python&live=python
    https://docs.databento.com/api-reference-live/basics/authentication?historical=python&live=python
    https://docs.databento.com/api-reference-live/client?historical=python&live=python
    https://github.com/databento/databento-python
    https://docs.databento.com/api-reference-live/client/live?historical=python&live=python
    """

    def __init__(self):
        self.keys = dict(
            stage="db-bdWRXSWSBXC3diBRmEEHfTJbnedKM",
            prod="db-tQqCcDUTBevFQwHvNdRKQCCnaXwkG"
        )

    async def run(self, env):
        # Create a live client
        client = db.Live(
            dataset="AAPL.MBO",
            key=self.keys.get(env),
        )

        # Connect to the gateway
        client.connect()

        # Subscribe to a data stream
        client.subscribe(
            schema="GLBX.MDP3",
            stype_in="smart",
            symbols="ES.FUT",
        )

        # Start the streaming session
        client.start()

        # Asynchronously iterate the records
        async for record in client:
            print(record)


if __name__ == "__main__":

    client = DataFeed()
    asyncio.run(client.run("stage"))
