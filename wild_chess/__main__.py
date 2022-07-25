"""Main file."""


import asyncio

from wild_chess.setup import Setup


async def test(setup) -> None:  # creating a function to test the setup
    await setup.setup()
    await setup.db.create_player("test")
    print(await setup.db.find_player("test"))
    print(await setup.db.all_players())
    await setup.db.update_player_win("test")
    print(await setup.db.find_player("test"))
    await setup.db.update_player_loss("test")
    print(await setup.db.find_player("test"))
    await setup.db.update_player_tie("test")
    print(await setup.db.find_player("test"))
    await setup.db.update_player_history("test", "user", ["00", "01", "02"], "win")
    print(await setup.db.find_player("test"))
    await setup.db.remove_player("test")
    print(await setup.db.all_players())
    await setup.db.drop_table()
    print("sucess")


if __name__ == "__main__":
    bot = Setup()  # creating a bot object
    asyncio.run(test(bot))  # calling the test function
