"""Renaming grade to how many bananas

Revision ID: 22f01d1a3fd5
Revises: 791279dd0760
Create Date: 2023-03-28 06:12:55.954826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f01d1a3fd5'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade',new_column_name = 'how_many_bananas')


def downgrade() -> None:
    op.alter_column('students', 'how_many_bananas' , new_column_name = 'grade')
