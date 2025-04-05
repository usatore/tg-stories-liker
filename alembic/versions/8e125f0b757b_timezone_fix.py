"""timezone fix

Revision ID: 8e125f0b757b
Revises: 8e4e2e427a18
Create Date: 2025-04-05 17:53:40.064265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e125f0b757b'
down_revision: Union[str, None] = '8e4e2e427a18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
