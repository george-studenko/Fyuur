"""empty message

Revision ID: 82063b2e30fc
Revises: ce6c73ab6071
Create Date: 2019-12-02 18:13:19.561421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82063b2e30fc'
down_revision = 'ce6c73ab6071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('City',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=40), nullable=True),
    sa.Column('state', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('city')
    op.add_column('Artist', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Artist', 'City', ['city_id'], ['id'])
    op.add_column('Venue', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Venue', 'City', ['city_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'city_id')
    op.drop_constraint(None, 'Artist', type_='foreignkey')
    op.drop_column('Artist', 'city_id')
    op.create_table('city',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('city', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='city_pkey')
    )
    op.drop_table('City')
    # ### end Alembic commands ###
