"""add content column to posts table

Revision ID: 8eee5836c771
Revises: 0fd5eb74eb95
Create Date: 2025-12-05 07:16:42.700373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8eee5836c771'
down_revision: Union[str, Sequence[str], None] = '0fd5eb74eb95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",
                  sa.Column("content", sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
