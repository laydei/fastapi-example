"""add user table

Revision ID: 26d03f8896a4
Revises: 049073358b3c
Create Date: 2026-09-07 20:08:39.330247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26d03f8896a4'
down_revision: Union[str, Sequence[str], None] = '049073358b3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op. create_table('users',
        sa.Column ('id', sa.Integer(), nullable=False),
        sa.Column ('email', sa.String(), nullable=False),
        sa.Column ('password', sa.String(), nullable=False),
        sa.Column ('created_at', sa.TIMESTAMP (timezone=True),
                    server_default=sa. text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint ('email')
    )


def downgrade() -> None:
    op.drop_table('users')
