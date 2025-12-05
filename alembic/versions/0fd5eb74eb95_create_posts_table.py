"""create posts table

Revision ID: 0fd5eb74eb95
Revises: 
Create Date: 2025-12-05 06:12:14.370764

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fd5eb74eb95'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts", sa.Column(
        "id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String, nullable=False)
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
    pass
