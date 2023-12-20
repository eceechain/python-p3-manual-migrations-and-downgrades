"""Renaming students to scholars

Revision ID: 3328df1129e3
Revises: f95c635699f5
Create Date: 2023-12-20 19:32:34.080795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3328df1129e3'
down_revision = 'f95c635699f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('students','scholars')
    # ### end Alembic commands ###


def downgrade():
   # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('scholars','students')
    # ### end Alembic commands ###