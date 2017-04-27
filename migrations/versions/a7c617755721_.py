"""empty message

Revision ID: a7c617755721
Revises: 8aa8f8d6a0c3
Create Date: 2017-04-26 11:22:15.384545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7c617755721'
down_revision = '8aa8f8d6a0c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('licenses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('plain_text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users_licenses',
    sa.Column('user', sa.BigInteger(), nullable=True),
    sa.Column('license', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['license'], ['licenses.id'], ),
    sa.ForeignKeyConstraint(['user'], ['users.id'], )
    )
    op.drop_index('idx_areas_of_interest_centroid', table_name='areas_of_interest')
    op.drop_index('idx_areas_of_interest_geometry', table_name='areas_of_interest')
    op.add_column('projects', sa.Column('license_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_licenses', 'projects', 'licenses', ['license_id'], ['id'])
    op.drop_index('idx_tasks_geometry', table_name='tasks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_tasks_geometry', 'tasks', ['geometry'], unique=False)
    op.drop_constraint('fk_licenses', 'projects', type_='foreignkey')
    op.drop_column('projects', 'license_id')
    op.create_index('idx_areas_of_interest_geometry', 'areas_of_interest', ['geometry'], unique=False)
    op.create_index('idx_areas_of_interest_centroid', 'areas_of_interest', ['centroid'], unique=False)
    op.drop_table('users_licenses')
    op.drop_table('licenses')
    # ### end Alembic commands ###