"""modify the pitch model

Revision ID: c9bf45489b0e
Revises: f6bc18931a1d
Create Date: 2022-03-13 14:10:00.082353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9bf45489b0e'
down_revision = 'f6bc18931a1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_category', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'pitch_category')
    # ### end Alembic commands ###