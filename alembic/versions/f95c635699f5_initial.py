"""initial

Revision ID: f95c635699f5
Revises: 
Create Date: 2023-12-20 19:31:56.320110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f95c635699f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scholars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=55), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('enrolled_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_scholars_name'), 'scholars', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_scholars_name'), table_name='scholars')
    op.drop_table('scholars')
    # ### end Alembic commands ###