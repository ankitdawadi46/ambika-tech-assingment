from bson import ObjectId

from app.db import database
from app.models.game import GameCreate, GameResponse, GameUpdate


class GameRepository:
    @staticmethod
    async def create_game(game_data: GameCreate) -> GameResponse:
        game_dict = game_data.dict()
        result = await database.db.games.insert_one(game_dict)
        created_game = await database.db.games.find_one({"_id": result.inserted_id})
        created_game["_id"] = str(created_game["_id"])
        return GameResponse(**created_game)

    @staticmethod
    async def get_game(game_id: str) -> GameResponse:
        game = await database.db.games.find_one({"_id": ObjectId(game_id)})
        if not game:
            raise ValueError("Game not found")
        game["_id"] = str(game["_id"])
        return GameResponse(**game)

    @staticmethod
    async def get_all_games() -> list[GameResponse]:
        games = []
        async for game in database.db.games.find():
            game["_id"] = str(game["_id"])
            games.append(GameResponse(**game))
        return games

    @staticmethod
    async def update_game(game_id: str, game_data: GameUpdate) -> GameResponse:
        # Filter out None values
        update_data = {k: v for k, v in game_data.dict().items() if v is not None}
        
        if not update_data:
            raise ValueError("No fields to update")

        result = await database.db.games.update_one(
            {"_id": ObjectId(game_id)},
            {"$set": update_data}
        )

        if result.modified_count == 0:
            raise ValueError("Game not found or no changes made")

        return await GameRepository.get_game(game_id)

    @staticmethod
    async def delete_game(game_id: str) -> bool:
        result = await database.db.games.delete_one({"_id": ObjectId(game_id)})
        return result.deleted_count > 0
