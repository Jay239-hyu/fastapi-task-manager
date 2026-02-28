"""init

Revision ID: 825622df983f
Revises:
Create Date: 2026-02-26 11:38:38.409279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "825622df983f"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Intentionally empty.
    # Initial revision should not drop tables on a fresh database.
    pass


def downgrade() -> None:
    """Downgrade schema."""
    # Nothing to downgrade for the initial revision.
    pass