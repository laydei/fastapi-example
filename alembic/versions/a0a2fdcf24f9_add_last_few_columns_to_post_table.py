"""add last few columns to post table

Revision ID: a0a2fdcf24f9
Revises: 896e49e12506
Create Date: 2026-09-07 20:24:36.569112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0a2fdcf24f9'
down_revision: Union[str, Sequence[str], None] = '896e49e12506'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('published', sa.Boolean(), nullable=True, server_default='TRUE')
    )
    op.add_column(
        'posts',
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text('NOW()')
        )
    )


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
