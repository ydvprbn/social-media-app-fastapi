"""add content column to posts table

Revision ID: 049ea5d0b55a
Revises: 0022a7f863ca
Create Date: 2025-02-06 14:25:24.416981

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "049ea5d0b55a"
down_revision: Union[str, None] = "0022a7f863ca"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("content", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
