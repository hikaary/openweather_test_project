"""second

Revision ID: 8fd822955b13
Revises: 64f601ab1e84
Create Date: 2023-07-24 16:53:42.614645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd822955b13'
down_revision = '64f601ab1e84'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('openweather', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'cities', ['city'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('openweather', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('city')

    # ### end Alembic commands ###
