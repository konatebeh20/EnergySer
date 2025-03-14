"""Création de la table Properties avec la colonne global_active_power

Revision ID: e0588b0968d5
Revises: 
Create Date: 2025-03-14 15:08:51.400147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0588b0968d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recommander',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=False),
    sa.Column('recommander', sa.String(length=255), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['property_id'], ['properties.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.add_column(sa.Column('global_active_power', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('global_reactive_power', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('voltage', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('global_intensity', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('sub_metering_1', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('sub_metering_2', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('sub_metering_3', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('properties', schema=None) as batch_op:
        batch_op.drop_column('sub_metering_3')
        batch_op.drop_column('sub_metering_2')
        batch_op.drop_column('sub_metering_1')
        batch_op.drop_column('global_intensity')
        batch_op.drop_column('voltage')
        batch_op.drop_column('global_reactive_power')
        batch_op.drop_column('global_active_power')

    op.drop_table('recommander')
    # ### end Alembic commands ###
