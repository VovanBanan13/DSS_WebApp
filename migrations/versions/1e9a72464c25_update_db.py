"""update db

Revision ID: 1e9a72464c25
Revises: d3a27c85c0fb
Create Date: 2021-05-11 18:49:51.498998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e9a72464c25'
down_revision = 'd3a27c85c0fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('material',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('thermal', sa.Integer(), nullable=True),
    sa.Column('depth', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_material_name'), 'material', ['name'], unique=True)
    op.add_column('region', sa.Column('duration', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('region', 'duration')
    op.drop_index(op.f('ix_material_name'), table_name='material')
    op.drop_table('material')
    # ### end Alembic commands ###