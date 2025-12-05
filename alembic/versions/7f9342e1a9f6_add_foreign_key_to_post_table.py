"""add foreign-key to post table

Revision ID: 7f9342e1a9f6
Revises: 9d155979b5f1
Create Date: 2025-12-05 07:29:00.530472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f9342e1a9f6'
down_revision: Union[str, Sequence[str], None] = '9d155979b5f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", 
                  sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", 
                          referent_table="users",
                          local_cols=["owner_id"], 
                          remote_cols=['id'],
                          ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    """Downgrade schema."""
    pass
