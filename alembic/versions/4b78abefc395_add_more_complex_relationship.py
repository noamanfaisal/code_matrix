"""Add more complex relationship

Revision ID: 4b78abefc395
Revises: 4fe52bfbfee9
Create Date: 2024-12-03 03:26:23.283842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b78abefc395'
down_revision: Union[str, None] = '4fe52bfbfee9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###