"""empty message

Revision ID: 2505ad08a7d0
Revises: 8cd8609c0cd6
Create Date: 2020-08-12 11:41:27.239327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2505ad08a7d0'
down_revision = '8cd8609c0cd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('youtube_id', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'youtube_id')
    # ### end Alembic commands ###