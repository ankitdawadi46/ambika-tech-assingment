import strawberry

from typing import Optional

from app.models.game import GameCreate, GameUpdate
from app.repositories.game_repository import GameRepository
from app.schemas.query import Game


""" strawberry module for comminication with the GraphQL data"""
@strawberry.input
class GameCreateInput:
    name: str 
    type: str
    publisher_name: str 
    external_game_id: str
    description: str = ""
    is_featured: bool
    cover_image_url: str

    def to_pydantic(self) -> GameCreate:
        return GameCreate(**self.__dict__)
    
@strawberry.input
class GameUpdateInput:
    name: Optional[str] = None
    type: Optional[str] = None
    publisher_name: Optional[str] = strawberry.field(name="publisherName", default=None)
    external_game_id: Optional[str] = strawberry.field(name="externalGameId", default=None)
    description: Optional[str] = None
    is_featured: Optional[bool] = strawberry.field(name="isFeatured", default=None)
    cover_image_url: Optional[str] = strawberry.field(name="coverImageUrl", default=None)

    def to_pydantic(self) -> GameUpdate:
        return GameUpdate(**{
            "name": self.name,
            "type": self.type,
            "publisher_name": self.publisher_name,
            "external_game_id": self.external_game_id,
            "description": self.description,
            "is_featured": self.is_featured,
            "cover_image_url": self.cover_image_url
        })


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_game(self, game_data: GameCreateInput) -> Game:
        created_game = await GameRepository.create_game(game_data.to_pydantic())
        return Game.from_pydantic(created_game)

    @strawberry.mutation
    async def update_game(self, id: str, game_data: GameUpdateInput) -> Game:
        updated_game = await GameRepository.update_game(id, game_data.to_pydantic())
        return Game.from_pydantic(updated_game)

    @strawberry.mutation
    async def delete_game(self, id: str) -> bool:
        return await GameRepository.delete_game(id)
