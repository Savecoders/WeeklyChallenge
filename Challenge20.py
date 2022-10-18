
import asyncio


async def sum(number, number2):

    await asyncio.sleep(20)
    print(number + number2)


def main():
    asyncio.run(sum(1, 2))


if __name__ == "__main__":
    main()
