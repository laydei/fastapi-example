"""add content column to posts table

Revision ID: 049073358b3c
Revises: c2019e442b12
Create Date: 2026-09-07 01:12:21.958905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '049073358b3c'
down_revision: Union[str, Sequence[str], None] = 'c2019e442b12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
