"""add last few colums to posts table

Revision ID: a24e85dd184b
Revises: 7f9342e1a9f6
Create Date: 2025-12-05 07:35:20.704274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a24e85dd184b'
down_revision: Union[str, Sequence[str], None] = '7f9342e1a9f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", 
                  sa.Column(
                      "published", sa.Boolean, default=False, server_default="TRUE", nullable=False
                  ))
    op.add_column("posts", 
                  sa.Column(
                      "created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False
                  ))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
    pass
