import strawberry

from app.models.game import GameResponse
from app.repositories.game_repository import GameRepository


@strawberry.type
class Game:
    id: str
    name: str
    type: str
    publisher_name: str
    external_game_id: str
    description: str
    is_featured: bool
    cover_image_url: str

    @classmethod
    def from_pydantic(cls, game: GameResponse):
        return cls(
            id=game.id,
            name=game.name,
            type=game.type,
            publisher_name=game.publisher_name,
            external_game_id=game.external_game_id,
            description=game.description,
            is_featured=game.is_featured,
            cover_image_url=game.cover_image_url,
        )


@strawberry.type
class Query:
    @strawberry.field
    async def games(self) -> list[Game]:
        games = await GameRepository.get_all_games()
        return [Game.from_pydantic(game) for game in games]

    @strawberry.field
    async def game(self, id: str) -> Game:
        game = await GameRepository.get_game(id)
        return Game.from_pydantic(game)
